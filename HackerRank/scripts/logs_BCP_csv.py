from glob import glob
import pandas as pd
import os

ruta_carpetas = r'C:/WPOSS/LOGS_BCP'
lista_carpetas = os.listdir(ruta_carpetas)


def buscar_archivos(ruta):
    listar_archivos = glob(ruta)
    return listar_archivos


def leer(ruta_archivo):
    archivo = open(ruta_archivo, encoding='utf-8').read()
    deposito01 = archivo.count(
        'URL https://www.conex.agentesbcp.com/channel/ageb/v1/deposit/confirm-voucher-print')
    deposito02 = archivo.count(
        'msgError : transEName DEPÓSITO')
    retiro01 = archivo.count('URL https://www.conex.agentesbcp.com/channel/ageb/v1/withdrawal/confirm-voucher-print')

    retiro02 = archivo.count('msgError : transEName RETIRO')

    giros_emision = archivo.count(
        'URL https://www.conex.agentesbcp.com/channel/ageb/v1/bank-draft-issue/confirm-voucher-print')
    giros_cobro = archivo.count(
        'URL https://www.conex.agentesbcp.com/channel/ageb/v1/bank-draft-withdrawal/confirm-voucher-print')
    giros01 = archivo.count('msgError : transEName GIROS')
    consultas01 = archivo.count(
        'URL https://www.conex.agentesbcp.com/channel/ageb/v1/product-overview/confirm-voucher-print')
    consultas02 = archivo.count('msgError : transEName CONSULTAS')
    excepcion = archivo.count('getErr 146')
    info_archivo = ruta_archivo.split('/')[-1].split("_")
    fecha = pd.Series(f'{info_archivo[-1][-6:-4]}/{info_archivo[-1][-8:-6]}/{info_archivo[0][:4]}')
    id_terminal = pd.Series(info_archivo[2])
    df = pd.DataFrame(
        {'Fecha': fecha, 'Serial_POS': id_terminal, 'Depositos Exitosos': deposito01,
         'Depositos Rechazados': deposito02, 'Retiros Exitosos': retiro01, 'Retiros Rechazados': retiro02,
         'Giros Emision Exitosos': giros_emision, 'Giros Cobro Exitosos': giros_cobro, 'Giros Rechazados': giros01,
         'Consultas Exitosas': consultas01, 'Consultas Fallidas': consultas02,
         'Error 146': excepcion})
    return df


if __name__ == '__main__':
    df_all = pd.DataFrame(columns=['Fecha', 'Serial_POS', 'Depositos Exitosos',
                                   'Depositos Rechazados', 'Retiros Exitosos', 'Retiros Rechazados',
                                   'Giros Emision Exitosos', 'Giros Cobro Exitosos', 'Giros Rechazados',
                                   'Consultas Exitosas', 'Consultas Fallidas',
                                   'Error 146'])
    for carpeta in lista_carpetas:
        ruta = f'{ruta_carpetas}/{carpeta}/*.txt'
        for archivo in buscar_archivos(ruta):
            df = leer(archivo)
            df_all = pd.concat([df_all, df], ignore_index=True)
    df_all.to_csv('resumen.csv', index=False)
