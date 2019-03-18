import ply.yacc as yacc
from ScattRS_AnalysisLex import tokens

def p_programa(p):
	'''
	programa : PROGRAM ID progra_A1 progra_A2 MAIN bloque
	'''
	print("SI SE PUDO")

def p_progra_A1(p):
	'''
	progra_A1 : var progra_A1 
		| empty
	'''

def p_progra_A2(p):
	'''
	progra_A2 : funcion progra_A2 
		| empty
	'''

def p_funcion(p):
	'''
	funcion : FUNC func_tipo ID PAREN_I func_param PAREN_D bloque
	'''
	print("SI SE PUDO funcion")

def p_func_tipo(p):
	'''
	func_tipo : VOID 
		| tipo
	'''

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
	print("SI SE param")

def p_var(p):
	'''
	var : PARAMS tipo var_A1 SEMICOLON 
	'''
	print("SI SE var")

def p_var_A1(p):
	'''
	var_A1 : ID arr 
		| ID arr COMA var_A1 
		| ID 
		| ID COMA var_A1
	'''

def p_assign(p):
	'''
	assign : ID assign_A1 EQUAL exp_cond SEMICOLON
	'''
	print("SI SE assign")

def p_assign_A1(p):
	'''
	assign_A1 : BRACKET_I exp BRACKET_D 
		| empty 
	'''

def p_args(p):
	'''
	args : expression 
		| expression COMA args 
		| empty
	'''
	print("SI SE args")

def p_factor(p):
	'''
	factor : PAREN_I expression PAREN_D 
		| fact_A1 var_cte
	'''
	print("SI SE factor")

def p_fact_A1(p):
	'''
	fact_A1 : OP_SUMA 
		| OP_RESTA 
		| empty
	'''

# Agregar el "read"
def p_stmt(p):
	'''
	stmt : func_call 
		| assign 
		| cond 
		| printf 
		| return 
		| estadistica 
	'''
	print("SI SE stmt")

def p_tipo(p):
	'''
	tipo : INT 
		| FLOAT 
		| BOOL 
		| CHAR 
	'''
	print("SI SE tipo")

def p_var_cte(p):
	'''
	var_cte : ID var_cte_A1 
		| INT_VALOR 
		| FLOAT_VALOR 
	'''
	print("SI SE var_cte")

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
	print("SI SE exp")

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
	print("SI SE arr")

def p_term(p):
	'''
	term : factor term_A1
	'''
	print("SI SE term")

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
	print("SI SE expression")

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
	exp_cond : exp exp_cond_A1 
	'''
	print("SI SE exp_cond")

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
	print("SI SE print")

def p_print_A1(p):
	'''
	print_A1 : expression 
		| STRING_VALOR
	'''

def p_cond(p):
 	'''
 	cond : IF PAREN_I exp_cond PAREN_D bloque cond_A1 SEMICOLON
 	'''

def p_cond_A1(p):
 	'''
 	cond_A1 : ELSE bloque 
	 	| empty
 	'''

def p_func_call(p):
 	'''
 	func_call : ID PAREN_I args PAREN_D
 	'''

def p_bloque(p):
 	'''
 	bloque : CURLY_I bloque_A1 CURLY_D
 	'''

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
		| GRAPH_BAR estadistica_A2 
		| GRAPH_SCATTER estadistica_A4 
 		| BINOMIAL estadistica_A3 
		| BERNOULLI estadistica_A2
 	'''

def p_estadistica_A1(p):
 	'''
 	estadistica_A1 : PAREN_I ID PAREN_D SEMICOLON
 	'''

def p_estadistica_A2(p):
 	'''
 	estadistica_A2 : PAREN_I ID COMA ID PAREN_D SEMICOLON
 	'''

def p_estadistica_A3(p):
 	'''
 	estadistica_A3 : PAREN_I ID COMA ID COMA ID PAREN_D SEMICOLON
 	'''

def p_estadistica_A4(p):
 	'''
 	estadistica_A4 : estadistica_A2 
		| estadistica_A3
 	'''

def p_return(p):
    '''
	return : RETURN exp_cond SEMICOLON
	'''

def p_empty(p):
    'empty :'
    pass

parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)