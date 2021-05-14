from glob import glob
import pandas as pd
import os

ruta_carpetas = r'C:/WPOSS/LOGS_BCP'
ruta_serial_merch_id = r'..\..\data\serial_merch_id.csv'
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
    giros02 = archivo.count('validarError getErr 0')
    consultas01 = archivo.count(
        'URL https://www.conex.agentesbcp.com/channel/ageb/v1/product-overview/confirm-voucher-print')
    consultas02 = archivo.count('msgError : transEName CONSULTAS')
    excepcion = archivo.count('getErr 146')
    info_archivo = ruta_archivo.split('/')[-1].split("_")
    fecha = pd.Series(f'{info_archivo[-1][-6:-4]}/{info_archivo[-1][-8:-6]}/{info_archivo[0][:4]}')
    id_terminal = pd.Series(info_archivo[2])
    df = pd.DataFrame(
        {'Fecha': fecha, 'Serial_POS': id_terminal, 'Depositos Procesadas': deposito01,
         'Depositos Rechazados': deposito02, 'Retiros Procesadas': retiro01, 'Retiros Rechazados': retiro02,
         'Giros Emision Procesadas': giros_emision, 'Giros Cobro Procesadas': giros_cobro,
         'Giros Rechazados 01': giros01, 'Giros Rechazados 02': giros02,
         'Consultas Procesadas': consultas01, 'Consultas Rechazadas': consultas02})
    return df


if __name__ == '__main__':
    columns_serial_merch_id = ['SERIAL_ID', 'MERCH_ID']
    merch_ids = pd.read_csv(ruta_serial_merch_id, names=columns_serial_merch_id, header=None)
    merch_ids[columns_serial_merch_id] = merch_ids[columns_serial_merch_id].astype(str)
    merch_ids['SERIAL_ID'] = '92' + merch_ids['SERIAL_ID']
    dict_serial_merch_id = dict(zip(merch_ids.SERIAL_ID, merch_ids.MERCH_ID))
    df_all = pd.DataFrame(columns=['Fecha', 'Serial_POS', 'Depositos Procesadas',
                                   'Depositos Rechazados', 'Retiros Procesadas', 'Retiros Rechazados',
                                   'Giros Emision Procesadas', 'Giros Cobro Procesadas', 'Giros Rechazados 01',
                                   'Giros Rechazados 02',
                                   'Consultas Procesadas', 'Consultas Rechazadas'])
    for carpeta in lista_carpetas:
        ruta = f'{ruta_carpetas}/{carpeta}/*.txt'
        for archivo in buscar_archivos(ruta):
            df = leer(archivo)
            df_all = pd.concat([df_all, df], ignore_index=True)
    df_all = df_all.groupby(['Fecha', 'Serial_POS']).sum().reset_index()
    df_all.insert(2, 'Merch_id', df_all['Serial_POS'].map(
        dict_serial_merch_id), True)

    df_all.to_csv('Global_POS_PILOTO.csv', index=False)
