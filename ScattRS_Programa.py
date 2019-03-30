#Lenguaje ScattRS
#Clase de Programa v1.0
#25/03/2019
from .ScattRS_DirectorioFunc import DireccionFunc

#El proposito de esta clase es para crear las pilas necesarias para la creacion de cuadruplos, y para conectar las clases del directorio de funciones y cubo semantico al resto del programa
class Programa():
	"""docstring for Programa"""
	def __init__(self, scope_global = "", scope_actual = ""):
		self.scope_global = scope_global
		self.scope_actual = scope_actual
		self.directorio_func = DireccionFunc()
		self.pila_operando = []
		self.pila_operador = []
		self.pila_tipo = []
		self.pila_saltos = []
		self.lista_cuadruplo = []