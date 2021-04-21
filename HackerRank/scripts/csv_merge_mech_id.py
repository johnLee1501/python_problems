import pandas as pd

bcp_dataframe = pd.read_csv("TRX_BCP.csv", delimiter=';')
polaris_dataframe = pd.read_csv("Global_POS_PILOTO.csv", delimiter=';')
polaris_dataframe['Serial_POS'] = polaris_dataframe['Serial_POS'].astype(str)
concat_dataframes = pd.merge(bcp_dataframe, polaris_dataframe, on=['Fecha', 'Merch_id'], how='outer')
columns = list(concat_dataframes.columns.array)[2:]
columns.remove('Serial_POS')
concat_dataframes[columns] = concat_dataframes[columns].fillna(0).astype(int)
concat_dataframes['Serial_POS'] = concat_dataframes['Serial_POS'].fillna('Desconocido')
concat_dataframes.to_csv('merge_bcp_polaris.csv', index=False)
