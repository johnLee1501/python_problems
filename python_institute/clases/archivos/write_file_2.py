from os import strerror

try:
	fo = open('newtext.txt', 'wt')
	for i in range(10):
		fo.write("line #" + str(i+1) + "\n")
	fo.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))