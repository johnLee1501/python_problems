import re
from glob import glob
import pandas as pd
import os

ruta_carpetas = r'C:/WPOSS/LOGS_BCP'
lista_carpetas = os.listdir(ruta_carpetas)


def buscar_archivos(ruta):
    listar_archivos = glob(ruta)
    return listar_archivos


def leer(ruta_archivo, df, codes):
    dict_temporal = {}
    archivo = open(ruta_archivo, encoding='utf-8').read()
    info_archivo = ruta_archivo.split('/')[-1].split("_")
    fecha = f'{info_archivo[-1][-6:-4]}/{info_archivo[-1][-8:-6]}/{info_archivo[0][:4]}'
    id_terminal = info_archivo[2]
    codes_temporal = set(re.findall(r'"code":"([A-Z\d]{6})"', archivo))
    new_codes = codes_temporal.difference(codes)
    codes = codes_temporal.union(codes)
    for new_code in list(new_codes):
        df[new_code] = 0
    for code_temporal in list(codes_temporal):
        count_code = archivo.count(r'"code":"%s"' % re.escape(code_temporal))
        if dict_temporal.get(code_temporal, None):
            dict_temporal[code_temporal] += count_code
        else:
            dict_temporal[code_temporal] = count_code
    if dict_temporal:
        dict_temporal['FECHA'] = fecha
        dict_temporal['SERIAL_POS'] = id_terminal
        df = df.append(dict_temporal, ignore_index=True)
    return df, codes


if __name__ == '__main__':
    codes = ['BI0210', 'BI0220', 'BI0330', 'BI0430', 'DE0011', 'DE0210', 'DE0220', 'DE0420', 'DE0430', 'DE0530',
             'DW0101',
             'DW0103', 'PO0210', 'PO0230', 'TL0007', 'TL9999', 'WD0102', 'WD0202', 'WD0401', 'WD0403']
    df = pd.DataFrame(
        columns=['FECHA', 'SERIAL_POS'] + codes)
    dict_temporal = {}
    for carpeta in lista_carpetas:
        ruta = f'{ruta_carpetas}/{carpeta}/*.txt'
        for archivo in buscar_archivos(ruta):
            df, codes = leer(archivo, df, codes)
    df = df.fillna(0)
    df[list(codes)] = df[list(codes)].astype(int)
    df = df.groupby(['FECHA', 'SERIAL_POS']).sum().reset_index()
    df.to_csv('codes_groupby_fecha_terminal.csv', index=False)
    df = df.drop(['SERIAL_POS'], axis=1)
    df = df.groupby(['FECHA']).sum().reset_index()
    df.to_csv('codes_groupby_fecha.csv', index=False)

