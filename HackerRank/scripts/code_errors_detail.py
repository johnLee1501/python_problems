from glob import glob
import pandas as pd
import os
import re

ruta_carpetas = r'C:/WPOSS/LOGS_BCP'
lista_carpetas = os.listdir(ruta_carpetas)


def buscar_archivos(ruta):
    listar_archivos = glob(ruta)
    return listar_archivos


def leer(ruta_archivo, df, index):
    archivo = open(ruta_archivo, encoding='utf-8').read()
    codes = set(re.findall(r'"code":"([A-Z\d]{6})"', archivo))
    info_archivo = ruta_archivo.split('/')[-1].split("_")
    fecha = f'{info_archivo[-1][-6:-4]}/{info_archivo[-1][-8:-6]}/{info_archivo[0][:4]}'
    id_terminal = info_archivo[2]
    for code in codes:
        pattern = r'(\d{2}:\d{2}:\d{2})[^\n]*\"code\"\:\"(%s)\"' % re.escape(code)
        code_records = re.findall(pattern, archivo)
        if code_records:
            for code_record in code_records:
                df = df.append(
                    {'FECHA': fecha, 'HORA': code_record[0], 'SERIAL_POS': id_terminal, 'CODE': code_record[1]},
                    ignore_index=True)
    print(f'{int(index * 100 / len(lista_carpetas))}% Completado')
    return df


if __name__ == '__main__':
    df = pd.DataFrame(
        columns=['FECHA', 'HORA', 'SERIAL_POS', 'CODE'])
    for index in range(len(lista_carpetas)):
        ruta = f'{ruta_carpetas}/{lista_carpetas[index]}/*.txt'
        for archivo in buscar_archivos(ruta):
            df = leer(archivo, df, index)
    df.to_csv('Code_details.csv', index=False)
