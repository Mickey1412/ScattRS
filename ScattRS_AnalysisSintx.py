# coding=utf-8
import ply.yacc as yacc
from scattRS_AnalysisLex import tokens
from scattRS_Programa import Programa
from scattRS_Cuadruplos import Cuadruplos
import sys

#variable que toma la clase programa para llamar los procedimientos del directorio de funciones y cuadruplos
var_program = Programa()

# Gramaticas del compilador
def p_programa(p):
	'''
	programa : PROGRAM ID punto_gotoMain punto_creardf progra_A1 progra_A2 MAIN PAREN_I PAREN_D punto_main bloque
	'''
	print("Sintaxis Correcto :D \n")

def p_progra_A1(p):
	'''
	progra_A1 : var progra_A1 
		| empty
	'''
	p[0] = p[1]

def p_progra_A2(p):
	'''
	progra_A2 : funcion progra_A2 
		| empty
	'''
	p[0] = p[1]

def p_funcion(p):
	'''
	funcion : FUNC func_tipo ID PAREN_I func_param PAREN_D punto_addf bloque punto_endProc
	'''
	# print("SI SE PUDO funcion")
	# print(p[3])

def p_func_tipo(p):
	'''
	func_tipo : VOID 
		| tipo
	'''
	p[0] = p[1]

def p_func_param(p):
	'''
	func_param : param 
		| param COMA func_param 
		| empty
	'''
 
def p_param(p):
	'''
	param : tipo ID
	'''
	# print("SI SE param")
#  Agarra los nombres y tipos de los parametros y los inserta en el arreglo de parametros temporales
	nombre_parametro = p[2]
	tipo_parametro = p[1]
	# print(nombre_parametro, tipo_parametro)
	var_program.parametros_temporales_nombres.insert(0,nombre_parametro)
	var_program.parametros_temporales_tipos.insert(0,tipo_parametro)

def p_var(p):
	'''
	var : PARAMS tipo ID var_A1 punto_addv SEMICOLON 
	| PARAMS tipo ID arr punto_addvarr SEMICOLON
	'''
	#print("SI SE var")

def p_var_A1(p):
	'''
	var_A1 : COMA ID var_A1
		| empty 
	'''
	#print("p[-1]", p[-1])
	nombre = p[-1]
	#print("p[-2]", p[-2])
	var_program.variables_temporales.insert(0,nombre)
	if p[-2] != ',':
		#print("p[-2]",p[-2])
		tipo = p[-2]
		var_program.variables_temporales_tipo = tipo
	#print("p[0]",p[1])
	#nombre = p[1]
	#var_program.variables_temporales.insert(0,nombre)

### VERSION PASADA DE LA GRAMATICA (11/04/19)
#def p_var(p):
	#'''
	#var : PARAMS tipo var_A1 SEMICOLON 
	#'''
	# print("SI SE var")

#def p_var_A1(p):
	#'''
	#var_A1 : ID arr 
		#| ID arr COMA var_A1 
		#| ID punto_addv
		#| ID punto_addv COMA var_A1
	#'''
	#var_program.variables_temporales.insert(0,)
	#if p[-1] != ',':
		#print("p[-1]",p[-1])
		#tipo = p[-1]
		#var_program.variables_temporales_tipo = tipo
	#print("p[0]",p[1])
	#nombre = p[1]
	#var_program.variables_temporales.insert(0,nombre)
	
	
# def p_var_A1(p):
# 	'''
# 	var_A1 : ID arr var_array
# 		| ID arr var_array COMA var_A1 
# 		| ID 
# 		| ID COMA var_A1
# 	'''

# def p_var_array(p):
#     '''
# 	var_array : ASSIGN CURLY_I var_array_A1 CURLY_D
# 		| empty
# 	'''

# def p_var_array_A1(p):
#     '''
# 	var_array_A1 : expression
# 		| expression COMA var_array_A1
# '''

def p_assign(p):
	'''
	assign : ID punto_pilaOvar assign_A1 ASSIGN punto_pOper assign_A2 SEMICOLON punto_cuadAssign
	'''

def p_assign_A1(p):
	'''
	assign_A1 : BRACKET_I exp BRACKET_D 
		| empty 
	'''
	
def p_assign_A2(p):
    '''
	assign_A2 : expression
		| estadistica
	'''

def p_args(p):
	'''
	args : expression punto_params
		| expression punto_params COMA args 
		| empty
	'''
	# print("SI SE args")

def p_factor(p):
	'''
	factor : PAREN_I punto_fondoIni expression PAREN_D punto_fondoFin
		| fact_A1 var_cte
	'''
	# print("SI SE factor")

def p_fact_A1(p):
	'''
	fact_A1 : OP_SUMA punto_pOper
		| OP_RESTA punto_pOper
		| empty
	'''

def p_stmt(p):
	'''
	stmt : func_call 
		| assign 
		| cond 
		| printf 
		| return 
		| estadistica_graph 
		| readf
		| while
	'''
	# print("SI SE stmt")

def p_tipo(p):
	'''
	tipo : INT 
		| FLOAT 
		| BOOL 
		| CHAR 
	'''
	p[0] = p[1]
	# print("SI SE tipo")

def p_var_cte(p):
	'''
	var_cte : ID punto_pilaOvar var_cte_A1 
		| INT_VALOR punto_pilaOint 
		| FLOAT_VALOR punto_pilaOfloat
		| TRUE punto_pilaObool
		| FALSE punto_pilaObool
		| CHAR_VALOR punto_pilaOchar
		| proc_call
	'''
	# print("exp: " + str(p[1]))
	# print("SI SE var_cte")

def p_var_cte_A1(p):
	'''
	var_cte_A1 : BRACKET_I exp BRACKET_D 
		| empty
	'''


#def p_var_cte_A1(p):
#	'''
#	var_cte_A1 : BRACKET_I exp BRACKET_D 
#		| PAREN_I punto_fondoIni punto_era var_cte_A2 PAREN_D punto_fondoFin punto_gosub
#		| empty
#	'''

def p_var_cte_A2(p):
	'''
	var_cte_A2 : exp COMA var_cte_A2 
		| exp 
		| empty
	'''

def p_proc_call(p):
	'''
	proc_call : ID PAREN_I punto_fondoIni punto_era args PAREN_D punto_fondoFin punto_gosub punto_funcCallR
	'''

def p_exp(p):
	'''
	exp : term punto_termino exp_A1 
	'''
	# print("SI SE exp")

def p_exp_A1(p):
	'''
	exp_A1 : OP_SUMA punto_pOper exp
		| OP_RESTA punto_pOper exp
		| empty
	'''

def p_arr(p):
	'''
	arr : BRACKET_I INT_VALOR punto_pilaOint BRACKET_D punto_identificarDim
	'''
	print("cosa: ", p[2])
	print("pasa por aqui")

def p_term(p):
	'''
	term : factor punto_factor term_A1 
	'''
	# print("SI SE term")

def p_term_A1(p):
	'''
	term_A1 : OP_MULT punto_pOper term
		| OP_DIV punto_pOper term
		| empty
	'''

def p_expression(p):
	'''
	expression : exp expression_A1 exp punto_relacion
		| exp
	'''
	# print("SI SE expression")

def p_expression_A1(p):
	'''
	expression_A1 : MAYOR punto_pOper
		| MENOR punto_pOper
		| MAYOR_EQ punto_pOper
		| MENOR_EQ punto_pOper
		| EQUAL punto_pOper
		| NOT_EQ punto_pOper
		| empty
	'''

def p_exp_cond(p):
	''' 
	exp_cond : expression exp_cond_A1
	'''
	# print("Si se exp_cond")

def p_exp_cond_A1(p):
	'''
	exp_cond_A1 : OR punto_pOper expression punto_logico
		| AND punto_pOper expression punto_logico
		| empty
	'''

def p_printf(p):
	'''
	printf : PRINT PAREN_I print_A1 PAREN_D punto_print SEMICOLON
	'''
	# print("Si se pudo print")

def p_print_A1(p):
	'''
	print_A1 : expression 
		| STRING_VALOR punto_pilaOString
	'''

def p_cond(p):
	'''
	cond : IF PAREN_I exp_cond PAREN_D punto_crearGotoF bloque cond_A1 punto_fillGotoF
	'''
	# print("Si se pudo cond")

def p_cond_A1(p):
	'''
	cond_A1 : ELSE punto_else bloque 
		| empty
	'''

def p_func_call(p):
	'''
	func_call : ID PAREN_I punto_fondoIni punto_era args PAREN_D punto_fondoFin punto_gosub void_check SEMICOLON
	'''
	# print("Si se pudo func_call")

def p_bloque(p):
	'''
	bloque : CURLY_I bloque_A1 CURLY_D
	'''
	# print("Si se pudo bloque")

def p_bloque_A1(p):
	'''
	bloque_A1 : var stmt bloque_A1 
		| var bloque_A1 
		| stmt bloque_A1 
		| empty
	'''

def p_estadistica(p):
	'''
	estadistica : PROM estadistica_A1 
		| MODA estadistica_A1 punto_cuadModa
		| MEDIAN estadistica_A1 punto_cuadMedian
		| SUM estadistica_A1 punto_cuadSum
		| DESVIA estadistica_A2 punto_cuadDesv
		| PEND estadistica_A2 punto_cuadPend
		| VARIANCE estadistica_A1 punto_cuadVarian
		| R_SQUARE estadistica_A2 punto_cuadRsquar
		| BINOMIAL estadistica_A3 
		| BERNOULLI estadistica_A2 punto_cuadBernou
	'''
	# print("Si se pudo estadistica")
	# print(p[1])

def p_estadisitica_graph(p):
    '''
	estadistica_graph : GRAPH_BAR estadistica_A2 SEMICOLON
		| GRAPH_SCATTER estadistica_A4 SEMICOLON
	'''

def p_estadistica_A1(p):
	'''
	estadistica_A1 : PAREN_I ID punto_pilaOvar PAREN_D 
	'''
	# print(p[1],p[2],p[3],p[4])

def p_estadistica_A2(p):
	'''
	estadistica_A2 : PAREN_I ID punto_pilaOvar COMA ID punto_pilaOvar PAREN_D 
	'''
	print("pasa por estadisticaA2")

def p_estadistica_A3(p):
	'''
	estadistica_A3 : PAREN_I ID punto_pilaOvar COMA ID punto_pilaOvar COMA ID punto_pilaOvar PAREN_D 
	'''
	print("pasa por estadisticaA3")
	print(var_program.pila_operando)

def p_estadistica_A4(p):
	'''
	estadistica_A4 : estadistica_A2 punto_cuadScatt
		| estadistica_A3 punto_cuadScattPend
	'''

def p_return(p):
	'''
	return : RETURN exp SEMICOLON punto_returnTrue
	'''
	# print("Si se pudo return")

def p_readf(p):
	'''
	readf : READ PAREN_I expression PAREN_D punto_cuadRead SEMICOLON 
	'''
	# print("Si se pudo read")

def p_while(p):
    '''
	while : WHILE punto_guardarWhile PAREN_I exp_cond PAREN_D punto_crearGotoF bloque punto_regresarWhile
	'''

def p_empty(p):
	'empty :'
	pass

## PUNTOS NEURALGICOS ##
# P.N. que agrega funcion principal (el programa)
def p_punto_creardf(p):
	'''punto_creardf : '''
	var_program.scope_global = p[-2]
	var_program.scope_actual = p[-2]
	
	#agrega la funcion al directorio 
	var_program.directorio_func.agregar_func(var_program.scope_global, 'void')
	# agregar las variables globales como los parametros en agregar funcion N.P.
	

# P.N. que agrega una funcion al directorio de funciones
# agregar el cuadruplo de funciones y return
def p_punto_addf(p):
	'''punto_addf : '''
	var_program.scope_actual = p[-4]
	tipofuncion = p[-5]
	direcciones_variables = []
	
 	#Agrega la funcion al directorio 
	var_program.directorio_func.agregar_func(var_program.scope_actual, tipofuncion)

	#Generar el cuadruplo de inicio de la funcion 
	var_program.directorio_func.set_numero_cuadruplo(var_program.scope_actual, var_program.numero_cuadruplo)

	if tipofuncion != 'void':
		#establece direccion de retorno de la funcion
		direccion_funcion = var_program.memoria.pedir_direccion_global(tipofuncion)
		var_program.directorio_func.set_funcion_direccion(var_program.scope_actual, direccion_funcion)
	
 	# Agregar las variables en la tabla de variables
	variables = zip(var_program.parametros_temporales_nombres, var_program.parametros_temporales_tipos)
	for variable_nombre, variable_tipo in variables: 
		direccion = var_program.memoria.pedir_direccion_local(variable_tipo)
		# print("direccion: ",direccion)
		direcciones_variables.append(direccion)
		var_program.directorio_func.agregar_variable(var_program.scope_actual, variable_tipo, variable_nombre, direccion)
	var_program.directorio_func.agregar_parametro(var_program.scope_actual, list(var_program.parametros_temporales_tipos), list(direcciones_variables))
 
	del var_program.parametros_temporales_nombres[:]
	del var_program.parametros_temporales_tipos[:]
 	# falta agregar la memoria 
	# var_program.directorio_func.agregar_parametro(var_program.scope_actual, list(var_program.variables_temporales_tipos), lista de direcciones)

#P.N. que agrega la funcion MAIN al directorio de funciones
def p_punto_main(p):
	'''punto_main : '''
	var_program.scope_actual = p[-3]
	# print(var_program.scope_actual)

	#agrega la funcion al directorio 
	var_program.directorio_func.agregar_func(var_program.scope_actual, 'void')

#P.N. que agrega varable a la tabla de variables de la funcion actual
def p_punto_addv(p):
	'''punto_addv : '''
	# variable_tipo = p[-2]
	# print("variable_tipo: ", variable_tipo)
	#variable_nombre = p[-1]
	# variable_direccion = '0'
	#print("pasa por aqui")
	#print("variables temporales nombre: ",var_program.variables_temporales)
	#print("variable tipo: ",var_program.variables_temporales_tipo)
	#func_nombre = var_program.scope_actual
	for variable in var_program.variables_temporales:
		variable_declarada = var_program.directorio_func.verificar_variable_existe(var_program.scope_actual, variable)
		#print(variable_declarada)
		#print(variable)
		if not variable_declarada:
			#pedir direccion de memoria dependiendo del scope
			if var_program.scope_actual == var_program.scope_global:
				variable_direccion = var_program.memoria.pedir_direccion_global(var_program.variables_temporales_tipo)
			else: 
				variable_direccion = var_program.memoria.pedir_direccion_local(var_program.variables_temporales_tipo)
			# print("tipo de variable: " + str(var_program.variables_temporales_tipo) + " nombre de variables: " + str(variable) + " nombre de funcion: " + str(func_nombre))
			var_program.directorio_func.agregar_variable(var_program.scope_actual, var_program.variables_temporales_tipo, variable, variable_direccion)
	
	del var_program.variables_temporales[:]
	var_program.variables_temporales_tipo = ""
	#print("tipo de variable: " + str(variable_tipo) + " nombre de variables: " + str(variable_nombre) + " nombre de funcion: " + str(func_nombre))
	#var_program.directorio_func.agregar_variable(func_nombre, variable_tipo, variable_nombre, variable_direccion)

	#print("tipo de variable: " + str(variable_tipo) + " nombre de variable: " + str(variable_nombre) + " nombre de funcion: " + str(func_nombre))
	#var_program.directorio_func.agregar_variable(func_nombre, variable_tipo, variable_nombre, variable_direccion)

#P.N. que identifica la dimension de una variable arreglo
def p_punto_identificarDim(p):
	'''punto_identificarDim : '''
	nombre_variable_arr = p[-5]
	direccion_variable_arr = var_program.pila_operando.pop()
	print(direccion_variable_arr)
	dimension_size = var_program.memoria.get_valor(direccion_variable_arr)
	print(dimension_size)
	dimension_tipo = var_program.pila_tipo.pop()
	print(dimension_tipo)

	#verificar la dimension del arreglo
	if dimension_tipo != 'int':
		print("los valores del arreglo deben ser de tipo entero")
		sys.exit()
	elif dimension_size < 1:
		print("la dimension del arreglo debe ser mayor a 0")
		sys.exit()
	else:
		#Si el arreglo es valido le inserta la informacion de la variable 
		
		var_program.arreglo_actual = {
			'nombre' : nombre_variable_arr,
			'limite_inf' : 0,
			'limite_sup' : dimension_size,
		}

#P.N. que agrega una variable dimensionada (arreglo) a la tabla de variables de la funcion actual
def p_punto_addvarr(p):
	'''punto_addvarr : '''
	variable_tipo = p[-3]
	variable = var_program.arreglo_actual
	#variable_direccion = '0'
	variable_declarada = var_program.directorio_func.verificar_variable_existe(var_program.scope_actual, variable['nombre'])

	if not variable_declarada:
		#pedir direccion de memoria dependiendo de scope
		if var_program.scope_actual == var_program.scope_global:
			direccion_variable = var_program.memoria.pedir_direccion_global_arreglo(variable_tipo, variable['limite_sup'])
		else:
			direccion_variable = var_program.memoria.pedir_direccion_local_arreglo(variable_tipo, variable['limite_sup'])
		

		variable['tipo'] = variable_tipo
		variable['direccion_memoria'] = direccion_variable

		var_program.directorio_func.agregar_variable_dimensionada(var_program.scope_actual, variable)
def p_void_check(p):
	'''void_check : '''
	nombre_funcion = p[-8]
	funcion_objeto = var_program.directorio_func.get_f(nombre_funcion)

	if funcion_objeto["tipo_retorno"] != 'void':
		print("Esta funcion no se puede usar como procedimiento")
		#sys.exit()

#P.N. que crea los cuadruplos para 

# P.N. que identifica el tamaño de los arreglos cuando se declaren
# def p_punto_declaracion_varr(p):
#     '''punto_declaracion_var'''
#     tamano = p[-2]
#     nombre = p[-4]
    

##########################  P.N. PARA GENERACION DE CUADRUPLOS ###############################

#P.N. que inserta un operador a la pila de operadores 
def p_punto_pOper(p):
	'''punto_pOper : ''' 
	var_program.pila_operador.append(p[-1])
	
#FUNCION que resuelve operaciones de las pilas de operando y operadores, creando su cuadruplo
def cuadOperaciones(p):
	resultado_cuad = 'temp'
	#se sacan los operandos de las pilas para el cuadruplo
	operando_der = var_program.pila_operando.pop()
	tipo_der = var_program.pila_tipo.pop()
	operando_izq = var_program.pila_operando.pop()
	tipo_izq = var_program.pila_tipo.pop()

	#sacar el operador de la operacion
	operador = var_program.pila_operador.pop()

	#verificar que el tipo del resultado de la operacion sea valido de acuerdo al punto semantico
	tipo_resultado = var_program.cubo_semantico.get_tipo_semantica(tipo_izq, tipo_der, operador)
	if tipo_resultado != 'error':
		#obtener una direccion temporal de memoria
		direccion_temporal_var = var_program.memoria.pedir_direccion_temporal(tipo_resultado)
		var_program.directorio_func.agregar_temporal(var_program.scope_actual, tipo_resultado)

		#Crear cuadruplo
		cuadrup = Cuadruplos(var_program.numero_cuadruplo, operador, operando_izq, operando_der, direccion_temporal_var)

		#Se agrega el cuadruplo a la lista de cuadruplos y el resultado a la pila de operandos y pila de tipos
		var_program.lista_cuadruplo.append(cuadrup)
		var_program.numero_cuadruplo += 1
		var_program.pila_operando.append(direccion_temporal_var)
		var_program.pila_tipo.append(tipo_resultado)
	else:
		#Si la operacion es entre 2 tipos de variables invalidas
		print('Mismatch de tipos de operandos')
		#sys.exit()

#P.N. que llama la funcion cuadOperaciones para resolver operaciones de "factor"
def p_punto_factor(p):
	'''punto_factor : '''
	if len(var_program.pila_operador) > 0 and len(var_program.pila_operando) > 1:
		if var_program.pila_operador[-1] == '*' or var_program.pila_operador[-1] == '/':
			cuadOperaciones(p)

#P.N. que llama la funcion cuadOperaciones para resolver operaciones de "term"
def p_punto_termino(p):
	'''punto_termino : '''
	if len(var_program.pila_operador) > 0 and len(var_program.pila_operando) > 1:
		if var_program.pila_operador[-1] == '+' or var_program.pila_operador[-1] == '-':
			cuadOperaciones(p)

#P.N. que llama la funcion cuadOperaciones para resolver operaciones relacionales de comparacion
def p_punto_relacion(p):
	'''punto_relacion : '''
	if len(var_program.pila_operador) > 0 and len(var_program.pila_operando) > 1:
		if var_program.pila_operador[-1] == '>' or var_program.pila_operador[-1] == '<' or var_program.pila_operador[-1] == '<=' or var_program.pila_operador[-1] == '>=' or var_program.pila_operador[-1] == '==' or var_program.pila_operador[-1] == '!=' :
				cuadOperaciones(p)

#P.N. que llama la funcion cuadOperaciones para resolver operaciones de logica
def p_punto_logico(p):
	'''punto_logico : '''
	if len(var_program.pila_operador) > 0 and len(var_program.pila_operando) > 1:
		if var_program.pila_operador[-1] == 'AND' or var_program.pila_operador[-1] == 'OR':
			cuadOperaciones(p)

#P.N. que inserta una variable a la pila de operandos
def p_punto_pilaOvar(p):
	'''punto_pilaOvar : '''
	variable = var_program.directorio_func.get_funcion_variable(var_program.scope_actual, p[-1])
	print("variable: ", variable)

	if variable is None:
		#Verifica si la varaible existe en el scope global
		variable = var_program.directorio_func.get_funcion_variable(var_program.scope_global, p[-1])
		if variable is None:
			print("La variable: " + p[-1] + " no esta declarada")
			#sys.exit()
		else:
			#Se agrega variable global a la pila de operandos
			var_program.pila_operando.append(variable['direccion_memoria'])
			var_program.pila_tipo.append(variable['tipo'])
	else:
		#Se agrega variable local a la pila de operandos
			var_program.pila_operando.append(variable['direccion_memoria'])
			var_program.pila_tipo.append(variable['tipo'])

#P.N. que inserta una constante entera a la pila de operandos
def p_punto_pilaOint(p):
	'''punto_pilaOint : '''
	#busqueda o asignacion de direccion de memoria 
	direccion_constante = var_program.memoria.ver_valor_constante_existe('int', int(p[-1]))
	if direccion_constante is None:
		direccion_constante = var_program.memoria.pedir_direccion_constante('int', int(p[-1]))

	
	var_program.pila_operando.append(direccion_constante)
	var_program.pila_tipo.append('int')

#P.N. que inserta una constante flotante a la pila de operandos
def p_punto_pilaOfloat(p):
	'''punto_pilaOfloat : '''
	#busqueda o asignacion de direccion de memoria 
	direccion_constante = var_program.memoria.ver_valor_constante_existe('float', float(p[-1]))
	if direccion_constante is None:
		direccion_constante = var_program.memoria.pedir_direccion_constante('float', float(p[-1]))

	var_program.pila_operando.append(direccion_constante)
	var_program.pila_tipo.append('float')

#P.N. que inserta una constante booleana a la pila de operandos
def p_punto_pilaObool(p):
	'''punto_pilaObool : '''
	#busqueda o asignacion de direccion de memoria 
	direccion_constante = var_program.memoria.ver_valor_constante_existe('bool', bool(p[-1]))
	if direccion_constante is None:
		direccion_constante = var_program.memoria.pedir_direccion_constante('bool', bool(p[-1]))

	var_program.pila_operando.append(direccion_constante)
	var_program.pila_tipo.append('bool')
 
def p_punto_pilaOString(p):
    ''' punto_pilaOString : '''
    var_program.pila_operando.append(str(p[-1]))
    var_program.pila_tipo.append('string')  

def p_punto_pilaOchar(p):
    ''' punto_pilaOchar : '''
    print("pasa por aqui")
    var_program.pila_operando.append(p[-1])
    var_program.pila_tipo.append('char')

#P.N. que crea y agrega un fondo falso a la pila de operadores
def p_punto_fondoIni(p):
    '''punto_fondoIni : '''
    var_program.pila_operador.append('()')
    
#P.N. que se deshace del fondo falso
def p_punto_fondoFin(p):
    '''punto_fondoFin : '''
    var_program.pila_operador.pop()

#P.N. que crea un cuadruplo de lectura (read)
def p_punto_cuadRead(p):
	'''punto_cuadRead : '''
	mensaje_dir = var_program.pila_operando.pop()
	variable_tipo = var_program.pila_tipo.pop()
 
	print("mensaje_dir: ", mensaje_dir)
	print("variable_tipo: ", variable_tipo)

	#Se obtiene el tipo de variable del que consistira el input de lectura y pide un espacio temporal de memoria para resolverlo
	# variable_tipo = var_program.pila_tipo[-1]
	#agregar a memoria

	var_program.pila_tipo.append(variable_tipo)

	cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'READ', variable_tipo, None ,mensaje_dir)
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1

#P.N. que resuleve una asignacion (con el cubo semantico) y crea su cuadruplo
def p_punto_cuadAssign(p):
	'''punto_cuadAssign : '''
	#obtener operador
	operador = var_program.pila_operador.pop()

	if operador == '=':
		#obtener operando con su tipo
		# print("lista 1 : ", var_program.pila_operando)
		operando_der = var_program.pila_operando.pop()
		# print("derecho: ",operando_der)
		tipo_der = var_program.pila_tipo.pop()
		# print("lista 2 : ", var_program.pila_operando)
		operando_izq = var_program.pila_operando.pop()
		# print("izquierdo: ",operando_izq)
		tipo_izq = var_program.pila_tipo.pop()

		#obtener el tipo del resultado de los operandos
		tipo_resultado = var_program.cubo_semantico.get_tipo_semantica(tipo_izq, tipo_der, operador)
		# print("tipo_resultado: ", tipo_resultado)
		#Si no es type_mismatch
		if tipo_resultado != 'error':
			#crear cuadruplo
			cuadrup = Cuadruplos(var_program.numero_cuadruplo, operador, operando_der, None , operando_izq)

			#se agrega el cuadruplo a la lista de cuadruplos y se incrementa el contador
			var_program.lista_cuadruplo.append(cuadrup)
			var_program.numero_cuadruplo += 1
		else:
			# print('Mismatch de operandos en: {0}'.format(p.lexer.lineno))
   			print('Mismatch de operandos en: {0}'.format(p.lexer.lineno))
			#sys.exit()

################################################### P.N. para cuadruplos de ciclos y condicionales ###############################################

#Funcion que crea el cuadruplo de condicion GotoF para "IF" y "WHILE"
def p_punto_crearGotoF(p):
    '''punto_crearGotoF : '''
    tipo_resultado = var_program.pila_tipo.pop()
    #verificar que el resultado de la condicion sea booleano
    if tipo_resultado != 'bool':
        print('Mismatch de tipo en operacion')
    else:
        #Crear cuadruplo GotoF
        resultado = var_program.pila_operando.pop()
        cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'GotoF', resultado, None, None)
        var_program.lista_cuadruplo.append(cuadrup)
        #guardar numero de cuadruplo GotoF en pila de saltos para terminar despues
        var_program.pila_saltos.append(var_program.numero_cuadruplo - 1)
        var_program.numero_cuadruplo += 1

# #P.N. que llama la funcion "cuadCondicion" para crear el cuadruplo GotoF
# def p_punto_crearGotoF(p):
#     '''punto_crearGotoF : '''
#     cuadCondicion(p)
    
#P.N. que completa los cuadruplos GotoF con la pila de saltos
def p_punto_fillGotoF(p):
	'''punto_fillGotoF : '''
	#Se busca el numero del cuadruplo que tiene el GotoF que se va rellenar
	numero_cuadruplo_fill = var_program.pila_saltos.pop()
	cuadrup = var_program.lista_cuadruplo[numero_cuadruplo_fill]
	#Se llama el proceso de llenar el cuadruplo GotoF de la clase cuadruplo 
	#Se rellena el cuadruplo con con el numero del cuadruplo que sigue
	cuadrup.cuadruplo_saltos(var_program.numero_cuadruplo)

#P.N. que crea los cuadruplos de ELSE
def p_punto_else(p):
	'''punto_else : '''
	#Se crea el cuadruplo GOTO y se agrega a la lista de cuadruplos
	cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'Goto', None, None, None)
	var_program.lista_cuadruplo.append(cuadrup)

	#Se busca el numerodel cuadruplo GotoF para llenar
	numero_cuadruplo_fill = var_program.pila_saltos.pop()
	cuadrup = var_program.lista_cuadruplo[numero_cuadruplo_fill]
	#Se guarda el numero del cuadruplo del GOTO en la pila de saltos
	var_program.pila_saltos.append(var_program.numero_cuadruplo - 1)
	var_program.numero_cuadruplo += 1
	#Se llena el GotoF del IF con el numero del cuadruplo que sigue despues de Goto
	cuadrup.cuadruplo_saltos(var_program.numero_cuadruplo)

#P.N. que guarda el numero de cuadruplo de la expresion del WHILE para regresar mas tarde
def p_punto_guardarWhile(p):
	'''punto_guardarWhile : '''
	var_program.pila_saltos.append(var_program.numero_cuadruplo)

#P.N. que crea el cuadruplo GOTO para regresar a la condicion del WHILE y reiniciar el ciclo
def p_punto_regreserWhile(p):
	'''punto_regresarWhile : '''
	#Se busca el numero del cuadruplo para rellenar el GotoF del WHILE y el cuadruplo de la condicion para el GOTO
	numero_cuadruplo_fill = var_program.pila_saltos.pop()
	numero_cuadruplo_regreso = var_program.pila_saltos.pop()
	#Se crea el cuadruplo GOTO
	cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'GOTO', None, None, numero_cuadruplo_regreso)
	#Se inserta el cuadruplo a la lista de cuadruplos 
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1
	#Se rellena el GotoF para salir de ciclos
	cuadrup_cond = var_program.lista_cuadruplo[numero_cuadruplo_fill]
	cuadrup_cond.cuadruplo_saltos(var_program.numero_cuadruplo)

#P.N. que crea el cuadruplo de PRINT
def p_punto_print(p):
	''' punto_print : '''
	#sacar direccion de memoria de lo que se va a imprimir de la pila de operandos
	operando = var_program.pila_operando.pop()
	#crear cadruplo PRINT
	cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'PRINT', operando, None, None)
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1
 
################################################# P.N. para generacion de cuadruplos de funciones ######################################################

#P.N. para generar el cuadruplo GOTO que salta a la funcion "main"
def p_punto_gotoMain(p):
	'''punto_gotoMain : '''
	cuadrup =Cuadruplos(var_program.numero_cuadruplo, 'GOTO', 'MAIN', None, None)
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1

#P.N. que genera el cuadruplo ENDPROC para el final de una funcion
def p_punto_endProc(p):
	'''punto_endProc : '''
	tipo_funcion = p[-7]
	#print(var_program.bandera_retorno)

	if (tipo_funcion == 'void' and var_program.bandera_retorno):
		print("La funcion no debio de regresar un valor")
		sys.exit()
	elif tipo_funcion != 'void' and not var_program.bandera_retorno:
		print("La funcion debio de haber regresado un valor")
		sys.exit()
	else:
		#Se genera el cuadruplo ENDPROC
		cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'ENDPROC', None, None, None)
		var_program.lista_cuadruplo.append(cuadrup)

	#Rellena el los cuadruplos Goto if si existen
	if var_program.bandera_retorno:
		while var_program.lista_retorno:
			numero_cuadruplo_fill = var_program.lista_retorno.pop()
			var_program.lista_cuadruplo[numero_cuadruplo_fill - 1].cuadruplo_saltos(var_program.numero_cuadruplo)

	var_program.numero_cuadruplo += 1
	var_program.bandera_retorno = False

	#Resetea y borra la memoria temporal
	var_program.scope_actual = var_program.scope_global
	var_program.memoria.reset_temporal()

#P.N. que genera el cuadruplo ERA, verifica que una funcion exista en el directorio de funciones y crea su espacio en memoria
def p_punto_era(p):
	'''punto_era : '''
	funcion = p[-3]
	#Verificar que la funcion existe
	if var_program.directorio_func.busqueda_f(funcion):
		# Creacion del cuadruplo ERA
		cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'ERA', funcion, None, None)
		var_program.lista_cuadruplo.append(cuadrup)
		var_program.numero_cuadruplo += 1
		#Se obtienen los parametros de una funcion
		parametros = var_program.directorio_func.get_funcion_parametros(funcion)
		var_program.argumentos_temporales_tipos = list(parametros['tipo'])
		print(var_program.argumentos_temporales_tipos)
	else:
		print("Error: La funcion que se esta llamando, No existe")
		sys.exit()

#P.N. que resuelve un argumento y genera los cuadruplos PARAMS
def p_punto_params(p):
	'''punto_params : '''
	#Se verifica que no haya mas argumentos que parametros de la funcion que se llama
	if var_program.argumentos_temporales_tipos:
		#Se obtiene el argumento y su tipo de las pilas 
		argumento = var_program.pila_operando.pop()
		argumento_tipo = var_program.pila_tipo.pop()
		parametro_tipo = var_program.argumentos_temporales_tipos.pop(0)
		#Se asegura que el tipo del argumento y el tipo de parametro sean iguales 
		if argumento_tipo == parametro_tipo:
			cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'PARAM', argumento, None, None)
			var_program.lista_cuadruplo.append(cuadrup)
			var_program.numero_cuadruplo += 1
		else:
			print("Error: El argumento con el que se llama la funcion, no es del mismo tipo que su parametro")
			sys.exit()
	else:
		print("Error: mismatch en numero de argumentos")
		sys.exit()

#P.N. que resuelve la llamada a una funcion y genera los cuadruplos GOSUB
def p_punto_gosub(p): 
	'''punto_gosub : '''
	#Verifica que no haya mas parametros que argumentos
	if not var_program.argumentos_temporales_tipos:
		#Obtiene la funcion y su numero de cuadruplo
		funcion = p[-7]
		funcion_numero_cuadruplo = var_program.directorio_func.get_numero_cuadruplo(funcion)
		#Se genera el cuadruplo GOSUB 
		cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'GOSUB', funcion, None, funcion_numero_cuadruplo)
		var_program.lista_cuadruplo.append(cuadrup)
		var_program.numero_cuadruplo += 1
	else:
		print("Error: Mismatch en el numero de parametros")
		sys.exit()

#P.N. que al leer el RETURN  marca la bandera_retorno como TRUE
def p_punto_returnTrue(p):
	'''punto_returnTrue : '''
	var_program.bandera_retorno = True

#P.N. que agrega el resultado producido por la llamada de funcion a la pila de operandos y crea su cuadruplo de asignacion
def p_punto_funcCallR(p):
	'''punto_funcCallR : '''
	funcion_llamada = p[-8]
	funcion = var_program.directorio_func.get_f(funcion_llamada)
	funcion_retorno = funcion['direccion_retorno']
	funcion_tipo = funcion['tipo_retorno']
	#Se pide una variable temporal para el resultado de la funcion que se llamo
	direccion_temporal_var = var_program.memoria.pedir_direccion_temporal(funcion_tipo)
	var_program.directorio_func.agregar_temporal(var_program.scope_actual, funcion_tipo)
	#Se crea el cuadruplo que asigna el valor de la funcion a la direccion temporal y la agrega a la pila de operandos
	cuadrup = Cuadruplos(var_program.numero_cuadruplo, '=', funcion_retorno, None, direccion_temporal_var)
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1
	#Se sube la direccion de memoria a pila de operadandos
	var_program.pila_operando.append(direccion_temporal_var)
	var_program.pila_tipo.append(funcion_tipo)

##################################################### P.N. que generan los cuadruplos de funciones especiales #################################################

#P.N. que crea una direccion temporal para las funciones especiales y mete la direccion a la pila de oprenados
#def p_punto_agregarEspecial(p):
#	'''punto_agregarEspecial : '''


#P.N. para el cuadruplo de la funcion: MODA
def p_punto_cuadModa(p):
	'''punto_cuadModa : '''
	#Se hace pop para sacar el arreglo de la pila de operandos
	id_variable = p[-7]
	#print("tipo_var: ", id_variable)
	variable = var_program.directorio_func.get_funcion_variable(var_program.scope_actual, id_variable)
	#print("variable", variable)
	tipo_var = variable['tipo']
	#print("tipo de variable: ", tipo_var)
	temporal = var_program.memoria.pedir_direccion_temporal(tipo_var)
	#print("temporal: ", temporal)
	operand = var_program.pila_operando.pop()
	cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'MODA', operand, None, temporal)
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1
	var_program.pila_operando.append(temporal)
	var_program.pila_tipo.append(tipo_var)

#P.N. para el cuadruplo de la funcion: MEDIANA
def p_punto_cuadMedian(p):
	'''punto_cuadMedian : '''
	#Se hace pop para sacar el arreglo de la pila de operandos
	id_variable = p[-7]
	variable = var_program.directorio_func.get_funcion_variable(var_program.scope_actual, id_variable)
	tipo_var = variable['tipo']
	temporal = var_program.memoria.pedir_direccion_temporal(tipo_var)
	operand = var_program.pila_operando.pop()
	cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'MEDIAN', operand, None, temporal)
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1
	var_program.pila_operando.append(temporal)
	var_program.pila_tipo.append(tipo_var)

#P.N. para el cuadruplo de la funcion: SUMATORIA
def p_punto_cuadSum(p):
	'''punto_cuadSum : '''
	#Se hace pop para sacar el arreglo de la pila de operandos
	id_variable = p[-7]
	#print("tipo_var: ", id_variable)
	variable = var_program.directorio_func.get_funcion_variable(var_program.scope_actual, id_variable)
	#print("variable", variable)
	tipo_var = variable['tipo']
	#print("tipo de variable: ", tipo_var)
	temporal = var_program.memoria.pedir_direccion_temporal(tipo_var)
	#print("temporal: ", temporal)
	operand = var_program.pila_operando.pop()
	operand = var_program.pila_operando.pop()
	cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'SUM', operand, None, temporal)
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1
	var_program.pila_operando.append(temporal)
	var_program.pila_tipo.append(tipo_var)

#P.N. para el cuadruplo de la funcion: DESVIACION ESTANDAR
def p_punto_cuadDesv(p):
	'''punto_cuadDesv : '''
	#Se hace pop para sacar los arreglos de la pila de operandos
	id_variable = p[-7]
	#print("tipo_var: ", id_variable)
	variable = var_program.directorio_func.get_funcion_variable(var_program.scope_actual, id_variable)
	#print("variable", variable)
	tipo_var = variable['tipo']
	#print("tipo de variable: ", tipo_var)
	temporal = var_program.memoria.pedir_direccion_temporal(tipo_var)
	#print("temporal: ", temporal)
	operand1 = var_program.pila_operando.pop()
	operand2 = var_program.pila_operando.pop()
	cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'DESV', operand2, operand1, temporal)
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1
	var_program.pila_operando.append(temporal)
	var_program.pila_tipo.append(tipo_var)

#P.N. para el cuadruplo de la funcion: PENDIENTE
###Verificar que regrese un arreglo 
def p_punto_cuadPend(p):
	'''punto_cuadPend : '''
	#Se hace pop para sacar el arreglo de la pila de operandos
	operand1 = var_program.pila_operando.pop()
	operand2 = var_program.pila_operando.pop()
	cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'PEND', operand2, operand1, None)
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1

def p_punto_cuadVarian(p):
	'''punto_cuadVarian : '''
	id_variable = p[-7]
	variable = var_program.directorio_func.get_funcion_variable(var_program.scope_actual, id_variable)
	tipo_var = variable['tipo']
	temporal = var_program.memoria.pedir_direccion_temporal(tipo_var)
	operand = var_program.pila_operando.pop()
	cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'VARIANCE', operand, None, temporal)
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1
	var_program.pila_operando.append(temporal)
	var_program.pila_tipo.append(tipo_var)

#P.N. para el cuadruplo de la funcion: R_SQUARE
def p_punto_cuadRsquar(p):
	'''punto_cuadRsquar : '''
	#Se hace pop para sacar los arreglos de la pila de operandos
	id_variable = p[-7]
	#print("tipo_var: ", id_variable)
	variable = var_program.directorio_func.get_funcion_variable(var_program.scope_actual, id_variable)
	#print("variable", variable)
	tipo_var = variable['tipo']
	#print("tipo de variable: ", tipo_var)
	temporal = var_program.memoria.pedir_direccion_temporal(tipo_var)
	#print("temporal: ", temporal)
	operand1 = var_program.pila_operando.pop()
	operand2 = var_program.pila_operando.pop()
	cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'RSQUARE', operand2, operand1, temporal)
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1
	var_program.pila_operando.append(temporal)
	var_program.pila_tipo.append(tipo_var)

#P.N. para el cuadruplo de la funcion: BERNOULLI
def p_punto_cuadBernou(p):
	'''punto_cuadBernou : '''
	#Se hace pop para sacar los arreglos de la pila de operandos
	id_variable = p[-7]
	print("tipo_var: ", id_variable)
	variable = var_program.directorio_func.get_funcion_variable(var_program.scope_actual, id_variable)
	print("variable", variable)
	tipo_var = variable['tipo']
	print("tipo de variable: ", tipo_var)
	temporal = var_program.memoria.pedir_direccion_temporal(tipo_var)
	print("temporal: ", temporal)
	operand1 = var_program.pila_operando.pop()
	operand2 = var_program.pila_operando.pop()
	cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'BERNOU', operand1, operand2, temporal)
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1
	var_program.pila_operando.append(temporal)
	var_program.pila_tipo.append(tipo_var)

#P.N. para el cuadruplo de la funcion: GRAPH_SCATTER sin Pendiente
def p_punto_cuadScatt(p):
	'''punto_cuadScatt : '''
	#Se hace pop para sacar los arreglos de la pila de operandos
	operand1 = var_program.pila_operando.pop()
	operand2 = var_program.pila_operando.pop()
	cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'SCATT', operand2, operand1, None)
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1

#P.N. para el cuadruplo de la funcion: GRAPH_SCATTER con Pendiente
def p_punto_cuadScattPend(p):
	'''punto_cuadScattPend : '''
	#Se hace pop para sacar los arreglos de la pila de operandos
	operand1 = var_program.pila_operando.pop()
	operand2 = var_program.pila_operando.pop()
	operand3 = var_program.pila_operador.pop()
	cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'SCATTPEND', operand2, operand1, operand3)
	var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1


## ARCHIVO A COMPILAR ##
parser = yacc.yacc()

# nombre del archivo a compilar
name = 'archivo4.txt'

with open(name, 'r') as myfile:
	s = myfile.read().replace('\n', '')
print("Nombre del archivo de prueba: " + name + "\n")
parser.parse(s)

# Imprimir programa
var_program.directorio_func.print_directorio()
var_program.print_cuadruplos()
# Imprimir los parametros de las funciones (comentar el borrado de la lista de parametros para que despliegue algo)
# var_program.print_temporales_parametros_nombres()
# var_program.print_temporales_parametros_tipos()


# var_program.print_programa()
# print ("Numero de variables: ", var_program.get_variable_tempo())
# while True:
#     try:
#         s = input('')
#     except EOFError:
#         break
#     parser.parse(s)