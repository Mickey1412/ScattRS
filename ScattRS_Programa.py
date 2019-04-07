#Lenguaje ScattRS
#Clase de Programa v1.0
#25/03/2019
from scattRS_DirectorioFunc import DireccionFunc

#El proposito de esta clase es para crear las pilas necesarias para la creacion de cuadruplos, y para conectar las clases del directorio de funciones y cubo semantico al resto del programa
class Programa():
	"""docstring for Programa"""
	def __init__(self, scope_global = "", scope_actual = ""):
		self.scope_global = scope_global
		self.scope_actual = scope_actual
		self.directorio_func = DireccionFunc()
		self.parametros_temporales_nombres = []
		self.parametros_temporales_tipos = []
		self.pila_operando = []
		self.pila_operador = []
		self.pila_tipo = []
		self.pila_saltos = []
		self.lista_cuadruplo = []

	# def print_programa(self):
    # 		for i in range (len(self.variables_temporales)):
	# 		print("variable: ", self.variables_temporales[i])
   	
	# def get_variable_tempo(self):
	# 	return len(self.variables_temporales)
 
	def print_temporales_parametros_nombres(self):
		for i in range(len(self.parametros_temporales_nombres)):
			print("parametro: ", self.parametros_temporales_nombres[i])
   
	def print_temporales_parametros_tipos(self):
		for i in range(len(self.parametros_temporales_nombres)):
			print("tipo: ", self.parametros_temporales_tipos[i])