from datetime import datetime
import pandas as pd
from glob import glob
import os
import re

ruta_carpetas = r'C:/WPOSS/LOGS_BCP'
lista_carpetas = os.listdir(ruta_carpetas)


def buscar_archivos(ruta):
    listar_archivos = glob(ruta)
    return listar_archivos


def leer(ruta_archivo):
    archivo = open(ruta_archivo, encoding='utf-8').read()
    lista_deposito = re.findall(
        r'\d{2}:\d{2}:\d{2} -  ==== startDeposito|\d{2}:\d{2}:\d{2} -  URL https://www.conex.agentesbcp.com/channel/ageb/v1/deposit/confirm-voucher-print',
        archivo)
    deposito = pd.Series(generar_lista_tiempos(lista_deposito), dtype='object')
    lista_retiro = re.findall(
        r'\d{2}:\d{2}:\d{2} -  ==== startRetiro|\d{2}:\d{2}:\d{2} -  URL https://www.conex.agentesbcp.com/channel/ageb/v1/withdrawal/confirm-voucher-print',
        archivo)
    retiro = pd.Series(generar_lista_tiempos(lista_retiro), dtype='object')
    lista_consulta = re.findall(
        r'\d{2}:\d{2}:\d{2} -  ==== startConsulta|\d{2}:\d{2}:\d{2} -  URL https://www.conex.agentesbcp.com/channel/ageb/v1/product-overview/confirm-voucher-print',
        archivo)
    consulta = pd.Series(generar_lista_tiempos(lista_consulta), dtype='object')
    lista_giro_emision = re.findall(
        r'\d{2}:\d{2}:\d{2} -  URL https://www.conex.agentesbcp.com/channel/ageb/v1/bank-draft-issue/execute-transaction|\d{2}:\d{2}:\d{2} -  URL https://www.conex.agentesbcp.com/channel/ageb/v1/bank-draft-issue/confirm-voucher-print',
        archivo)
    giro_emision = pd.Series(generar_lista_tiempos(lista_giro_emision), dtype='object')
    lista_giro_cobro = re.findall(
        r'\d{2}:\d{2}:\d{2} -  URL https://www.conex.agentesbcp.com/channel/ageb/v1/bank-draft-withdrawal/execute-transaction|\d{2}:\d{2}:\d{2} -  URL https://www.conex.agentesbcp.com/channel/ageb/v1/bank-draft-withdrawal/confirm-voucher-print',
        archivo)
    giro_cobro = pd.Series(generar_lista_tiempos(lista_giro_cobro), dtype='object')
    filas_dataframe = max(len(deposito), len(retiro), len(consulta), len(giro_emision), len(giro_cobro))
    info_archivo = ruta_archivo.split('/')[-1].split("_")
    fecha = pd.Series([f'{info_archivo[-1][-6:-4]}/{info_archivo[-1][-8:-6]}/{info_archivo[0][:4]}'] * filas_dataframe,
                      dtype='object')
    id_terminal = pd.Series([info_archivo[2]] * filas_dataframe, dtype='object')
    data = {'Fecha': fecha, 'Serial_POS': id_terminal, 'DEPOSITO': deposito,
            'RETIRO': retiro, 'CONSULTA': consulta, 'GIRO_EMISION': giro_emision,
            'GIRO_COBRO': giro_cobro}
    df = pd.DataFrame.from_dict(data, orient='index', dtype='object')
    df = df.transpose()
    return df


def generar_lista_tiempos(lista_transaccion):
    lista = []
    x = 0
    while x < (len(lista_transaccion) - 1):
        registro1 = lista_transaccion[x].split(" ")
        registro2 = lista_transaccion[x + 1].split(" ")
        if registro1[-1] != registro2[-1]:
            lista.append(
                int((datetime.strptime(registro2[0], '%H:%M:%S') - datetime.strptime(registro1[0],
                                                                                     '%H:%M:%S')).total_seconds()))
            x += 2
        else:
            x += 1
    return lista


if __name__ == '__main__':
    df_all = pd.DataFrame(columns=['Fecha', 'Serial_POS', 'DEPOSITO',
                                   'RETIRO', 'CONSULTA', 'GIRO_EMISION',
                                   'GIRO_COBRO'], dtype='object')
    for carpeta in lista_carpetas:
        ruta = f'{ruta_carpetas}/{carpeta}/*.txt'
        for archivo in buscar_archivos(ruta):
            df = leer(archivo)
            df_all = pd.concat([df_all, df], ignore_index=True)
    df_all.to_csv('tiempos.csv', index=False)
