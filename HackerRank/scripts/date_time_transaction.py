from datetime import datetime
import pandas as pd
from glob import glob
import os
import re

path_main_folder = r'C:/WPOSS/LOGS_BCP'
path_serial_merch_id = r'.\serial_merch_id.csv'
list_folder = os.listdir(path_main_folder)
dict_trx = {
    'URL https://www.conex.agentesbcp.com/channel/ageb/v1/deposit/confirm-voucher-print': 'DEPÓSITOS PROCESADOS',
    'msgError : transEName DEPÓSITO': 'DEPÓSITOS RECHAZADOS',
    'URL https://www.conex.agentesbcp.com/channel/ageb/v1/withdrawal/confirm-voucher-print': 'RETIROS PROCESADOS',
    'msgError : transEName RETIRO': 'RETIROS RECHAZADOS',
    'URL https://www.conex.agentesbcp.com/channel/ageb/v1/bank-draft-issue/confirm-voucher-print': 'GIROS EMISIÓN PROCESADOS',
    'msgError : transEName GIROS': 'GIROS RECHAZADOS 01',
    'validarError getErr 0': 'GIROS RECHAZADOS 02',
    'URL https://www.conex.agentesbcp.com/channel/ageb/v1/bank-draft-withdrawal/confirm-voucher-print': 'GIROS COBROS PROCESADOS',
    'URL https://www.conex.agentesbcp.com/channel/ageb/v1/product-overview/confirm-voucher-print': 'CONSULTAS PROCESADAS',
    'msgError : transEName CONSULTAS': 'CONSULTAS RECHAZADAS'}
columns_df = ['FECHA', 'HORA', 'SERIAL', 'TRX']


def search_file(path):
    list_files = glob(path)
    return list_files


def read(file_path, dataframe, i):
    file = open(file_path, encoding='utf-8').read()
    info_file = file_path.split('/')[-1].split("_")
    date = f'{info_file[-1][-6:-4]}/{info_file[-1][-8:-6]}/{info_file[0][:4]}'
    terminal_serial = info_file[2]
    data = re.findall(
        r'(\d{2}:\d{2}:\d{2})[^\n]*(URL https://www.conex.agentesbcp.com/channel/ageb/v1/deposit/confirm-voucher-print|msgError : transEName DEPÓSITO|URL https://www.conex.agentesbcp.com/channel/ageb/v1/withdrawal/confirm-voucher-print|msgError : transEName RETIRO|URL https://www.conex.agentesbcp.com/channel/ageb/v1/bank-draft-issue/confirm-voucher-print|URL https://www.conex.agentesbcp.com/channel/ageb/v1/bank-draft-withdrawal/confirm-voucher-print|msgError : transEName GIROS|validarError getErr 0|URL https://www.conex.agentesbcp.com/channel/ageb/v1/product-overview/confirm-voucher-print|msgError : transEName CONSULTAS)',
        file)
    trx_dataframe = pd.DataFrame(data, columns=['HORA', 'URL'])
    trx_dataframe['TRX'] = trx_dataframe['URL'].map(dict_trx)
    trx_dataframe.insert(0, 'FECHA', date)
    trx_dataframe.insert(1, 'SERIAL', terminal_serial)
    dataframe = dataframe.append(trx_dataframe, ignore_index=True)
    print(f'{int(i * 100 / len(list_folder))}% Completado')
    return dataframe


if __name__ == '__main__':
    columns_serial_merch_id = ['SERIAL_ID', 'MERCH_ID']
    merch_ids = pd.read_csv(path_serial_merch_id, names=columns_serial_merch_id, header=None)
    merch_ids[columns_serial_merch_id] = merch_ids[columns_serial_merch_id].astype(str)
    merch_ids['SERIAL_ID'] = '92' + merch_ids['SERIAL_ID']
    dict_serial_merch_id = dict(zip(merch_ids.SERIAL_ID, merch_ids.MERCH_ID))
    df = pd.DataFrame(columns=columns_df, dtype='object')
    for index in range(len(list_folder)):
        ruta = f'{path_main_folder}/{list_folder[index]}/*.txt'
        for file in search_file(ruta):
            df = read(file, df, index)
    df = df.drop(['URL'], axis=1)
    df.insert(2, 'MERCH_ID', df['SERIAL'].map(dict_serial_merch_id), True)
    print('100% Completado')
    df.to_csv('transaction_time.csv', index=False)
