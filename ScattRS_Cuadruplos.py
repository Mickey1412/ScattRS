#Lenguaje ScattRS
#Clase para los cuadruplos
#25/03/2019

class Cuadruplos():
	"""docstring for Cuadruplos"""
	def __init__(self, numero_cuadruplo, operador, operando_Izq, operando_Der, resultado):
		self.numero_cuadruplo = numero_cuadruplo
		self.operador = operador
		self.operando_Der = operando_Der
		self.operando_Izq = operando_Izq
		self.resultado = resultado

#metodo que actualiza el resultado de un cuadruplo, asignandole el numero del cuadruplo al que va a saltar
	def cuadruplo_saltos(self, num_saltos):
		self.resultado = num_saltos


#representacion del cuadruplo en forma de string
	def __str__(self):
		return (str(self.numero_cuadruplo) + " | " + str(self.operador) + ", " + str(self.operando_Izq) + ", " + str(self.operando_Der) + ", " + str(self.resultado))