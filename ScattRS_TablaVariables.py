#Lenguaje ScattRS
#Clase de tabla de variables v1.0
#18/03/2019

class Tabla_Variables(object):
	"""Clase para la creacion de la tabla de variables """
	
	#Constructor de la Clase
	def __init__(self):
		self.list_Variables = {}

	#Metodo para agregar variables a la lista
	def agregar_v(self, nombre_v, tipo_v, direccion_memoria_v = 0):
		self.List_Variables[nombre_v] = {
		'nombre' : nombre_v,
		'tipo' : tipo_v,
		'direccion_memoria' : direccion_memoria_v
		}

	#Metodo para agregar a la lista variables dimensionadas
	def agregar_vArreglo(self, variable):
		self.List_Variables[variable['nombre']] = variable

	#metodo que busca una variable especifica en la lista
	def busqueda_v(self, nombre_v):
		return nombre_v in self.List_Variables.keys()

	#metodo que obtiene una variable de la lista
	def get_v(self, nombre_v):
		if self.busqueda_v(nombre_v):
			return self.List_Variables[nombre_v]
		else:
			return None

	def _str__(self):
		return self.List_Variables