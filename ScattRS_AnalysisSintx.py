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
	assign : ID assign_A1 ASSIGN assign_A2 SEMICOLON
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
	factor : PAREN_I expression PAREN_D 
		| fact_A1 var_cte
	'''
	# print("SI SE factor")

def p_fact_A1(p):
	'''
	fact_A1 : OP_SUMA 
		| OP_RESTA 
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
	var_cte : ID var_cte_A1 
		| INT_VALOR 
		| FLOAT_VALOR
		| TRUE
		| FALSE 
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
	exp : term exp_A1
	'''
	# print("SI SE exp")

def p_exp_A1(p):
	'''
	exp_A1 : OP_SUMA 
		| OP_RESTA 
		| empty
	'''

def p_arr(p):
	'''
	arr : BRACKET_I INT_VALOR BRACKET_D
	'''
	# print("SI SE arr")

def p_term(p):
	'''
	term : factor term_A1
	'''
	# print("SI SE term")

def p_term_A1(p):
	'''
	term_A1 : OP_MULT 
		| OP_DIV 
		| empty
	'''

def p_expression(p):
	'''
	expression : exp expression_A1 exp
		| exp
	'''
	# print("SI SE expression")

def p_expression_A1(p):
	'''
	expression_A1 : MAYOR  
		| MENOR 
		| MAYOR_EQ  
		| MENOR_EQ 
		| EQUAL 
		| NOT_EQ 
	'''

def p_exp_cond(p):
	''' 
	exp_cond : expression exp_cond_A1
	'''
	# print("Si se exp_cond")

def p_exp_cond_A1(p):
	'''
	exp_cond_A1 : OR expression 
		| AND expression 
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
	cond : IF PAREN_I exp_cond PAREN_D bloque cond_A1
	'''
	# print("Si se pudo cond")

def p_cond_A1(p):
	'''
	cond_A1 : ELSE bloque 
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
	readf : READ PAREN_I expression PAREN_D punto_cuadRead SEMICOLON
	'''
	# print("Si se pudo read")

def p_while(p):
    '''
	while : WHILE PAREN_I exp_cond PAREN_D bloque
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
    

#P.N. que crea un cuadruplo de lectura (read)
def p_punto_cuadRead(p):
	'''punto_cuadRead : '''
	mensaje_dir = var_program.pila_operando.pop()
	var_program.pila_tipo.pop()

	#Se obtiene el tipo de variable del que consistira el input de lectura y pide un espacio temporal de memoria para resolverlo
	variable_tipo = var_program.pila_tipo[-1]
	#agregar a memoria

	var_program.pila_tipo.append(variable_tipo)

	# cuadrup = Cuadruplos(var_program.numero_cuadruplo, 'READ', variable_tipo, mensaje_dir)
	# var_program.lista_cuadruplo.append(cuadrup)
	var_program.numero_cuadruplo += 1

#P.N. que resuleve una asignacion (con el cubo semantico) y crea su cuadruplo
def p_punto_cuadAssign(p):
	'''punto_cuadAssign : '''
	#obtener operador
	operador = var_program.pila_operador.pop()

	if operador == '=':
		#obtener operador con su tipo
		operando_der = var_program.pila_operador.pop()
		tipo_der = var_program.pila_tipo.pop()
		operando_izq = var_program.pila_operador.pop()
		tipo_izq = var_program.pila_tipo.pop()

		#obtener el tipo del resultado de los operandos
		tipo_resultado = var_program.cubo_semantico.get_tipo_semantica(tipo_izq, tipo_der, operador)

		#Si no es type_mismatch
		if tipo_resultado != 'error':
			#crear cuadruplo
			# cuadrup = Cuadruplos(var_program.numero_cuadruplo, operador, operando_der, operando_izq)

			#se agrega el cuadruplo a la lista de cuadruplos y se incrementa el contador
			#var_program.lista_cuadruplo.append(cuadrup)
   			var_program.numero_cuadruplo += 1
		else:
			# print('Mismatch de operandos en: {0}'.format(p.lexer.lineno))
   			print('Mismatch de operandos en: {0}'.format(p.lexer.lineno))
			#sys.exit()

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