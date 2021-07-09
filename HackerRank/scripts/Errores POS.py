import sys
from glob import glob
import pandas as pd
import os

ruta_carpetas = r'C:\WPOSS\ANALIZAR'
lista_carpetas = os.listdir(ruta_carpetas)
len_list_carpetas = len(lista_carpetas)


def buscar_archivos(ruta):
    listar_archivos = glob(ruta)
    return listar_archivos


def leer(ruta_archivo, index):
    try:
        archivo = open(ruta_archivo).read()
    except:
        print(ruta_archivo)
        sys.exit()
    E101 = archivo.count('msgError : retVal 101')
    E103 = archivo.count('msgError : retVal 103')
    E102 = archivo.count('msgError : retVal 102')
    E104 = archivo.count('msgError : retVal 104')
    E105 = archivo.count('msgError : retVal 105')
    E106 = archivo.count('msgError : retVal 106')
    E107 = archivo.count('msgError : retVal 107')
    E109 = archivo.count('msgError : retVal 109')
    E110 = archivo.count('msgError : retVal 110')
    E114 = archivo.count('msgError : retVal 114')
    E116 = archivo.count('msgError : retVal 116')
    E117 = archivo.count('msgError : retVal 117')
    E119 = archivo.count('msgError : retVal 119')
    E120 = archivo.count('msgError : retVal 120')
    E121 = archivo.count('msgError : retVal 121')
    E122 = archivo.count('msgError : retVal 122')
    E123 = archivo.count('msgError : retVal 123')
    E126 = archivo.count('msgError : retVal 126')
    E127 = archivo.count('msgError : retVal 127')
    E128 = archivo.count('msgError : retVal 128')
    E129 = archivo.count('msgError : retVal 129')
    E130 = archivo.count('msgError : retVal 130')
    E131 = archivo.count('msgError : retVal 131')
    E133 = archivo.count('msgError : retVal 133')
    E134 = archivo.count('msgError : retVal 134')
    E135 = archivo.count('msgError : retVal 135')
    E136 = archivo.count('msgError : retVal 136')
    E137 = archivo.count('msgError : retVal 137')
    E138 = archivo.count('msgError : retVal 138')
    E139 = archivo.count('msgError : retVal 139')
    E140 = archivo.count('msgError : retVal 140')
    E141 = archivo.count('msgError : retVal 141')
    E142 = archivo.count('msgError : retVal 142')
    E144 = archivo.count('msgError : retVal 144')
    E146 = archivo.count('msgError : retVal 146')
    E147 = archivo.count('msgError : retVal 147')
    E001 = archivo.count('validarError getErr 0')
    E148 = archivo.count('msgError : retVal 148')
    E149 = archivo.count('msgError : retVal 149')
    E150 = archivo.count('msgError : retVal 150')
    E152 = archivo.count('msgError : retVal 152')
    E153 = archivo.count('msgError : retVal 153')
    E154 = archivo.count('msgError : retVal 154')
    E155 = archivo.count('msgError : retVal 155')
    E158 = archivo.count('msgError : retVal 158')
    E159 = archivo.count('msgError : retVal 159')
    E160 = archivo.count('msgError : retVal 160')
    E163 = archivo.count('msgError : retVal 163')
    E164 = archivo.count('msgError : retVal 164')
    E165 = archivo.count('msgError : retVal 165')
    E166 = archivo.count('msgError : retVal 166')
    E167 = archivo.count('msgError : retVal 167')
    E168 = archivo.count('msgError : retVal 168')
    E169 = archivo.count('msgError : retVal 169')
    E170 = archivo.count('msgError : retVal 170')
    E171 = archivo.count('msgError : retVal 171')
    E172 = archivo.count('msgError : retVal 172')
    E173 = archivo.count('msgError : retVal 173')
    E174 = archivo.count('msgError : retVal 174')
    E175 = archivo.count('msgError : retVal 175')
    E176 = archivo.count('msgError : retVal 176')
    E177 = archivo.count('msgError : retVal 177')
    E178 = archivo.count('msgError : retVal 178')
    E179 = archivo.count('msgError : retVal 179')
    E180 = archivo.count('msgError : retVal 180')
    E181 = archivo.count('msgError : retVal 181')
    E182 = archivo.count('msgError : retVal 182')
    E183 = archivo.count('msgError : retVal 183')
    info_archivo = ruta_archivo.split('/')[-1].split("_")
    fecha = pd.Series(f'{info_archivo[-1][-6:-4]}/{info_archivo[-1][-8:-6]}/{info_archivo[0][:4]}')
    id_terminal = pd.Series(info_archivo[2])
    df = pd.DataFrame(
        {'Fecha': fecha, 'Serial_POS': id_terminal, 'ERROR 101': E101, 'ERROR 103': E103, 'ERROR 102': E102,
         'ERROR 104': E104, 'ERROR 105': E105, 'ERROR 106': E106,
         'ERROR 107': E107, 'ERROR 109': E109, 'ERROR 110': E110, 'ERROR 114': E114, 'ERROR 116': E116,
         'ERROR 117': E117, 'ERROR 119': E119, 'ERROR 120': E120,
         'ERROR 121': E121, 'ERROR 122': E122, 'ERROR 123': E123, 'ERROR 126': E126, 'ERROR 127': E127,
         'ERROR 128': E128, 'ERROR 129': E129, 'ERROR 130': E130,
         'ERROR 131': E131, 'ERROR 133': E133, 'ERROR 134': E134, 'ERROR 135': E135, 'ERROR 136': E136,
         'ERROR 137': E137, 'ERROR 138': E138, 'ERROR 139': E139,
         'ERROR 140': E140, 'ERROR 141': E141, 'ERROR 142': E142, 'ERROR 144': E144, 'ERROR 146': E146,
         'ERROR 147': E147, 'ERROR 001': E001, 'ERROR 148': E148,
         'ERROR 149': E149, 'ERROR 150': E150, 'ERROR 152': E152, 'ERROR 153': E153, 'ERROR 154': E154,
         'ERROR 155': E155, 'ERROR 158': E158, 'ERROR 159': E159,
         'ERROR 160': E160, 'ERROR 163': E163, 'ERROR 164': E164, 'ERROR 165': E165, 'ERROR 166': E166,
         'ERROR 167': E167, 'ERROR 168': E168, 'ERROR 169': E169,
         'ERROR 170': E170, 'ERROR 171': E171, 'ERROR 172': E172, 'ERROR 173': E173, 'ERROR 174': E174,
         'ERROR 175': E175, 'ERROR 176': E176, 'ERROR 177': E177,
         'ERROR 178': E178, 'ERROR 179': E179, 'ERROR 180': E180, 'ERROR 181': E181, 'ERROR 182': E182,
         'ERROR 183': E183, })
    print(f'{int(index * 100 / len_list_carpetas)}% Completado')
    return df


if __name__ == '__main__':
    df_all = pd.DataFrame(
        columns=['Fecha', 'Serial_POS', 'ERROR 101', 'ERROR 103', 'ERROR 102', 'ERROR 104', 'ERROR 105', 'ERROR 106',
                 'ERROR 107', 'ERROR 109', 'ERROR 110', 'ERROR 114', 'ERROR 116', 'ERROR 117',
                 'ERROR 119', 'ERROR 120', 'ERROR 121', 'ERROR 122', 'ERROR 123', 'ERROR 126', 'ERROR 127', 'ERROR 128',
                 'ERROR 129', 'ERROR 130', 'ERROR 131', 'ERROR 133', 'ERROR 134', 'ERROR 135',
                 'ERROR 136', 'ERROR 137', 'ERROR 138', 'ERROR 139', 'ERROR 140', 'ERROR 141', 'ERROR 142', 'ERROR 144',
                 'ERROR 146', 'ERROR 147', 'ERROR 001', 'ERROR 148', 'ERROR 149', 'ERROR 150',
                 'ERROR 152', 'ERROR 153', 'ERROR 154', 'ERROR 155', 'ERROR 158', 'ERROR 159', 'ERROR 160', 'ERROR 163',
                 'ERROR 164', 'ERROR 165', 'ERROR 166', 'ERROR 167', 'ERROR 168', 'ERROR 169',
                 'ERROR 170', 'ERROR 171', 'ERROR 172', 'ERROR 173', 'ERROR 174', 'ERROR 175', 'ERROR 176', 'ERROR 177',
                 'ERROR 178', 'ERROR 179', 'ERROR 180', 'ERROR 181', 'ERROR 182', 'ERROR 183'])
    for index in range(len_list_carpetas):
        ruta = f'{ruta_carpetas}/{lista_carpetas[index]}/*.txt'
        for archivo in buscar_archivos(ruta):
            df = leer(archivo, index)
            df_all = pd.concat([df_all, df], ignore_index=True)
    print('100% Completado')
    df_all.to_csv('Error_GLOBAL_BCP.csv', index=False)
