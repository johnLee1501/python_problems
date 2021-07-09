def exterior(par):
	loc = par
	def interior():
		return loc
	return interior

var = 1
fun = exterior(var)
print(fun())