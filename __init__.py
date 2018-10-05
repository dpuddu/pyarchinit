# -*- coding: utf-8 -*-
"""
/***************************************************************************
        pyArchInit Plugin  - A QGIS plugin to manage archaeological dataset
                             -------------------
        begin                : 2007-12-01
        copyright            : (C) 2008 by Luca Mandolesi
        email                : mandoluca at gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import re
import traceback

import sys
from qgis.core import QgsMessageLog, Qgis, QgsSettings

from .modules.utility.pyarchinit_OS_utility import Pyarchinit_OS_Utility
from .modules.utility.pyarchinit_folder_installation import pyarchinit_Folder_installation

sys.path.append(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'resources')))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'gui', 'ui')))

pyarchinit_home = os.path.expanduser("~") + os.sep + 'pyarchinit'
fi = pyarchinit_Folder_installation()
if not os.path.exists(pyarchinit_home):
    fi.install_dir()
else:
    os.environ['PYARCHINIT_HOME'] = pyarchinit_home

confing_path = os.path.join(os.sep, pyarchinit_home, 'pyarchinit_DB_folder', 'config.cfg')
if not os.path.isfile(confing_path):
    fi.installConfigFile(os.path.dirname(confing_path))

missing_libraries = []
try:
    import pyper
except Exception as e:
    missing_libraries.append(str(e))

try:
    import graphviz
except Exception as e:
    missing_libraries.append(str(e))

try:
    import sqlalchemy
except Exception as e:
    missing_libraries.append(str(e))

try:
    import reportlab
except Exception as e:
    missing_libraries.append(str(e))

try:
    import matplotlib
except Exception as e:
    missing_libraries.append(str(e))

try:
    import networkx
except Exception as e:
    missing_libraries.append(str(e))

try:
    import sqlalchemy_utils
except Exception as e:
    missing_libraries.append(str(e))

install_libraries = []
for l in missing_libraries:
    p = re.findall(r"'(.*?)'", l)
    install_libraries.append(p[0])

if install_libraries:
    from qgis.PyQt.QtWidgets import QMessageBox

    res = QMessageBox.warning(None, 'PyArchInit', "Some of the required packages are missing from your machine:\n{}\n\n"
                                                  "Do you want install the missing packages?".format(
        ',\n'.join(missing_libraries)), QMessageBox.Ok | QMessageBox.Cancel)
    if res == QMessageBox.Ok:
        import subprocess

        try:
            cmd = 'python3'
            subprocess.call([cmd,'{}'.format(os.path.join(os.path.dirname(__file__), 'scripts', 'modules_installer.py')),
                             ','.join(install_libraries)], shell=True if Pyarchinit_OS_Utility.isWindows() else False)
        except Exception as e:
            error = traceback.format_exc()
            QgsMessageLog.logMessage(error, tag="PyArchInit", level=Qgis.Critical)
    else:
        pass

s = QgsSettings()
if not Pyarchinit_OS_Utility.checkGraphvizInstallation() and s.value('pyArchInit/graphvizBinPath'):
    os.environ['PATH'] += os.pathsep + os.path.normpath(s.value('pyArchInit/graphvizBinPath'))


def classFactory(iface):
    from .pyarchinitPlugin import PyArchInitPlugin
    return PyArchInitPlugin(iface)
