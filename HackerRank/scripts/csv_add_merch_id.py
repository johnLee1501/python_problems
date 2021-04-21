import pandas as pd

input_csv = r'.\Global_POS_PILOTO_DIF12.csv'
ruta_serial_merch_id = r'.\serial_merch_id.csv'
column_serial_name = 'Serial_POS'
output_csv = 'csv_merch_id.csv'

if __name__ == '__main__':
    dataframe_csv = pd.read_csv(input_csv)
    dataframe_csv[column_serial_name] = dataframe_csv[column_serial_name].astype(str)
    columns_serial_merch_id = ['SERIAL_ID', 'MERCH_ID']
    merch_ids = pd.read_csv(ruta_serial_merch_id, names=columns_serial_merch_id, header=None)
    merch_ids[columns_serial_merch_id] = merch_ids[columns_serial_merch_id].astype(str)
    merch_ids['SERIAL_ID'] = '92' + merch_ids['SERIAL_ID']
    dict_serial_merch_id = dict(zip(merch_ids.SERIAL_ID, merch_ids.MERCH_ID))
    dataframe_csv.insert(2, 'Merch_id', dataframe_csv[column_serial_name].map(
        dict_serial_merch_id), True)
    dataframe_csv.to_csv(output_csv, index=False)
