try:
    stream = open("C:\Users\User\Desktop\file.txt", "rt")
    # aqui se procesa el archivo
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)