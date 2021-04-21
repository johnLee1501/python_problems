from datetime import datetime
import pandas as pd
from glob import glob
import os
import re

path_main_folder = r'C:/WPOSS/LOGS_BCP'
list_folder = os.listdir(path_main_folder)
columns_df = ['FECHA', 'HORA ENVÍO', 'HORA RECIBIDO', 'SERIAL', 'URL', 'TIEMPO DE EJECUCIÓN']
interval_time = 1  # Transacciones mayores o iguales a esta cantidad de segundos


def search_file(path):
    list_files = glob(path)
    return list_files



def read(file_path, dataframe):
    file = open(file_path, encoding='utf-8').read()
    list_transactions = re.findall(
        r'\b\d{2}:\d{2}:\d{2}[^\n]*URL\s+([^\n]+)(?:\n|\n[^\n]*\n)(\b\d{2}:\d{2}:\d{2})[^\n]*Enviando petición\n(\b\d{2}:\d{2}:\d{2})[^\n]*\n',
        file)
    info_file = file_path.split('/')[-1].split("_")
    date = f'{info_file[-1][-6:-4]}/{info_file[-1][-8:-6]}/{info_file[0][:4]}'
    terminal_serial = info_file[2]
    for transaction in list_transactions:
        start_time = transaction[1]
        end_time = transaction[2]
        time_transaction = int((datetime.strptime(end_time, '%H:%M:%S') - datetime.strptime(start_time,
                                                                                            '%H:%M:%S')).total_seconds())
        if time_transaction >= interval_time:
            dataframe = dataframe.append(
                {'FECHA': date, 'HORA ENVÍO': start_time, 'HORA RECIBIDO': end_time, 'SERIAL': terminal_serial,
                 'URL': transaction[0], 'TIEMPO DE EJECUCIÓN': time_transaction},
                ignore_index=True)
    return dataframe


if __name__ == '__main__':
    df = pd.DataFrame(columns=columns_df, dtype='object')
    for folder in list_folder:
        ruta = f'{path_main_folder}/{folder}/*.txt'
        for file in search_file(ruta):
            df = read(file, df)
            df.to_csv('transaction_time.csv', index=False)
