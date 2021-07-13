import os
from glob import glob

logs_path = r'C:\WPOSS\POWER'
folder_list = os.listdir(logs_path)
len_folder_list = len(folder_list)
wrong_format_files_list = []


def search_files(path):
    listar_archivos = glob(path)
    return listar_archivos


def read(file_path, index):
    try:
        open(file_path, encoding='utf-8').read()
    except UnicodeDecodeError:
        wrong_format_files_list.append(file_path)
    print(f'{int(index * 100 / len_folder_list)}% Completado')


if __name__ == '__main__':
    for index in range(len_folder_list):
        path = f'{logs_path}/{folder_list[index]}/*.txt'
        for file in search_files(path):
            read(file, index)
    print('100% Completado')
    print(*wrong_format_files_list, sep='\n')
