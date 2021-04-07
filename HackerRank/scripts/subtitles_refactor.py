import collections
import re
from glob import glob

ruta_carpeta = r'C:/subtitles'


def buscar_archivos(ruta):
    listar_archivos = glob(ruta)
    return listar_archivos


def leer(ruta_archivo):
    archivo = open(ruta_archivo, encoding='utf-8').read()
    archivo = re.sub(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n[^\nA-Za-ko-z]+\n', "", archivo)
    lista_subs = re.findall(r'\d+\s+\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n([^\n]*)\n', archivo)
    subs_rep = [x for x, y in collections.Counter(lista_subs).items() if y > 1]
    for sub in subs_rep:
        pattern = r'\n\d+\n+\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n%s\n' % re.escape(sub)
        archivo = re.sub(pattern, "", archivo)
    archivo = re.sub(r'\n{2,}', "\n", archivo)
    f = open(ruta_archivo, "w", encoding='utf-8')
    f.write(archivo)



    f.close()


if __name__ == '__main__':
    ruta = f'{ruta_carpeta}/*.srt'
    for archivo in buscar_archivos(ruta):
        leer(archivo)
