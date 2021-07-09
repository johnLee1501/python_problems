import errno
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # el procesamiento va aquí
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("El archivo no existe.")
    elif exc.errno == errno.EMFILE:
        print("Has abierto demasiados archivos.")
    else:
        print("El número de error es:", exc.errno)