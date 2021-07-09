from os import strerror

try:
	fo = open('newtext.txt', 'wt') #un nuevo archivo (newtext.txt) es creado
	for i in range(10):
		s = "línea #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))