#Lenguaje ScattRS
#Clase de directorio de funciones v2.00
#25/03/2019

import json
#el json le da formato al los diccionarios al imprimirlos
from scattRS_TablaVariables import Tabla_Variables

#clase que contiene la lista de funciones y procedimientos del lenguaje ScattRS
class DireccionFunc():
	
    #Constructor
    def __init__(self):
        self.lista_func = {}
		
    def agregar_func(self, func_nombre, func_tipo, func_param = [], func_para_dir = []):
        self.lista_func[func_nombre] = {
        'nombre' : func_nombre,
        'tipo_retorno' : func_tipo,
        'direccion_retorno' : -1,
        'numero_cuadruplo' : -1,
        'parametros' : {
        'tipo' : func_param,
        'direccion' : func_para_dir,
        },
        'variables' : Tabla_Variables(),
        'num_de_variables_locales' : {
        'int' : 0,
        'float' : 0,
        'char' : 0,
        'string' : 0,
        'bool' : 0
        },
        'num_de_variables_temporales' : {
        'int' : 0,
        'float' : 0,
        'char' : 0,
        'string' : 0,
        'bool' : 0
        }
    }
	
    #metodo que busca una funcion del directorio
    def busqueda_f(self, func_nombre):
        return func_nombre in self.lista_func.keys()

    #metodo que obtiene una funcion del directorio
    def get_f(self, func_nombre):
        if self.busqueda_f(func_nombre):
            return self.lista_func[func_nombre]
        else:
            print("la funcion con este nombre no existe")
            return None

    def agregar_parametro(self, func_nombre, lista_tipo, lista_direcciones):
        funcion = self.get_f(func_nombre)
        if funcion is not None:
            funcion['parametros']['tipo'] = lista_tipo
            funcion['parametros']['dirreccion'] = lista_direcciones
        else:
            print("La funcion que se intenta insertar no existe")
	
    def agregar_variable(self, func_nombre, variable_tipo, variable_nombre, variable_direccion=0):
        funcion = self.get_f(func_nombre)
        if funcion is not None:
            if funcion['variables'].busqueda_v(variable_nombre):
                print("existe otra variable con este nombre dentro de la funcion")
            else:
                #agrega variables a la tabla de variables y se incrementa el numero de variables locales dentro de la funcion
                funcion['variables'].agregar_v(variable_tipo, variable_nombre, variable_direccion)
                funcion['num_variables_locales'][variable_tipo] += 1
        else:
            print("La funcion donde se esta agregando la variable no existe")

    def agregar_variable_dimensionada(self, func_nombre, variable):
        funcion = self.get_f(func_nombre)
        if funcion is not None:
            if funcion['variables'].busqueda_v(variable['nombre']):
                print("existe otra variable con este nombre dentro de la funcion")
            else:
                # agrega variables dimensionada a la tabla de variables y se incrementa el numero de variables locales dentro de la funcion
                funcion['variables'].agregar_vArreglo(variable)
                for i in range(variable['limite_superior']):
                    funcion['num_de_variables_locales'][variable['tipo']] += 1
        else:
            print("La funcion donde se esta agregando la variable no existe")

    #checa que la variable exista en el scope de la funcion
    def verificar_variable_existe(self, func_nombre, variable_nombre):
        funcion = self.get_f(func_nombre)
        if funcion is not None:
            if funcion['variables'].busqueda_v(variable_nombre):
                return True
            else:
                return False
        else:
            print("La variable " + variable_nombre + " ya fue declarada")

    #agrega una variable temporal a la funcion
    def agregar_temporal(self, func_nombre, temporal_tipo):
        funcion = self.get_f(func_nombre)
        if funcion is not None:
            funcion['num_de_variables_temporalesm'][temporal_tipo] += 1
        else:
            print("La funcion donde se esta agregando la variable temporal no existe")

    #busca por una variable dentro de una funcion
    def get_funcion_variable(self, func_nombre, variable_nombre):
        funcion = self.get_f(func_nombre)
        if funcion is not None:
            variable = funcion['variables'].get_f(variable_nombre)
            if variable is not None:
                return variable
            else:
                return None
        else:
            print("La funcion que contiene la variable que buscas no existe")

    #busca por el tipo de la funcion
    def get_funcion_tipo(self, func_nombre):
        funcion = self.get_f(func_nombre)
        if funcion is not None:
            func_tipo = funcion['return_type']
            return func_tipo
        else:
            print("Esta funcion no existe")

    #regresa los parametros de la funcion
    def get_funcion_parametros(self, func_nombre):
        funcion = self.get_f(func_nombre)
        if funcion is not None:
            return funcion['parametros']
        else:
            print("La funcion que contiene el parametro que buscas no existe")

    #establece la direccion de regreso de la funcion
    def set_funcion_direccion(self, func_nombre, num_direccion):
        funcion = self.get_f(func_nombre)
        if funcion is not None:
            funcion['direccion_retorno'] = num_direccion
        else:
            print("La funcion que se desea agregar una direccion no existe")

    #establece el cuadruplo donde inicia el procedimiento
    def set_numero_cuadruplo(self, func_nombre, numero_cuadruplo):
    	funcion = self.get_f(func_nombre)
    	if funcion is not None:
    		funcion['numero_cuadruplo'] = numero_cuadruplo
    	else:
    		print("La funcion a la que deseas hacer set del cuadruplo no existe")
    	
    #llama el numero del cuadruplo de una funcion
    def get_numero_cuadruplo(self, func_nombre):
    	funcion = self.get_f(func_nombre)
    	if funcion is not None:
    		return funcion['numero_cuadruplo']
    	else:
    		print("el cuadruplo de la funcion que tratas de llamar no existe")
    	
    #imprime la lista de funciones del directorio con sus propiedades
    def print_directorio(self):
        for funcion, propiedades in self.lista_func.items():
            print("funcion: " + str(funcion))

            #ciclo que hace que se imprima la tabla de variables solo si el valor es una instancia de la clase
            for prop, valor in propiedades.items():
                if isinstance(valor, Tabla_Variables):
                    print("  " + str(prop) + " : " +
                    json.dumps(valor.list_variables, indent=4))
                elif isinstance(valor, dict):
                    print("  " + str(prop) + " : " + json.dumps(valor, indent=4))
                else:
                    print("  " + str(prop) + " : " + str(valor))