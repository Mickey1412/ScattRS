# coding=utf-8
import ply.yacc as yacc
from scattRS_AnalysisLex import tokens
from scattRS_Programa import Programa
from scattRS_Cuadruplos import Cuadruplos

#variable que toma la clase programa para llamar los procedimientos del directorio de funciones y cuadruplos
var_program = Programa()

# Gramaticas del compilador
def p_programa(p):
	'''
	programa : PROGRAM ID punto_creardf progra_A1 progra_A2 MAIN PAREN_I PAREN_D punto_main bloque
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
	funcion : FUNC func_tipo ID PAREN_I func_param PAREN_D punto_addf bloque
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
	| PARAMS tipo ID arr SEMICOLON
	'''
	# print("SI SE var")

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
	args : expression 
		| expression COMA args 
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
	'''
	# print("exp: " + str(p[1]))
	# print("SI SE var_cte")

def p_var_cte_A1(p):
	'''
	var_cte_A1 : BRACKET_I exp BRACKET_D 
		| PAREN_I var_cte_A2 PAREN_D 
		| empty
	'''

def p_var_cte_A2(p):
	'''
	var_cte_A2 : exp COMA var_cte_A2 
		| exp 
		| empty
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
	arr : BRACKET_I INT_VALOR BRACKET_D
	'''
	# print("SI SE arr")

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
	printf : PRINT PAREN_I print_A1 PAREN_D SEMICOLON
	'''
	# print("Si se pudo print")

def p_print_A1(p):
	'''
	print_A1 : expression 
		| STRING_VALOR
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
	func_call : ID PAREN_I args PAREN_D
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
		| MODA estadistica_A1 
		| MEDIAN estadistica_A1 
		| SUM estadistica_A1 
		| DESVIA estadistica_A2 
		| PEND estadistica_A2 
		| VARIANCE estadistica_A1 
		| R_SQUARE estadistica_A2 
		| BINOMIAL estadistica_A3 
		| BERNOULLI estadistica_A2
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
	estadistica_A1 : PAREN_I ID PAREN_D 
	'''
	# print(p[1],p[2],p[3],p[4])

def p_estadistica_A2(p):
	'''
	estadistica_A2 : PAREN_I ID COMA ID PAREN_D 
	'''

def p_estadistica_A3(p):
	'''
	estadistica_A3 : PAREN_I ID COMA ID COMA ID PAREN_D 
	'''

def p_estadistica_A4(p):
	'''
	estadistica_A4 : estadistica_A2 
		| estadistica_A3
	'''

def p_return(p):
	'''
	return : RETURN exp SEMICOLON
	'''
	# print("Si se pudo return")

def p_readf(p):
	'''
	readf : READ PAREN_I expression PAREN_D SEMICOLON 
	'''
	# print("Si se pudo read")

def p_while(p):
    '''
	while : WHILE punto_guardarWhile PAREN_I exp_cond PAREN_D punto_crearGotoF bloque punto_guardarWhile
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
def p_punto_addf(p):
	'''punto_addf : '''
	var_program.scope_actual = p[-4]
	tipofuncion = p[-5]
	
 	#Agrega la funcion al directorio 
	var_program.directorio_func.agregar_func(var_program.scope_actual, tipofuncion)
	
 	# Agregar las variables en la tabla de variables
	variables = zip(var_program.parametros_temporales_nombres, var_program.parametros_temporales_tipos)
	for variable_nombre, variable_tipo in variables: 
		var_program.directorio_func.agregar_variable(var_program.scope_actual, variable_tipo, variable_nombre)
	
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
	#variable_tipo = p[-2]
	#variable_nombre = p[-1]
	variable_direccion = '0'
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

			# print("tipo de variable: " + str(var_program.variables_temporales_tipo) + " nombre de variables: " + str(variable) + " nombre de funcion: " + str(func_nombre))
			var_program.directorio_func.agregar_variable(var_program.scope_actual, var_program.variables_temporales_tipo, variable, variable_direccion)
	
	del var_program.variables_temporales[:]
	var_program.variables_temporales_tipo = ""
	#print("tipo de variable: " + str(variable_tipo) + " nombre de variables: " + str(variable_nombre) + " nombre de funcion: " + str(func_nombre))
	#var_program.directorio_func.agregar_variable(func_nombre, variable_tipo, variable_nombre, variable_direccion)

	#print("tipo de variable: " + str(variable_tipo) + " nombre de variable: " + str(variable_nombre) + " nombre de funcion: " + str(func_nombre))
	#var_program.directorio_func.agregar_variable(func_nombre, variable_tipo, variable_nombre, variable_direccion)



#P.N. que agrega una variable dimensionada (arreglo) a la tabla de variables de la funcion actual
def p_punto_addvarr(p):
	'''punto_addvarr : '''
	variable_tipo = p[-3]
	variable = var_program.arreglo_actual
	variable_direccion = '0'
	variable_declarada = var_program.directorio_func.verificar_variable_existe(var_program.scope_actual, variable['nombre'])

	if not variable_declarada:
		#pedir direccion de memoria dependiendo de scope

		variable['tipo'] = variable_tipo
		variable['direccion_memoria'] = variable_direccion

		var_program.directorio_func.agregar_variable_dimensionada(var_program.scope_actual, variable)


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
		#####

		#Crear cuadruplo
		cuadrup = Cuadruplos(var_program.numero_cuadruplo, operador, operando_izq, operando_der, resultado_cuad)

		#Se agrega el cuadruplo a la lista de cuadruplos y el resultado a la pila de operandos y pila de tipos
		var_program.lista_cuadruplo.append(cuadrup)
		var_program.numero_cuadruplo += 1
		var_program.pila_operando.append(resultado_cuad)
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

	if variable is None:
		#Verifica si la varaible existe en el scope global
		variable = var_program.directorio_func.get_funcion_variable(var_program.scope_global, p[-1])
		if variable is None:
			print("La variable: " + p[-1] + " no esta declarada")
			#sys.exit()
		else:
			#Se agrega variable global a la pila de operandos
			var_program.pila_operando.append(variable['nombre'])
			var_program.pila_tipo.append(variable['tipo'])
	else:
		#Se agrega variable local a la pila de operandos
			var_program.pila_operando.append(variable['nombre'])
			var_program.pila_tipo.append(variable['tipo'])

#P.N. que inserta una constante entera a la pila de operandos
def p_punto_pilaOint(p):
	'''punto_pilaOint : '''
	#busqueda o asignacion de direccion de memoria 
	#########

	var_program.pila_operando.append(int(p[-1]))
	var_program.pila_tipo.append('int')

#P.N. que inserta una constante flotante a la pila de operandos
def p_punto_pilaOfloat(p):
	'''punto_pilaOfloat : '''
	#busqueda o asignacion de direccion de memoria 
	#########

	var_program.pila_operando.append(float(p[-1]))
	var_program.pila_tipo.append('float')

#P.N. que inserta una constante booleana a la pila de operandos
def p_punto_pilaObool(p):
	'''punto_pilaObool : '''
	#busqueda o asignacion de direccion de memoria 
	#########

	var_program.pila_operando.append(bool(p[-1]))
	var_program.pila_tipo.append('bool')

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
	var_program.pila_tipo.pop()

	#Se obtiene el tipo de variable del que consistira el input de lectura y pide un espacio temporal de memoria para resolverlo
	variable_tipo = var_program.pila_tipo[-1]
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
		print("lista 1 : ", var_program.pila_operando)
		operando_der = var_program.pila_operando.pop()
		tipo_der = var_program.pila_tipo.pop()
		print("lista 2 : ", var_program.pila_operando)
		operando_izq = var_program.pila_operando.pop()
		tipo_izq = var_program.pila_tipo.pop()

		#obtener el tipo del resultado de los operandos
		tipo_resultado = var_program.cubo_semantico.get_tipo_semantica(tipo_izq, tipo_der, operador)

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

############################## P.N. para cuadruplos de ciclos y condicionales ###################################

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
	'''punto regresarWhile : '''
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



## ARCHIVO A COMPILAR ##
parser = yacc.yacc()

# nombre del archivo a compilar
name = 'archivo2.txt'

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