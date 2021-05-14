import datetime
from random import randrange

from cassandra.cluster import Cluster

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

for y in range(100, 200):
    today = datetime.datetime.now().date() - datetime.timedelta(days=y)
    for x in range(100, 1000):
        print(f'{int((x / 900) * 100)} %')
        terminal = f'H98{x}'
        monitoring_merchi_date = today
        monitoring_merchid = terminal
        monitoring_merchi_printing_error = 0
        monitoring_merchi_timeout = 0
        monitoring_merchi_transaction_type = 'RETIROS'
        monitoring_merchi_approved = randrange(100)
        monitoring_merchi_rejected = randrange(100)
        session.execute(prepared, [monitoring_merchi_date,
                                   monitoring_merchid,
                                   monitoring_merchi_transaction_type,
                                   monitoring_merchi_approved,
                                   monitoring_merchi_rejected,
                                   monitoring_merchi_printing_error,
                                   monitoring_merchi_timeout])
        monitoring_merchi_transaction_type = 'DEPOSITOS'
        monitoring_merchi_approved = randrange(100)
        monitoring_merchi_rejected = randrange(100)
        session.execute(prepared, [monitoring_merchi_date,
                                   monitoring_merchid,
                                   monitoring_merchi_transaction_type,
                                   monitoring_merchi_approved,
                                   monitoring_merchi_rejected,
                                   monitoring_merchi_printing_error,
                                   monitoring_merchi_timeout])
        monitoring_merchi_transaction_type = 'GIROS'
        monitoring_merchi_approved = randrange(100)
        monitoring_merchi_rejected = randrange(100)
        session.execute(prepared, [monitoring_merchi_date,
                                   monitoring_merchid,
                                   monitoring_merchi_transaction_type,
                                   monitoring_merchi_approved,
                                   monitoring_merchi_rejected,
                                   monitoring_merchi_printing_error,
                                   monitoring_merchi_timeout])
        monitoring_merchi_transaction_type = 'CONSULTAS'
        monitoring_merchi_approved = randrange(100)
        monitoring_merchi_rejected = randrange(100)
        session.execute(prepared, [monitoring_merchi_date,
                                   monitoring_merchid,
                                   monitoring_merchi_transaction_type,
                                   monitoring_merchi_approved,
                                   monitoring_merchi_rejected,
                                   monitoring_merchi_printing_error,
                                   monitoring_merchi_timeout])
# closing Cassandra connection
session.shutdown()
