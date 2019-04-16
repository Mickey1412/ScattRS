#Lenguaje ScattRS 
#Clase de Tipos de Segmento de Memoria
#15/04/2019

import json
import sys
#Clase re representa los segmentos de memoria que dividen la memoria pricipal
class TipoSegmentoMem():
    #Clase constructora
    def __init__(self, nombre_segmento, direccion_inicio, direccion_final):
        self.nombre = nombre_segmento
        self.direccion_inicio = direccion_inicio
        self.direccion_final = direccion_final
        self.direccion_actual = direccion_inicio
        self.segmento = {}

    #Representacion de la clase en forma de String
    #def __str__(self):
     #   return ("Segmento : " + self.nombre + "\n" +
      #      "   Direccion Inicial: " + str(self.direccion_inicio) + "\n" + 
       #     "   Direccion Final: " + str(self.direccion_final) + "\n" + 
        #    "   Direccion Actual: " + str(self.direccion_actual) + "\n" + 
         #   "   Direcciones: " + json.dumps(self.segmento, indent=4))

    #otorga una direccion de memoria para una variable o una constante del lenguaje
    def pedir_direccion(self, valor):
        if self.espacio_Disponible():
            direccion = self.direccion_actual
            self.segmento[direccion] = valor
            self.direccion_actual += 1
            return direccion
        else:
            print("No hay espacio de memoria disponible")
    
    #Procedimiento que determina si el espacio de memoria no esta lleno
    def espacio_Disponible(self, total_direcciones = 0):
        if self.direccion_actual + total_direcciones <= self.direccion_final:
            return True
        else:
            return False
    
    #Proceso que valida la direccion de memoria
    def validar_direccion(self, direccion):
        if direccion in self.segmento:
            return True
        else:
            return False

    #Proceso que obtiene el valor de una direccion de me
    def get_valor(self, direccion):
        if self.validar_direccion(direccion):
            return self.segmento[direccion]
        else:
            print("La direccion de memoria requerida no es valida")
            return None

    #Proceso que verifica si el el valor ya existe en el segmento de memoria
    def ver_valor_existe(self, valor_existe):
        for direccion, valor in self.segmento.items():
            if valor == valor_existe:
                return direccion
        #No se regresa nada si el valor no existe
        return None

    #proceso que edita un valor de una direccion de memoria
    def editar_valor(self, direccion, valor):
        if self.validar_direccion(direccion):
            self.segmento[direccion] = valor
        else: 
            print("el valor que se intenta cambiar en la direccion de memoria no es valido")
            sys.exit()

    #Proceso que borra todas las direcciones del segmente y comienza desde el principio
    def borron_y_cuenta_nueva(self):
        self.segmento.clear()
        self.direccion_actual = self.direccion_inicio

    #Proceso que separa direcciones de memoria sequenciales para un arreglo
    def pedir_direccion_arreglo(self, total_direcciones, valor):
        if self.espacio_Disponible(total_direcciones):
            direccion_base = self.direccion_actual

            #ciclo que pide una direccion de memoria para cada elemento del arreglo
            for iA in range(total_direcciones):
                self.segmento[self.direccion_actual] = valor
                self.direccion_actual += 1
            
            return direccion_base
        else:
            print("No hay espacio de memoria disponible")



