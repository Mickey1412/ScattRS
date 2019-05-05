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

        #Ciclo que lee todos las instruciones hasta que se hayan leido todos los cuadruplos
        while self.num_instrucciones_actual < self.num_instrucciones:
            instruccion_actual = self.instrucciones[self.num_instrucciones_actual]

            #insertar el operador, operandos (direcciones de memoria) y resultado de los cuadruplos en variables para ejecucion
            accion = instruccion_actual.operador
            dir_operando_izq = instruccion_actual.operando_Izq
            dir_operando_der = instruccion_actual.operando_Der
            dir_resultado = instruccion_actual.resultado
            # print("Accion: ", accion)

            #Obtiene los valores adentro de las variables especiales para otorgar las direcciones que tiene el valor de la casilla del arreglo
            #Cuando operandos izquierdos son una casilla de arreglo
            if isinstance(dir_operando_izq, dict):
                dir_operando_izq = memoria_actual.get_valor(dir_operando_izq['direccion_indice'])
                print("dir_operando_izq: ", dir_operando_izq)
            #Cuando operandos derechos son una casilla de arreglo
            elif isinstance(dir_operando_der, dict):
                dir_operando_der = memoria_actual.get_valor(dir_operando_der['direccion_indice'])
                print("dir_operando_der: ", dir_operando_der)
            #Cuando operandos de resultado son una casilla de arreglo
            elif isinstance(dir_resultado, dict):
                dir_resultado = memoria_actual.get_valor(dir_resultado['direccion_indice'])
                # print("dir_resultado: ", dir_resultado)

            #Lista de condiciones para la ejeecucin de cada  instruccion de acuerdo a sutipo de accion en el cuadruplos 

            ##################################### Ejecucion de cuadruplos basicos #######################################
            if accion == '+':
                operando_izq = memoria_actual.get_valor(dir_operando_izq)
                print("operando_izq", operando_izq)
                operando_der = memoria_actual.get_valor(dir_operando_der)
                print("operando_der", operando_der)
                #Se realiza la operacion de la suma con los valores de los operandos
                resultado = operando_izq + operando_der
                print("resultado", resultado)
                print("dir_resultado: ", dir_resultado)
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
                print("\nAsignacion")
                print("operand_izq: ", operando_izq)
                #Le asignas el valor del operando izquierdo al resultado
                resultado = operando_izq
                print("resultado: ", resultado)
                print("direccion resultado: ", dir_resultado)
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
                print("indice: ", indice)
                limite_inf = dir_operando_der
                print("dir_operando_der: ", dir_operando_der)
                limite_sup = dir_resultado
                # try:
                #     limite_sup = dir_resultado
                # except:
                #     print("no jala el limite_sup")
                print("limite_sup: ", limite_sup , "\n")
                
                if indice < limite_sup and indice >= limite_inf:
                    self.num_instrucciones_actual += 1
                else:
                    print("El indice esta fuera de los limites del arreglo")
                    sys.exit()

