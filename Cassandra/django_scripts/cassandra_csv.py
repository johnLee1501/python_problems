import datetime

import pandas as pd
from cassandra.cluster import Cluster

dataframe = pd.read_csv('./data.csv')
dataframe.drop('Serial_POS', axis=1)
KEYSPACE = "monitoreo_general"

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.set_keyspace(KEYSPACE)

prepared = session.prepare("""
        INSERT INTO general_monitoring_by_merch_id (monitoring_merchi_date,
                                                    monitoring_merchid,
                                                    monitoring_merchi_transaction_type,
                                                    monitoring_merchi_approved,
                                                    monitoring_merchi_rejected,
                                                    monitoring_merchi_printing_error,
                                                    monitoring_merchi_timeout)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """)

for index, row in dataframe.iterrows():
    print(f'Index: {index}')
    monitoring_merchi_date = datetime.datetime.strptime(row.get("Fecha"), "%d/%m/%Y").date()
    monitoring_merchid = row.get("Merch_id")
    monitoring_merchi_printing_error = 0
    monitoring_merchi_timeout = 0
    monitoring_merchi_transaction_type = 'RETIROS'
    monitoring_merchi_approved = row.get("Retiros Procesadas")
    monitoring_merchi_rejected = row.get("Retiros Rechazados")
    session.execute(prepared, [monitoring_merchi_date,
                               monitoring_merchid,
                               monitoring_merchi_transaction_type,
                               monitoring_merchi_approved,
                               monitoring_merchi_rejected,
                               monitoring_merchi_printing_error,
                               monitoring_merchi_timeout])
    monitoring_merchi_transaction_type = 'DEPOSITOS'
    monitoring_merchi_approved = row.get("Depositos Procesadas")
    monitoring_merchi_rejected = row.get("Depositos Rechazados")
    session.execute(prepared, [monitoring_merchi_date,
                               monitoring_merchid,
                               monitoring_merchi_transaction_type,
                               monitoring_merchi_approved,
                               monitoring_merchi_rejected,
                               monitoring_merchi_printing_error,
                               monitoring_merchi_timeout])
    monitoring_merchi_transaction_type = 'GIROS'
    monitoring_merchi_approved = row.get("Giros Emision Procesadas") + row.get("Giros Cobro Procesadas")
    monitoring_merchi_rejected = row.get("Giros Rechazados 01") + row.get("Giros Rechazados 02")
    session.execute(prepared, [monitoring_merchi_date,
                               monitoring_merchid,
                               monitoring_merchi_transaction_type,
                               monitoring_merchi_approved,
                               monitoring_merchi_rejected,
                               monitoring_merchi_printing_error,
                               monitoring_merchi_timeout])
    monitoring_merchi_transaction_type = 'CONSULTAS'
    monitoring_merchi_approved = row.get("Consultas Procesadas")
    monitoring_merchi_rejected = row.get("Consultas Rechazadas")
    session.execute(prepared, [monitoring_merchi_date,
                               monitoring_merchid,
                               monitoring_merchi_transaction_type,
                               monitoring_merchi_approved,
                               monitoring_merchi_rejected,
                               monitoring_merchi_printing_error,
                               monitoring_merchi_timeout])
# closing Cassandra connection
session.shutdown()
