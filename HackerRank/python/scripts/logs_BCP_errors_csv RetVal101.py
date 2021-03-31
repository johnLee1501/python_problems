from collections import Counter
import pandas as pd
from glob import glob
import os
import re

ruta_carpetas = r'C:/WPOSS/LOGS_BCP'
lista_carpetas = os.listdir(ruta_carpetas)
error_msgs = [f'ERROR {str(x)}' for x in range(101, 184)]
columnas_base = ['FECHA', 'SERIAL', 'TIPO TRX']
columnas_errores = columnas_base + ['HORA']
columnas_errores_group = columnas_base + error_msgs + ['RetVal 101']


def buscar_archivos(ruta):
    listar_archivos = glob(ruta)
    return listar_archivos


def leer(ruta_archivo):
    archivo = open(ruta_archivo, encoding='utf-8').read()
    lista_transacciones = re.findall(
        r'(\d{2}:\d{2}:\d{2}) -  msgError : transEName ([\w]*)\n\d{2}:\d{2}:\d{2} -  msgError : retVal (\d{3})',
        archivo)
    retVal101_list = re.findall(r'(\d{2}:\d{2}:\d{2})\s-\s+retVal\s+:\s+(101)', archivo)
    info_archivo = ruta_archivo.split('/')[-1].split("_")
    fecha = f'{info_archivo[-1][-6:-4]}/{info_archivo[-1][-8:-6]}/{info_archivo[0][:4]}'
    id_terminal = info_archivo[2]
    df = pd.DataFrame(columns=columnas_errores)
    df_agrupado = pd.DataFrame(columns=columnas_errores_group)
    for transaccion in lista_transacciones:
        hora = transaccion[0]
        tipo_trx = transaccion[1]
        cod_error = transaccion[2]
        df = df.append(
            {'HORA': hora, 'FECHA': fecha, 'SERIAL': id_terminal, 'COD ERROR': cod_error, 'TIPO TRX': tipo_trx},
            ignore_index=True
        )
    for type_transaction in set(df['TIPO TRX']):
        data = {'FECHA': fecha, 'SERIAL': id_terminal, 'TIPO TRX': type_transaction}
        group_errors = Counter(df[df['TIPO TRX'] == type_transaction]['COD ERROR'])
        for k, v in group_errors.items():
            data[f'ERROR {k}'] = v
        df_agrupado = df_agrupado.append(data, ignore_index=True)
    for retVal101 in retVal101_list:
        df = df.append(
            {'HORA': retVal101[0], 'FECHA': fecha, 'SERIAL': id_terminal, 'COD ERROR': retVal101[1],
             'TIPO TRX': 'INICIALIZACIÓN'},
            ignore_index=True
        )
    if retVal101_list:
        df_agrupado = df_agrupado.append(
            {'FECHA': fecha, 'SERIAL': id_terminal, 'TIPO TRX': 'INICIALIZACIÓN', 'RetVal 101': len(retVal101_list)},
            ignore_index=True)
    return df, df_agrupado


if __name__ == '__main__':
    df_all = pd.DataFrame(columns=columnas_errores)
    df_agrupados = pd.DataFrame(columns=columnas_errores_group)
    for carpeta in lista_carpetas:
        ruta = f'{ruta_carpetas}/{carpeta}/*.txt'
        for archivo in buscar_archivos(ruta):
            df, df_groups = leer(archivo)
            df_all = pd.concat([df_all, df], ignore_index=True)
            df_agrupados = pd.concat([df_agrupados, df_groups], ignore_index=True)
    df_agrupados = df_agrupados.fillna(0)
    df_all.to_csv('errors.csv', index=False, encoding="utf-8")
    df_agrupados.to_csv('errors_groups.csv', index=False, encoding="utf-8")
