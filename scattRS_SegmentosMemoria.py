#Lenguaje ScattRS 
#Clase Segmentos de Memoria
#15/04/2019

from scattRS_TiposSegmentos import TipoSegmentoMem
import sys
#Clase que divide la memoria en segmentos, basados en tipos de valor (int, float, char o bool) y manda llamar a la clase "Tipos_Segmento" para los procedimientos de asignacion de memoria
class Segmentos():
    def __init__(self, nombre_memoria, direccion_inicio, total_direcciones):
        self.nombre = nombre_memoria
        #Division del segmento por los tipos de datos
        self.size_tipo_seg = int(total_direcciones / 4)
        self.direccion_inicio = direccion_inicio
        #Direccion final del segmento de memoria (-1 para no intercalar con la primera direccions del siguiente segmento)
        self.direccion_final = direccion_inicio + total_direcciones - 1
    #Constructures de la direccion inicial y final de cada tipo de valor
    #Calculo de desplazamiento para tipo de datos visto en clase
        #int
        self.int_direccion_inicio = direccion_inicio
        self.int_direccion_final = direccion_inicio + self.size_tipo_seg - 1
        #float
        self.float_direccion_inicio = direccion_inicio + self.size_tipo_seg
        self.float_direccion_final = direccion_inicio + self.size_tipo_seg * 2 - 1
        #char
        self.char_direccion_inicio = direccion_inicio + self.size_tipo_seg * 2
        self.char_direccion_final = direccion_inicio + self.size_tipo_seg * 3 - 1
        #bool
        self.bool_direccion_inicio = direccion_inicio + self.size_tipo_seg * 3
        self.bool_direccion_final = direccion_inicio + self.size_tipo_seg * 4 - 1
    #Construccion de los tipos de segmento
        self.int_segmento = TipoSegmentoMem('int', self.int_direccion_inicio, self.int_direccion_final)
        self.float_segmento = TipoSegmentoMem('float', self.float_direccion_inicio, self.float_direccion_final)
        self.char_segmento = TipoSegmentoMem('char', self.char_direccion_inicio, self.char_direccion_final)
        self.bool_segmento = TipoSegmentoMem('bool', self.bool_direccion_inicio, self.bool_direccion_final)

    #Procesi que pide la direccion de memoria dependiendo del tipo de valor
    def pedir_direccion(self, tipo_segmento, valor = None):
        #Si la direccion esta vacia, su valor es 0
        if tipo_segmento == 'int':
            if valor is None:
                valor = 0
            return self.int_segmento.pedir_direccion(valor)
        elif tipo_segmento == 'float':
            if valor is None:
                valor = 0.0
            return self.float_segmento.pedir_direccion(valor)
        elif tipo_segmento == 'char':
            if valor is None:
                valor = ''
            return self.char_segmento.pedir_direccion(valor)
        elif tipo_segmento == 'bool':
            if valor is None:
                valor = False
            return self.bool_segmento.pedir_direccion(valor)

    #Proceso que pide el tipo para mandar llamar el proceso de pedir direcciones de memoria para arreglos
    def pedir_direccion_arreglo(self, tipo_segmento, total_direcciones, valor = None):
        if tipo_segmento == 'int':
            if valor is None:
                valor = 0
            return self.int_segmento.pedir_direccion_arreglo(total_direcciones, valor)
        elif tipo_segmento == 'float':
            if valor is None:
                valor = 0.0
            return self.float_segmento.pedir_direccion_arreglo(total_direcciones, valor)
        elif tipo_segmento == 'char':
            if valor is None:
                valor = ''
            return self.char_segmento.pedir_direccion_arreglo(total_direcciones, valor)
        elif tipo_segmento == 'bool':
            if valor is None:
                valor = False
            return self.bool_segmento.pedir_direccion_arreglo(total_direcciones, valor)

    #Proceso que determina el tipo de valor para llamar al proceso que obtiene el tipo de acuerdo a la direccion de memoria
    def get_valor(self, direccion):
        tipo_segmento = self.determinar_tipo_segmento(direccion)
        if tipo_segmento == 'int':
            return self.int_segmento.get_valor(direccion)
        elif tipo_segmento == 'float':
            return self.float_segmento.get_valor(direccion)
        elif tipo_segmento == 'char':
            return self.char_segmento.get_valor(direccion)
        elif tipo_segmento == 'bool':
            return self.bool_segmento.get_valor(direccion)

    #Proceso que manda llamara la clase tipo segmento para editar valores de acuerdo a su direccion de memoria
    def editar_valor(self, direccion, valor):
        tipo_segmento = self.determinar_tipo_segmento(direccion)
        if tipo_segmento == 'int':
            return self.int_segmento.editar_valor(direccion, valor)
        elif tipo_segmento == 'float':
            return self.float_segmento.editar_valor(direccion, valor)
        elif tipo_segmento == 'char':
            return self.char_segmento.editar_valor(direccion, valor)
        elif tipo_segmento == 'bool':
            return self.bool_segmento.editar_valor(direccion, valor)

    def ver_valor_existe(self, tipo_segmento, valor):
        if tipo_segmento == 'int':
            return self.int_segmento.ver_valor_existe(valor)
        elif tipo_segmento == 'float':
            return self.float_segmento.ver_valor_existe(valor)
        elif tipo_segmento == 'char':
            return self.char_segmento.ver_valor_existe(valor)
        elif tipo_segmento == 'bool':
            return self.bool_segmento.ver_valor_existe(valor)

    def borron_y_cuenta_nueva(self):
        self.int_segmento.borron_y_cuenta_nueva()
        self.float_segmento.borron_y_cuenta_nueva()
        self.char_segmento.borron_y_cuenta_nueva()
        self.bool_segmento.borron_y_cuenta_nueva()

    
    #proceso que regresa el tipo de un segmento, de acuerdo a su direccion de memoria
    def determinar_tipo_segmento(self, direccion):
        if (direccion >= self.int_direccion_inicio and direccion <= self.int_direccion_final):
            return 'int'
        elif (direccion >= self.float_direccion_inicio and direccion <= self.float_direccion_final):
            return 'float'
        elif (direccion >= self.char_direccion_inicio and direccion <= self.char_direccion_final):
            return 'char'
        elif (direccion >= self.bool_direccion_inicio and direccion <= self.bool_direccion_final):
            return 'bool'
        else:
            print("Direccion invalida")
            sys.exit()

    


    
