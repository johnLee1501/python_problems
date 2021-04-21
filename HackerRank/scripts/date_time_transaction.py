from datetime import datetime
import pandas as pd
from glob import glob
import os
import re

path_main_folder = r'C:/WPOSS/LOGS_BCP'
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
columns_df = ['FECHA', 'SERIAL', 'HORA', 'TRX']


def search_file(path):
    list_files = glob(path)
    return list_files


def read(file_path, dataframe):
    file = open(file_path, encoding='utf-8').read()
    data = re.findall(
        r'(\d{2}:\d{2}:\d{2})[^\n]*(URL https://www.conex.agentesbcp.com/channel/ageb/v1/deposit/confirm-voucher-print|msgError : transEName DEPÓSITO|URL https://www.conex.agentesbcp.com/channel/ageb/v1/withdrawal/confirm-voucher-print|msgError : transEName RETIRO|URL https://www.conex.agentesbcp.com/channel/ageb/v1/bank-draft-issue/confirm-voucher-print|URL https://www.conex.agentesbcp.com/channel/ageb/v1/bank-draft-withdrawal/confirm-voucher-print|msgError : transEName GIROS|validarError getErr 0|URL https://www.conex.agentesbcp.com/channel/ageb/v1/product-overview/confirm-voucher-print|msgError : transEName CONSULTAS)',
        file)
    trx_dataframe = pd.DataFrame(data, columns=['HORA', 'URL'])
    trx_dataframe['TXR'] = trx_dataframe['URL'].map(dict_trx)
    pass


if __name__ == '__main__':
    df = pd.DataFrame(columns=columns_df, dtype='object')
    for folder in list_folder:
        ruta = f'{path_main_folder}/{folder}/*.txt'
        for file in search_file(ruta):
            df = read(file, df)
    df.to_csv('transaction_time.csv', index=False)
