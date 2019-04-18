#Lenguaje ScattRS 
#Maquina Virtual
#17/04/2019

import sys
from ast import literal_eval
from scattRS_Memoria import Memoria
from scattRS_DirectorioFunc import DireccionFunc

class Maquina_Virtual():

    def __init__(self, memoria, directorio_func, instrucciones):
        self.memoria = memoria
        self.directorio_func = directorio_func
        self.instrucciones = instrucciones
        self.num_instrucciones = len(self.instrucciones)
        self.num_instrucciones_actual = 0

    def direccion_local(self, llamada_funcion):
        for n in range(llamada_funcion['funcion']['num_variables_local']['int']):
            llamada_funcion['memoria'].direccion_local('int')
        for n in range(llamada_funcion['funcion']['num_variables_local']['float']):
            llamada_funcion['memoria'].direccion_local('float')
        for n in range(llamada_funcion['funcion']['num_variables_local']['char']):
            llamada_funcion['memoria'].direccion_local('char')
        for n in range(llamada_funcion['funcion']['num_variables_local']['bool']):
            llamada_funcion['memoria'].direccion_local('bool')

    def direccion_temporal(self, llamada_funcion):
        for n in range(llamada_funcion['funcion']['num_variables_local']['int']):
            llamada_funcion['memoria'].direccion_temporal('int')
        for n in range(llamada_funcion['funcion']['num_variables_local']['float']):
            llamada_funcion['memoria'].direccion_temporal('float')
        for n in range(llamada_funcion['funcion']['num_variables_local']['char']):
            llamada_funcion['memoria'].direccion_temporal('char')
        for n in range(llamada_funcion['funcion']['num_variables_local']['bool']):
            llamada_funcion['memoria'].direccion_temporal('bool')

    def get_tipo_input(self, valor):
        try:
            return type(literal_eval)(valor)
        except (ValueError, SyntaxError):
            return str

    def set_tipo_input(self, valor):
        if self.get_tipo_input(valor) is int:
            return int(valor)
        elif self.get_tipo_input(valor) is float:
            return float(valor)
        elif self.get_tipo_input(valor) is str:
            return str(valor)
        elif self.get_tipo_input(valor) is bool:
            return bool(valor)

    def get_tipo_string(self, valor):
        if self.get_tipo_input(valor) is int:
            return 'int'
        elif self.get_tipo_input(valor) is float:
            return 'float'
        elif self.get_tipo_input(valor) is str:
            return 'char'
        elif self.get_tipo_input(valor) is bool:
            return 'bool'

    def ejecutar_maquina(self):
        print("Esta es la Maquina virtual")
    