#Lenguaje ScattRS 
#Maquina Virtual
#17/04/2019

import sys
import statistics
from scipy import stats
from sklearn.metrics import r2_score
from scipy.stats import binom
from scipy.stats import bernoulli
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()

# import array
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
        # print("pasa por aqui")
        # print(llamada_funcion, "\n")
        # variable = llamada_funcion['funcion']['num_de_variables_locales']['int']
        # try:
        #     variable = llamada_funcion['funcion']['num_de_variables_locales']['int']
        # except:
        #     print("no jala esto")
        # print("cantidad de enteros: ", variable)
        for n in range(llamada_funcion['funcion']['num_de_variables_locales']['int']):
            llamada_funcion['memoria'].pedir_direccion_local('int')
            # try:
            #     llamada_funcion['memoria'].pedir_direccion_local('int')
            # except:
            #     print("no jalo local int")
        for n in range(llamada_funcion['funcion']['num_de_variables_locales']['float']):
            llamada_funcion['memoria'].pedir_direccion_local('float')
            # try:
            #     llamada_funcion['memoria'].pedir_direccion_local('float')
            # except:
            #     print("no jalo local float")
        for n in range(llamada_funcion['funcion']['num_de_variables_locales']['string']):
            llamada_funcion['memoria'].pedir_direccion_local('string')
            # try:
            #     llamada_funcion['memoria'].pedir_direccion_local('string')
            # except:
            #     print("no jalo local string")
        for n in range(llamada_funcion['funcion']['num_de_variables_locales']['bool']):
            llamada_funcion['memoria'].pedir_direccion_local('bool')
            # try:
            #     llamada_funcion['memoria'].pedir_direccion_local('bool')
            # except:
            #     print("no jalo local bool")

    def direccion_temporal(self, llamada_funcion):
        for n in range(llamada_funcion['funcion']['num_de_variables_temporales']['int']):
            llamada_funcion['memoria'].pedir_direccion_temporal('int')
        for n in range(llamada_funcion['funcion']['num_de_variables_temporales']['float']):
            llamada_funcion['memoria'].pedir_direccion_temporal('float')
        for n in range(llamada_funcion['funcion']['num_de_variables_temporales']['string']):
            llamada_funcion['memoria'].pedir_direccion_temporal('string')
        for n in range(llamada_funcion['funcion']['num_de_variables_temporales']['bool']):
            llamada_funcion['memoria'].pedir_direccion_temporal('bool')

    def get_tipo_input(self, valor):
        try:
            return type(literal_eval)(valor)
        except (ValueError, SyntaxError):
            return str

    def set_tipo_input(self, valor):
        if valor.isdigit():
            if "." in valor:
                return float(valor)
            else:
                return int(valor)
        elif valor == "verdadero" or valor == "falso":
            return bool(valor)
        else:
            return str(valor)

    def get_tipo_string(self, valor):
        if valor.isdigit():
            if "." in valor:
                return 'float'
            else:
                return 'int'
        elif valor == "verdadero" or valor == "falso":
            return 'bool'
        else:
            return 'string'

    #Funcion principal de la maquina virtual que ejecuta las instrucciones de codigo intermedio
    def ejecutar_maquina(self):
        print("\n================================")
        print("Esta es la Maquina virtual")
        #Alacena la informacion de la funcion cuando se hace una llamada a funcion
        funcion_llamada = {}
        memoria_actual = self.memoria
        #Numero que representa la posicion del parametro de una funcion
        parametro_posicion = 0
        #pila que guarda numero de cuadruplo al que se debe regresar al terminar una llamada a funcion
        pila_num_instruccion_rtr = []
        #lista de memoria locar
        pila_seg_local = []
        #lista de memoria temporal
        pila_seg_temp = []
        # variable que contiene el scope
        scope = ''
        nombre_variable1 = ''
        nombre_variable2 = ''
        
        
        

        #Ciclo que lee todos las instruciones hasta que se hayan leido todos los cuadruplos
        while self.num_instrucciones_actual < self.num_instrucciones:
            instruccion_actual = self.instrucciones[self.num_instrucciones_actual]
            
            # print("imprimir cuadruplo?")
            # cuad = input()
            # if(cuad == 'y'):
            #     print(instruccion_actual)

            #insertar el operador, operandos (direcciones de memoria) y resultado de los cuadruplos en variables para ejecucion
            accion = instruccion_actual.operador
            dir_operando_izq = instruccion_actual.operando_Izq
            dir_operando_der = instruccion_actual.operando_Der
            dir_resultado = instruccion_actual.resultado
            # print("Accion: ", accion)
            

            #Obtiene los valores adentro de las variables especiales para otorgar las direcciones que tiene el valor de la casilla del arreglo
            #Cuando operandos izquierdos son una casilla de arreglo
            dir_izq = isinstance(dir_operando_izq, dict)
            dir_der = isinstance(dir_operando_der, dict)
            dir_resul = isinstance(dir_resultado, dict)
            
            if (dir_izq == True and dir_der == False and dir_resul == False):
                dir_operando_izq = memoria_actual.get_valor(dir_operando_izq['direccion_indice'])
                # print("dir_operando_izq: ", dir_operando_izq)
            #Cuando operandos derechos son una casilla de arreglo
            elif (dir_izq == False and dir_der == True and dir_resul == False):
                dir_operando_der = memoria_actual.get_valor(dir_operando_der['direccion_indice'])
                # print("dir_operando_der: ", dir_operando_der)
            #Cuando operandos de resultado son una casilla de arreglo
            elif (dir_izq == False and dir_der == False and dir_resul == True):
                dir_resultado = memoria_actual.get_valor(dir_resultado['direccion_indice'])
                # print("dir_resultado: ", dir_resultado)
            elif (dir_izq == True and dir_der == True and dir_resul == False):
                dir_operando_izq = memoria_actual.get_valor(dir_operando_izq['direccion_indice'])
                dir_operando_der = memoria_actual.get_valor(dir_operando_der['direccion_indice'])
            elif (dir_izq == False and dir_der == True and dir_resul == True):
                dir_resultado = memoria_actual.get_valor(dir_resultado['direccion_indice'])
                dir_operando_der = memoria_actual.get_valor(dir_operando_der['direccion_indice'])
            elif (dir_izq == True and dir_der == False and dir_resul == True):
                dir_resultado = memoria_actual.get_valor(dir_resultado['direccion_indice'])
                dir_operando_izq = memoria_actual.get_valor(dir_operando_izq['direccion_indice'])
            elif (dir_izq == True and dir_der == True and dir_resul == True):
                dir_resultado = memoria_actual.get_valor(dir_resultado['direccion_indice'])
                dir_operando_der = memoria_actual.get_valor(dir_operando_der['direccion_indice'])
                dir_operando_izq = memoria_actual.get_valor(dir_operando_izq['direccion_indice'])

            #Lista de condiciones para la ejeecucin de cada  instruccion de acuerdo a sutipo de accion en el cuadruplos 

            ##################################### Ejecucion de cuadruplos basicos #######################################
            if accion == '+':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                # print("operando_izq", operando_izq)
                operando_der = memoria_actual.get_valor(dir_operando_der)
                # print("operando_der", operando_der)
                #Se realiza la operacion de la suma con los valores de los operandos
                resultado = operando_izq + operando_der
                # print("resultado", resultado)
                # print("dir_resultado: ", dir_resultado)
                #Se guarda el resultado y se continua al siguiente cuadruplo
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == '-':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                operando_der = memoria_actual.get_valor(dir_operando_der)
                #Se realiza la operacion de la resta con los valores de los operandos
                resultado = operando_izq - operando_der
                #Se guarda el resultado y se continua al siguiente cuadruplo
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == '*':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                operando_der = memoria_actual.get_valor(dir_operando_der)
                #Se realiza la operacion de la multiplicacion con los valores de los operandos
                resultado = operando_izq * operando_der
                #Se guarda el resultado y se continua al siguiente cuadruplo
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == '/':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                operando_der = memoria_actual.get_valor(dir_operando_der)
                #Validacion para cnacelar divisiones entre 0
                if operando_der == 0:
                    print("ERROR: division entre 0 no es valida")
                    sys.exit()
                else:
                    #Se realiza la division exacta dependiendo los tipos de valores que se dividen ya sea int o float
                    if isinstance(operando_izq, float) or isinstance(operando_der, float):
                        resultado = operando_izq/operando_der
                    else:
                        resultado = int(operando_izq/operando_der)
        
                #Se guarda el resultado y se continua al siguiente cuadruplo
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == '<':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                operando_der = memoria_actual.get_valor(dir_operando_der)
                #Se realiza la operacion logica MENOR QUE con los valores de los operandos
                resultado = operando_izq < operando_der
                #Se guarda el resultado y se continua al siguiente cuadruplo
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == '>':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                operando_der = memoria_actual.get_valor(dir_operando_der)
                #Se realiza la operacion logica MAYOR QUE con los valores de los operandos
                resultado = operando_izq > operando_der
                #Se guarda el resultado y se continua al siguiente cuadruplo
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == '<=':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                operando_der = memoria_actual.get_valor(dir_operando_der)
                #Se realiza la operacion logica MENOR IGUAL con los valores de los operandos
                resultado = operando_izq <= operando_der
                #Se guarda el resultado y se continua al siguiente cuadruplo
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == '>=':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                operando_der = memoria_actual.get_valor(dir_operando_der)
                #Se realiza la operacion logica MAYOR IGUAL con los valores de los operandos
                resultado = operando_izq >= operando_der
                #Se guarda el resultado y se continua al siguiente cuadruplo
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == '=':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                # print("\nAsignacion")
                # print("operand_izq: ", operando_izq)
                #Le asignas el valor del operando izquierdo al resultado
                resultado = operando_izq
                # print("resultado: ", resultado)
                # print("direccion resultado: ", dir_resultado)
                #Se guarda el resultado y se continua al siguiente cuadruplo
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == '==':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                operando_der = memoria_actual.get_valor(dir_operando_der)
                #Se realiza la operacion logica IGUAL IGUAL con los valores de los operandos
                resultado = operando_izq == operando_der
                #Se guarda el resultado y se continua al siguiente cuadruplo
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == '!=':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                operando_der = memoria_actual.get_valor(dir_operando_der)
                #Se realiza la operacion logica NO IGUAL con los valores de los operandos
                resultado = operando_izq != operando_der
                #Se guarda el resultado y se continua al siguiente cuadruplo
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == 'Y':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                operando_der = memoria_actual.get_valor(dir_operando_der)
                #Se realiza la operacion logica AND con los valores de los operandos
                resultado = operando_izq and operando_der
                #Se guarda el resultado y se continua al siguiente cuadruplo
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == 'O':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                operando_der = memoria_actual.get_valor(dir_operando_der)
                #Se realiza la operacion logica OR con los valores de los operandos
                resultado = operando_izq or operando_der
                #Se guarda el resultado y se continua al siguiente cuadruplo
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == 'PRINT':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                #Se imprime en consola un string del operando izquierdo del cuadruplo
                print(str(operando_izq))
                #Se guarda el resultado y se continua al siguiente cuadruplo
                self.num_instrucciones_actual += 1
            elif accion == 'READ':
                variable = dir_resultado
                variable_tipo = dir_operando_izq
                valor_input = input()
                tipo_valor_input = self.get_tipo_string(valor_input)
                # try:
                #     tipo_valor_input = self.get_tipo_string(valor_input)
                # except:
                #     print("Marco error en el get tipo string")
                
                # print("tipo_valor_input: ", tipo_valor_input)
                valor_input = self.set_tipo_input(valor_input)
                
                if tipo_valor_input == variable_tipo:
                    memoria_actual.editar_valor(variable, valor_input)
                else:
                    print("El input que se escribio no es correcto para el tipo de variable")
                    sys.exit()
                self.num_instrucciones_actual += 1
            ################################# Cuadruplos para condiciones/ciclos y saltos ####################################
            elif accion == 'GOTO':
                #Apunta al cuadruplo a saltar y se lo asigna al cuadruplo actual para ejecutar
                self.num_instrucciones_actual = dir_resultado - 1
            elif accion == 'GOTOF':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                #Verificar 
                if not operando_izq:
                    self.num_instrucciones_actual = dir_resultado - 1
                else:
                    self.num_instrucciones_actual += 1
            ################################ Cuadruplos de funciones ########################################################
            elif accion == 'ENDPROC':
                #Se elimina la informacion local de la funcion cuando se termina su ejecucion y regresa el segmento local y temporal a la funcion que llamo la ejecucion
                funcion_llamada.clear()
                memoria_actual.memoria_local = pila_seg_local.pop()
                memoria_actual.memoria_temporal = pila_seg_temp.pop()
                #regresa la instruccion a la funcion que llamo la ejecucion
                self.num_instrucciones_actual = pila_num_instruccion_rtr.pop() + 1
            elif accion == 'ERA':
                #Se busca la funcion en el directorio de funciones y crea su segmento de memoria para sus variables locales y temporales
                funcion_llamada['funcion'] = self.directorio_func.get_f(dir_operando_izq)
                # print("funcion llamada: ", funcion_llamada)
                funcion_llamada['memoria'] = Memoria()
                parametro_posicion = 0
                #Se corre la funcion para pedir espacio para direcciones locales y temporales de la funcion que se llama
                try:
                    self.direccion_local(funcion_llamada)
                except:
                    print("No jalo direccion local")
                
                try:
                    self.direccion_temporal(funcion_llamada)
                except:
                    print("No jalo direccion temporal")
                # self.direccion_temporal(funcion_llamada)
                self.num_instrucciones_actual += 1
            elif accion == 'PARAM':
                #Se obtiene el valor de los parametros y la direccion de memoria deonde se van a guardar
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                # print("operando_izq: ", operando_izq)
                # print("parametros de la funcion: ",funcion_llamada['funcion']['parametros']['direccion'][parametro_posicion])
                # print("parametro posicion: ",parametro_posicion)
                # print("lista direcciones: ", funcion_llamada['funcion']['parametros']['direccion'] )
                
                # parametro_posicion = len(funcion_llamada['funcion']['parametros']['direccion']) - 1
                # print("parametro posicion: ", parametro_posicion)
                try:
                    dir_parametro = funcion_llamada['funcion']['parametros']['direccion'][parametro_posicion]
                except:
                    print("no jala el dir parametro")
                # print("dir_parametro", dir_parametro)
                # try:
                #     parametro_posicion = len(dir_parametro)
                # except:
                #     print("no jalo el parametro posicion")
                # print("parametro posicion: ", parametro_posicion)
                # print("dir_parametro: ", dir_parametro)
                parametro_posicion += 1
                #Se guardan los valores de los parametros en el segmento de memoria de la funcion que se llama
                try:
                    funcion_llamada['memoria'].editar_valor(dir_parametro, operando_izq)
                except:
                    print("no esta jalando la memoria")
                #Pasa al cuadruplo siguiente
                self.num_instrucciones_actual += 1
            elif accion == 'GOSUB':
                #se guarda el numero de la instruccion a la que se va a regresar despues de la ejecucucion de la funcion llamada
                pila_num_instruccion_rtr.append(self.num_instrucciones_actual)
                #guarda los segmentos de memoria locales y temporales de la funcion que hizo la llamada
                pila_seg_local.append(memoria_actual.memoria_local)
                pila_seg_temp.append(memoria_actual.memoria_temporal)
                #Cambiar el segmento de memoria actual por el de la funcion a la que se esta llamando
                memoria_actual.memoria_local = funcion_llamada['memoria'].memoria_local
                memoria_actual.memoria_temporal = funcion_llamada['memoria'].memoria_temporal
                #se cambia el cuadruplo actual por el de la funcion que se va a ejecutar
                self.num_instrucciones_actual = dir_resultado - 1
            elif accion == 'RETURN':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                resultado = operando_izq
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            ################################## Cuadruplos de Arreglos ##########################################
            elif accion == 'VER_ARR':
                #Toma el indice del arreglo que se llama y verifica que se encuentre dentro de los limites superiores e inferiores del arreglo
                indice = memoria_actual.get_valor(dir_operando_izq)
                # print("indice: ", indice)
                limite_inf = dir_operando_der
                # print("dir_operando_der: ", dir_operando_der)
                limite_sup = dir_resultado
                # try:
                #     limite_sup = dir_resultado
                # except:
                #     print("no jala el limite_sup")
                # print("limite_sup: ", limite_sup , "\n")
                
                if indice < limite_sup and indice >= limite_inf:
                    self.num_instrucciones_actual += 1
                else:
                    print("El indice esta fuera de los limites del arreglo")
                    sys.exit()
            ################################## Funciones Predefinidas ##########################################
            elif accion == 'SPECNAME':
                scope = dir_operando_izq
                nombre_variable1 = dir_operando_der
                nombre_variable2 = dir_resultado
                # print("scope: ",scope)
                # print("nombre variable 1: ", nombre_variable1)
                # print("nombre variable 2: ", nombre_variable2)
                self.num_instrucciones_actual += 1
            elif accion == 'SUM':
                # print("operando izq: ", dir_operando_izq)
                variable_objeto = self.directorio_func.get_funcion_variable(scope, nombre_variable1)
                # print("variable: ", variable_objeto)
                variable_lim_sup = variable_objeto['limite_sup']
                # print("variable_lim_sup: ", variable_lim_sup)
                resultado = 0
                
                for i in range(variable_lim_sup):
                    direccion = dir_operando_izq + i
                    # print("direccion: ", direccion)  
                    try:
                        
                        resultado += memoria_actual.get_valor(direccion)
                    except:
                        print("pasa i = ", i)
                # print("resultado: ", resultado)
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == 'PROM':
                # print("operando izq: ", dir_operando_izq)
                variable_objeto = self.directorio_func.get_funcion_variable(scope, nombre_variable1)
                # print("variable: ", variable_objeto)
                variable_lim_sup = variable_objeto['limite_sup']
                # print("variable_lim_sup: ", variable_lim_sup)
                resultado = 0
                
                for i in range(variable_lim_sup):
                    direccion = dir_operando_izq + i
                    # print("direccion: ", direccion)  
                    try:
                        
                        resultado += memoria_actual.get_valor(direccion)
                    except:
                        print("pasa i = ", i)
                # print("resultado: ", resultado)
                resultado /= variable_lim_sup
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == 'MEDIAN':
                variable_objeto = self.directorio_func.get_funcion_variable(scope, nombre_variable1)
                variable_lim_sup = variable_objeto['limite_sup']
                arreglo = []
                # print("entro a mediana")
                
                for i in range(variable_lim_sup):
                    direccion = dir_operando_izq + i
                    # print("direccion: ", direccion)
                    # variable = memoria_actual.get_valor(direccion)
                    # print("valor del arreglo: ", variable)
                    try:
                        arreglo.append(memoria_actual.get_valor(direccion))
                    except:
                        print("pasa i = ", i)
                # print("arreglo: ", arreglo)
                # print("resultado: ", resultado)
                resultado = statistics.median(arreglo)
                # if(variable_lim_sup % 2 != 0):
                #     # print("valor de index: ", int(variable_lim_sup / 2))
                #     resultado = arreglo[int(variable_lim_sup / 2)]
                #     # print("resultado: ", resultado)
                # else:
                #     # Falta calcular la media cuando se tiene una lista par
                #     resultado = arreglo[int(variable_lim_sup / 2)]
                #     print("\nFalta calcular la media cuando se tiene una lista par")
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == 'MODA':
                variable_objeto = self.directorio_func.get_funcion_variable(scope, nombre_variable1)
                variable_lim_sup = variable_objeto['limite_sup']
                arreglo = []
                
                for i in range(variable_lim_sup):
                    direccion = dir_operando_izq + i
                    try:
                        arreglo.append(memoria_actual.get_valor(direccion))
                    except:
                        print("pasa i = ", i)
                # print(arreglo)
                try: 
                    resultado = statistics.mode(arreglo)
                except:
                    print("moda no jalo")
                
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == 'DESV':
                variable_objeto = self.directorio_func.get_funcion_variable(scope, nombre_variable1)
                variable_lim_sup = variable_objeto['limite_sup']
                arreglo = []
                
                for i in range(variable_lim_sup):
                    direccion = dir_operando_izq + i
                    try:
                        arreglo.append(memoria_actual.get_valor(direccion))
                    except:
                        print("pasa i = ", i)
                # print(arreglo)
                resultado = statistics.stdev(arreglo)
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == 'VARIANCE':
                variable_objeto = self.directorio_func.get_funcion_variable(scope, nombre_variable1)
                variable_lim_sup = variable_objeto['limite_sup']
                arreglo = []
                
                for i in range(variable_lim_sup):
                    direccion = dir_operando_izq + i
                    try:
                        arreglo.append(memoria_actual.get_valor(direccion))
                    except:
                        print("pasa i = ", i)
                # print(arreglo)
                resultado = statistics.variance(arreglo)
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == 'RSQUARE':
                
                variable_objeto1 = self.directorio_func.get_funcion_variable(scope, nombre_variable1)
                variable_lim_sup1 = variable_objeto1['limite_sup']
                # print("variable objeto 1: ", variable_objeto1)
                variable_objeto2 = self.directorio_func.get_funcion_variable(scope, nombre_variable2)
                variable_lim_sup2 = variable_objeto2['limite_sup']
                # print("variable objeto 2: ", variable_objeto2)
                arreglo1 = []
                arreglo2 = []
                
                for i in range(variable_lim_sup1):
                    direccion = dir_operando_izq + i
                    try:
                        arreglo1.append(memoria_actual.get_valor(direccion))
                    except:
                        print("pasa i = ", i)
                # print(arreglo1)
                
                for i in range(variable_lim_sup2):
                    direccion = dir_operando_der + i
                    try:
                        arreglo2.append(memoria_actual.get_valor(direccion))
                    except:
                        print("pasa i = ", i)
                # print(arreglo2)
                resultado = r2_score(arreglo1, arreglo2)
                memoria_actual.editar_valor(dir_resultado, resultado)
                self.num_instrucciones_actual += 1
            elif accion == 'SCATT':
                variable_objeto1 = self.directorio_func.get_funcion_variable(scope, nombre_variable1)
                variable_lim_sup1 = variable_objeto1['limite_sup']
                # print("variable objeto 1: ", variable_objeto1)
                variable_objeto2 = self.directorio_func.get_funcion_variable(scope, nombre_variable2)
                variable_lim_sup2 = variable_objeto2['limite_sup']
                # print("variable objeto 2: ", variable_objeto2)
                arreglo1 = []
                arreglo2 = []
                
                for i in range(variable_lim_sup1):
                    direccion = dir_operando_izq + i
                    try:
                        arreglo1.append(memoria_actual.get_valor(direccion))
                    except:
                        print("pasa i = ", i)
                # print(arreglo1)
                
                for i in range(variable_lim_sup2):
                    direccion = dir_operando_der + i
                    try:
                        arreglo2.append(memoria_actual.get_valor(direccion))
                    except:
                        print("pasa i = ", i)
                # print(arreglo2)
                print("Por favor inserte el limite de los ejes de la grafica")
                index = input()
                indice = int(index)
                print("Desea imprimir la pendiente en la grafica? [y/n]")
                res_pend = input()
                if res_pend == 'y':
                    print("inserta el valor del gradiente 'm' de la formula y = mx + b")
                    valor_m = input()
                    int_valor_m = int(valor_m)
                    print("inserta el valor del intercept 'b' de la formula y = mx + b")
                    valor_b = input()
                    int_valor_b = int(valor_b)
                    valor_x = np.linspace(-5, indice, 100)
                    valor_y = int_valor_m * valor_x + int_valor_b
                    plt.plot(valor_x, valor_y, '-r', label = 'pendiente')
                    plt.legend(loc='upper left')
                plt.plot(arreglo1, arreglo2, 'ro')
                plt.axis([0, indice, 0, indice])
                plt.grid()
                plt.show()
                self.num_instrucciones_actual += 1
            elif accion == 'BAR':
                variable_objeto1 = self.directorio_func.get_funcion_variable(scope, nombre_variable1)
                variable_lim_sup1 = variable_objeto1['limite_sup']
                # print("variable objeto 1: ", variable_objeto1)
                variable_objeto2 = self.directorio_func.get_funcion_variable(scope, nombre_variable2)
                variable_lim_sup2 = variable_objeto2['limite_sup']
                # print("variable objeto 2: ", variable_objeto2)
                arreglo1 = []
                arreglo2 = []
                
                for i in range(variable_lim_sup1):
                    direccion = dir_operando_izq + i
                    try:
                        arreglo1.append(memoria_actual.get_valor(direccion))
                    except:
                        print("pasa i = ", i)
                # print(arreglo1)
                
                for i in range(variable_lim_sup2):
                    direccion = dir_operando_der + i
                    try:
                        arreglo2.append(memoria_actual.get_valor(direccion))
                    except:
                        print("pasa i = ", i)
                # print(arreglo2)
                y_pos = np.arange(len(arreglo2))
                print("Desea que la grafica de barras sea horizontal? [y/n]")
                horizon = input()
                if horizon == 'y':
                    plt.barh(y_pos, arreglo1, align='center', alpha=0.5)
                    plt.xticks(y_pos, arreglo2)
                    plt.show()
                    self.num_instrucciones_actual += 1
                else:
                    plt.bar(y_pos, arreglo1, align='center', alpha=0.5)
                    plt.xticks(y_pos, arreglo2)
                    plt.show()
                    self.num_instrucciones_actual += 1
            elif accion == 'BINOM':
                valor_n = memoria_actual.get_valor(dir_operando_der)
                probabilidad = memoria_actual.get_valor(dir_operando_izq)
                x = stats.binom(valor_n, probabilidad)
                print("generacio de 10 numeros")
                try:
                    valor_pmf = x.pmf(3)
                except:
                    print("no jalo el binomial")
                binomial = binom.rvs(valor_n, probabilidad, size=10)
                print("10 samples al azar de la distribucion binomial")
                print(binomial)
                memoria_actual.editar_valor(dir_resultado, valor_pmf)
                self.num_instrucciones_actual += 1
            elif accion == 'BERNOU':
                valor_n = memoria_actual.get_valor(dir_operando_der)
                probabilidad = memoria_actual.get_valor(dir_operando_izq)
                datos = bernoulli.rvs(probabilidad, size=10)
                memoria_actual.editar_valor(dir_resultado, datos)
                self.num_instrucciones_actual += 1
            elif accion == 'PEND':
                variable_objeto1 = self.directorio_func.get_funcion_variable(scope, nombre_variable1)
                variable_lim_sup1 = variable_objeto1['limite_sup']
                # print("variable objeto 1: ", variable_objeto1)
                variable_objeto2 = self.directorio_func.get_funcion_variable(scope, nombre_variable2)
                variable_lim_sup2 = variable_objeto2['limite_sup']
                # print("variable objeto 2: ", variable_objeto2)
                arreglo1 = []
                arreglo2 = []
                
                for i in range(variable_lim_sup1):
                    direccion = dir_operando_izq + i
                    try:
                        arreglo1.append(memoria_actual.get_valor(direccion))
                    except:
                        print("pasa i = ", i)
                # print(arreglo1)
                
                for i in range(variable_lim_sup2):
                    direccion = dir_operando_der + i
                    try:
                        arreglo2.append(memoria_actual.get_valor(direccion))
                    except:
                        print("pasa i = ", i)
                # print(arreglo2)
                valor_m = (arreglo1[variable_lim_sup1 - 1] - arreglo1[0]) / (arreglo2[variable_lim_sup2 - 1] - arreglo2[0])
                valor_b = arreglo1[0] - (valor_m * arreglo2[0])
                string_m = str(valor_m)
                string_b = str(valor_b)
                print("Pendiente:")
                print("y = " + string_m + "x + " + string_b)
                #print("valor m:")
                #print(valor_m)
                #print("valor b:")
                #print(valor_b)
                self.num_instrucciones_actual += 1

                
