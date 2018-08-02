'''
Created on 19 feb 2018

@author: Serena Sensini
'''
from sqlalchemy import Table, Column, Integer, String, Text, Numeric, MetaData, create_engine, UniqueConstraint

from modules.db.pyarchinit_conn_strings import Connection


class US_table:
    # connection string postgres"
    internal_connection = Connection()

    # create engine and metadata

    engine = create_engine(internal_connection.conn_str(), echo=False, convert_unicode=True)
    metadata = MetaData(engine)

    # define tables check per verifica fill fields 20/10/2016 OK
    us_table = Table('us_table', metadata,
                     Column('id_us', Integer, primary_key=True),  # 0
                     Column('sito', Text),  # 1
                     Column('area', String(4)),  # 2
                     Column('us', Integer),  # 3
                     Column('d_stratigrafica', String(100)),  # 4
                     Column('d_interpretativa', String(100)),  # 5
                     Column('descrizione', Text),  # 6
                     Column('interpretazione', Text),  # 7
                     Column('periodo_iniziale', String(4)),  # 8
                     Column('fase_iniziale', String(4)),  # 9
                     Column('periodo_finale', String(4)),  # 10
                     Column('fase_finale', String(4)),  # 11
                     Column('scavato', String(2)),  # 12
                     Column('attivita', String(4)),  # 13
                     Column('anno_scavo', String(4)),  # 14
                     Column('metodo_di_scavo', String(20)),  # 15
                     Column('inclusi', Text),  # 16
                     Column('campioni', Text),  # 17
                     Column('rapporti', Text),  # 18
                     Column('data_schedatura', String(20)),  # 19
                     Column('schedatore', String(25)),  # 20
                     Column('formazione', String(20)),  # 21
                     Column('stato_di_conservazione', String(20)),  # 22
                     Column('colore', String(20)),  # 23
                     Column('consistenza', String(20)),  # 24
                     Column('struttura', String(30)),  # 25
                     Column('cont_per', String(200)),  # 26
                     Column('order_layer', Integer),  # 27
                     Column('documentazione', Text),  # 28
                     Column('unita_tipo', Text),  # campi aggiunti per USM    #29
                     Column('settore', Text),  # 30
                     Column('quad_par', Text),  # 31
                     Column('ambient', Text),  # 32
                     Column('saggio', Text),  # 33
                     Column('elem_datanti', Text),  # 34
                     Column('funz_statica', Text),  # 35
                     Column('lavorazione', Text),  # 36
                     Column('spess_giunti', Text),  # 37
                     Column('letti_posa', Text),  # 38
                     Column('alt_mod', Text),  # 39
                     Column('un_ed_riass', Text),  # 40
                     Column('reimp', Text),  # 41
                     Column('posa_opera', Text),  # 42
                     Column('quota_min_usm', Numeric(6, 2)),  # 43
                     Column('quota_max_usm', Numeric(6, 2)),  # 44
                     Column('cons_legante', Text),  # 45
                     Column('col_legante', Text),  # 46
                     Column('aggreg_legante', Text),  # 47
                     Column('con_text_mat', Text),  # 48
                     Column('col_materiale', Text),  # 49
                     Column('inclusi_materiali_usm', Text),  # 50
                     Column('n_catalogo_generale', Text),  # 51 campi aggiunti per archeo 3.0 e allineamento ICCD
                     Column('n_catalogo_interno', Text),
                     Column('n_catalogo_internazionale', Text),
                     Column('soprintendenza', Text),
                     Column('quota_relativa', Numeric(6, 2)),
                     Column('quota_abs', Numeric(6, 2)),
                     Column('ref_tm', Text),
                     Column('ref_ra', Text),
                     Column('ref_n', Text),
                     Column('posizione', Text),
                     Column('criteri_distinzione', Text),
                     Column('modo_formazione', Text),
                     Column('componenti_organici', Text),
                     Column('componenti_inorganici', Text),
                     Column('lunghezza_max', Numeric(6,2)),
                     Column('altezza_max', Numeric(6,2)),
                     Column('altezza_min', Numeric(6,2)),
                     Column('profondità_max', Numeric(6,2)),
                     Column('profondità_min', Numeric(6,2)),
                     Column('larghezza_media', Numeric(6,2)),
                     Column('quota_max_abs', Numeric(6,2)),
                     Column('quota_max_rel', Numeric(6,2)),
                     Column('quota_min_abs', Numeric(6,2)),
                     Column('quota_min_rel', Numeric(6,2)),
                     Column('osservazioni', Text),
                     Column('datazione', Text),
                     Column('flottazione', Text),
                     Column('setacciatura', Text),
                     Column('affidabilita', Text),
                     Column('direttore_us', Text),
                     Column('responsabile_us', Text),
                     Column('responsabile_us', Text),
                     Column('cod_ente_schedatore', Text),
                     Column('responsabile_usm', Text),
                     Column('data_rilevazione', String(20)),
                     Column('data_rielaborazione', String(20)),
                     Column('lunghezza_usm', Numeric(6,2)),
                     Column('altezza_usm', Numeric(6,2)),
                     Column('spessore_usm', Numeric(6,2)),
                     Column('tecnica_muraria_usm', Numeric(6,2)),
                     Column('modulo_usm', Text),
                     Column('campioni_malta_usm', Text),
                     Column('campioni_mattone_usm', Text),
                     Column('campioni_pietra_usm', Text),
                     Column('provenienza_materiali_usm', Text),
                     Column('criteri_distinzione_usm', Text),
                     Column('uso_primario_usm', Text),

                     # explicit/composite unique constraint.  'name' is optional.
                     UniqueConstraint('sito', 'area', 'us', name='ID_us_unico')
                     )

    metadata.create_all(engine)
