import numpy as np
import os


def buscar_archivos(ruta):
    archivos_texto = []
    archivos = os.listdir(ruta)
    for archivo in archivos:
        if archivo[-4:] == '.txt':
            archivos_texto.append(archivo)
    return archivos_texto


def leer(ruta_archivo):
    datos = np.genfromtxt(ruta_archivo, delimiter='\n', names=True, dtype=None, encoding='utf-8')
    deposito01 = 0
    deposito02 = 0
    retiro01 = 0
    retiro02 = 0
    giros_emision = 0
    giros_cobro = 0
    giros01 = 0
    consultas01 = 0
    consultas02 = 0
    excepcion = 0

    for dato in datos:
        if 'URL https://www.conex.agentesbcp.com/channel/ageb/v1/deposit/confirm-voucher-print' in str(dato):
            deposito01 += 1
        elif 'msgError : transEName DEPÓSITO' in str(dato):
            deposito02 += 1
        elif 'URL https://www.conex.agentesbcp.com/channel/ageb/v1/withdrawal/confirm-voucher-print' in str(dato):
            retiro01 += 1
        elif 'msgError : transEName RETIRO' in str(dato):
            retiro02 += 1
        elif 'URL https://www.conex.agentesbcp.com/channel/ageb/v1/bank-draft-issue/confirm-voucher-print' in str(dato):
            giros_emision += 1
        elif 'URL https://www.conex.agentesbcp.com/channel/ageb/v1/bank-draft-withdrawal/confirm-voucher-print' in str(
                dato):
            giros_cobro += 1
        elif 'msgError : transEName GIROS' in str(dato):
            giros01 += 1
        elif 'URL https://www.conex.agentesbcp.com/channel/ageb/v1/product-overview/confirm-voucher-print' in str(dato):
            consultas01 += 1
        elif 'msgError : transEName CONSULTAS' in str(dato):
            consultas02 += 1
        elif 'getErr 146' in str(dato):
            excepcion += 1
    print(f'\nArchivo: {ruta_archivo}\n')
    return print(
        f'Depositos Exitosos = {deposito01}\nDepositos Fallidos = {deposito02}\nRetiros Exitosos = {retiro01}\nRetiros Fallidos = {retiro02}\nGiros Emision = {giros_emision}\nGiros Cobro = {giros_cobro}\nGiros Fallidos = {giros01}\nConsultas Exitosas = {consultas01}\nConsultas Fallidas = {consultas02}\nError 146 = {excepcion}\n')


ruta_carpetas = r'C:/WPOSS/LOGS_BCP'
nombres_carpetas = os.listdir(ruta_carpetas)

for carpeta in nombres_carpetas:
    ruta = ruta_carpetas + '/' + carpeta
    for archivo in buscar_archivos(ruta):
        ruta_archivo = ruta + '/' + archivo
        leer(ruta_archivo)
    ruta = ''
