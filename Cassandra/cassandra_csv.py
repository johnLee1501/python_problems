from cassandra.cluster import Cluster
import pandas as pd

train_dataframe = pd.read_csv('../data/train.csv')
pass
KEYSPACE = "pricepred"

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

session.execute("""
    CREATE KEYSPACE IF NOT EXISTS %s
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
    """ % KEYSPACE)

session.set_keyspace(KEYSPACE)
session.execute(
    """CREATE TABLE prices (
  rank2014 int,
  city varchar,
  state varchar,
  statecode varchar,
  popest2014 int,
  medprice2015 float,
  PRIMARY KEY (city, state, statecode)
);
"""
)

prepared = session.prepare("""
        INSERT INTO prices (rank2014, city, state, statecode, popest2014, medprice2015)
        VALUES (?, ?, ?, ?, ?, ?)
        """)

with open("../data/train.csv", "r") as row:
    for fare in row:
        columns = fare.strip().split(",")
        rank2014 = int(columns[0])
        city = columns[1]
        state = columns[2]
        statecode = columns[3]
        popest2014 = int(columns[4])
        medprice2015 = float(columns[5])
        session.execute(prepared, [rank2014, city, state, statecode, popest2014, medprice2015])

# closing the file
row.close()

# closing Cassandra connection
session.shutdown()
