#Lenguaje ScattRS
#Clase Memoria
#14/04/2019

from scattRS_SegmentosMemoria import Segmentos
import sys
#Clase que representa la memoria completa del compilador para guardar valores constantes, temporales y globales del programa
class Memoria():
    #Clase constructora
    #La memoria se divide en segmentos de memoria tomados de la clase "Segmento_Memoria" 
    def __init__(self,):
        self.memoria_global = Segmentos('Global', 5000, 4000)
        self.memoria_temporal = Segmentos('Local', 10000, 4000)
        self.memoria_local = Segmentos('Constantes', 15000, 4000)
        self.memoria_constantes = Segmentos('Temporal', 20000, 4000)

    def pedir_direccion_global(self, tipo_valor, valor = None):
        return self.memoria_global.pedir_direccion(tipo_valor, valor)

    def pedir_direccion_local(self, tipo_valor, valor = None):
        return self.memoria_local.pedir_direccion(tipo_valor, valor)

    def pedir_direccion_constante(self, tipo_valor, valor = None):
        return self.memoria_constantes.pedir_direccion(tipo_valor, valor)

    def pedir_direccion_temporal(self, tipo_valor, valor = None):
        return self.memoria_temporal.pedir_direccion(tipo_valor, valor)

    def pedir_direccion_global_arreglo(self, tipo_valor, total_direcciones, valor = None):
        return self.memoria_global.pedir_direccion_arreglo(tipo_valor, total_direcciones, valor)

    def pedir_direccion_local_arreglo(self, tipo_valor, total_direcciones, valor = None):
        return self.memoria_local.pedir_direccion_arreglo(tipo_valor, total_direcciones, valor)

    def determinar_tipo_memoria(self, direccion):
        if (direccion >= self.memoria_global.direccion_inicio and direccion <= self.memoria_global.direccion_final):
            return 'global'
        elif (direccion >= self.memoria_local.direccion_inicio and direccion <= self.memoria_local.direccion_final):
            return 'local'
        elif (direccion >= self.memoria_constantes.direccion_inicio and direccion <= self.memoria_constantes.direccion_final):
            return 'constantes'
        elif (direccion >= self.memoria_temporal.direccion_inicio and direccion <= self.memoria_temporal.direccion_final):
            return 'temporal'
        else:
            print("direccion de memoria invalida")
            sys.exit()
    
    def get_valor(self, direccion):
        tipo_memoria = self.determinar_tipo_memoria(direccion)
        if tipo_memoria == 'global':
            self.memoria_global.get_valor(direccion)
        elif tipo_memoria == 'local':
            self.memoria_local.get_valor(direccion)
        elif tipo_memoria == 'constante':
            self.memoria_constantes.get_valor(direccion)
        elif tipo_memoria == 'temporal':
            self.memoria_temporal.get_valor(direccion)

    def editar_valor(self, direccion, valor):
        tipo_memoria = self.determinar_tipo_memoria(direccion)
        if tipo_memoria == 'global':
            self.memoria_global.editar_valor(direccion, valor)
        elif tipo_memoria == 'local':
            self.memoria_local.editar_valor(direccion, valor)
        elif tipo_memoria == 'constante':
            self.memoria_constantes.editar_valor(direccion, valor)
        elif tipo_memoria == 'temporal':
            self.memoria_temporal.editar_valor(direccion, valor)

    def ver_valor_constante_existe(self, tipo_valor, valor):
        return self.memoria_constantes.ver_valor_existe(tipo_valor, valor)

    def reset_temporal(self):
        self.memoria_local.borron_y_cuenta_nueva()
        self.memoria_temporal.borron_y_cuenta_nueva()

    
