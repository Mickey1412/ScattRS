#Lenguaje ScattRS
#Clase de Cubo Semantico v1.0
#25/03/2019

#Esta clase define los resultados de las operaciones entre distintos tipos de datos, asignando cuales son y no son aceptadas
class CuboSemantico():

	def __init__(self):

		self.Cubo = {
			"int" : {
				"int" : {
					"+" : "int",
                	"-" : "int",
                	"*" : "int",
                	"/" : "int",
                	"=" : "int",
                	"==" : "bool",
                	"!=" : "bool",
                	">" : "bool",
                	"<" : "bool",
                	">=" : "bool",
                	"<=" : "bool",
                	"Y" : "error",
                	"O" : "error"
				},
				"float" : {
					"+" : "float",
                	"-" : "float",
                	"*" : "float",
                	"/" : "float",
                	"=" : "int", #verificar si cambiar a error
                	"==" : "bool",
                	"!=" : "bool",
                	">" : "bool",
                	"<" : "bool",
                	">=" : "bool",
                	"<=" : "bool",
                	"Y" : "error",
                	"O" : "error"
				},
				"string": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                },
                "char": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                },
				"bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    "Y" : "error",
                    "O" : "error"
                }
			},

			"float" : {
				"float" : {
					"+" : "float",
                    "-" : "float",
                    "*" : "float",
                    "/" : "float",
                    "=" : "float",
                    "==" : "bool",
                    "!=" : "bool",
                    ">" : "bool",
                    "<" : "bool",
                    ">=" : "bool",
                    "<=" : "bool",
                    "Y" : "error",
                    "O" : "error"
				},
				"int" : {
                    "+" : "float",
                    "-" : "float",
                    "*" : "float",
                    "/" : "float",
                    "=" : "float",
                    "==" : "bool",
                    "!=" : "bool",
                    ">" : "bool",
                    "<" : "bool",
                    ">=" : "bool",
                    "<=" : "bool",
                    "Y" : "error",
                    "O" : "error"
                },
                "string": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                },
                "char": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                },
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    "Y" : "error",
                    "O" : "error"
                }
			},

			"string" : {
				"string": {
                    "+": "string",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "string",
                    "==": "bool",
                    "!=": "bool",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                },
                "int": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                },
                "float": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                },
                "char": {
                    "+": "string",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                },
                "bool": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                }
			},

			"char" : {
				"char" : {
					"+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "char",
                    "==": "bool",
                    "!=": "bool",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
				},
				"int": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                },
                "float": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                },
                "string": {
                    "+": "string",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                },
                "bool": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                }
			},

			"bool" : {
				"bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "bool",
                    "==" : "bool",
                    "!=" : "bool",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    "Y" : "bool",
                    "O" : "bool"
                },
                "int" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    "Y" : "error",
                    "O" : "error"
                },
                "float" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    "Y" : "error",
                    "O" : "error"
                },
                "string": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                },
                "char": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "!=": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "Y": "error",
                    "O": "error"
                }
			}

		}

	#llama al tipo de las variables que se tienen el los cuadruplos
	def get_tipo_semantica(self, tipo_Izq, tipo_Der, operador):
		return self.Cubo[tipo_Izq][tipo_Der][operador]
