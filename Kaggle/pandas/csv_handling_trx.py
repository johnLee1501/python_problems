import pandas as pd

reviews = pd.read_excel("../data/Libro3.xlsx")
reviews['FECDIA'] = reviews['FECDIA'].dt.date
reviews['TIPESTTRANSACCIONAGENTEVIABCP'] = reviews['TIPESTTRANSACCIONAGENTEVIABCP'].map(
    {'P': 'PROCESADOS', 'R': 'RECHAZADOS'})
reviews['TRANSACCION'] = reviews['DESTIPTRANSACCIONAGENTEVIABCP'] + " " + reviews['TIPESTTRANSACCIONAGENTEVIABCP']
reviews = reviews.drop(['TIPESTTRANSACCIONAGENTEVIABCP', 'TIPTRANSACCIONAGENTEVIABCP', 'DESTIPTRANSACCIONAGENTEVIABCP'],
                       axis=1)
transaction_dataframe = reviews.pivot(index=['FECDIA', 'CODAGENTEVIABCP'], columns='TRANSACCION',
                                      values='COUNT(*)').reset_index()
columns_count = list(transaction_dataframe.columns.array)[2:]
transaction_dataframe = transaction_dataframe.fillna(0)
transaction_dataframe[columns_count] = transaction_dataframe[columns_count].astype(int)
transaction_dataframe.to_csv('transaction_bcp.csv', index=False)
