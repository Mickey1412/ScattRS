def p_programa(p):
	'''
	programa : PROGRAM ID progra_A1 progra_A2 MAIN bloque
	'''

def progra_A1(p):
	'''
	progra_A1 : var progra_A1 | empty
	'''

def progra_A2(p):
	'''
	progra_A2 : function progra_A2 | empty
	'''

def function(p):
	'''
	function : FUNC func_tipo ID PAREN_I func_param PAREN_D bloque
	'''

def func_tipo(p):
	'''
	func_tipo: void | tipo
	'''

def func_param(p):
	'''
	func_param : param | param COMA func_param | void
	'''

def param(p):
	'''
	param : tipo ID
	'''

def var(p):
	'''
	var : PARAMS tipo var_A1 SEMICOLON 
	'''

def var_A1(p):
	'''
	var_A1: ID ARR | ID ARR COMA var_A1 | ID | ID COMA var_A1
	'''

def assign(p):
	'''
	assign : ID assign_A1 EQUAL exp_cond SEMICOLON
	'''

def assign_A1(p):
	'''
	assign_A1 : BRACKET_I exp BRACKET_D | empty 
	'''

def args(p):
	'''
	args : expression | expression COMA args | empty
	'''

def factor(p):
	'''
	factor : PAREN_I expression PAREN_D | fact_A1 var_cte
	'''

def fact_A1(p):
	'''
	fact_A1 : OP_SUMA | OP_RESTA | empty
	'''

def stmt(p):
	'''
	stmt : read | assign | condition | printf | return | estadistica | func_call
	'''

def tipo(p):
	'''
	INT | FLOAT | BOOL | CHAR 
	'''

def var_cte(p):
	'''
	var_cte : ID var_cte_A1 | INT_VALOR | FLOAT_VALOR 
	'''

def var_cte_A1(p):
	'''
	var_cte_A1 : BRACKET_I exp BRACKET_D | PAREN_I var_cte_A2 PAREN_D | empty
	'''

def var_cte_A2(p):
	'''
	var_cte_A2 : exp COMA var_cte_A2 | exp | empty
	'''

def exp(p):
	'''
	exp : term exp_A1
	'''

def exp_A1(p):
	'''
	exp_A1 : OP_SUMA | OP_RESTA | empty
	'''

def arr(p):
	'''
	arr : BRACKET_I INT_VALOR BRACKET_D
	'''

def term(p):
	'''
	term : factor term_A1
	'''

def term_A1(p):
	'''
	term_A1 : OP_MULT | OP_DIV | empty
	'''

def expression(p):
	'''
	expression : exp expression_A1
	'''

def expression_A1(p):
	'''
	expression_A1 : MAYOR exp | MENOR exp | MAYOR_EQ exp | MENOR_EQ exp | EQUAL exp | NOT_EQ exp | empty
	'''

def exp_cond(p):
	'''
	exp_cond : exp exp_cond_A1 
	'''

def exp_cond_A1(p):
	'''
	exp_cond_A1 : OR expression | AND expression | empty
	'''

def printf(p):
	'''
	printf : PRINT PAREN_I print_A1 PAREN_D SEMICOLON
	'''

def print_A1(p):
	'''
	print_A1 : expression | STRING_VALOR
	'''

def cond(p):
 	'''
 	cond : IF PAREN_I exp_cond PAREN_D bloque cond_A1 SEMICOLON
 	'''

def cond_A1(p):
 	'''
 	cond_A1 : ELSE bloque | empty
 	'''

def func_call(p):
 	'''
 	func_call : ID PAREN_I args PAREN_D
 	'''

def bloque(p):
 	'''
 	bloque : CURLY_I bloque_A1 CURLY_D
 	'''

def bloque_A1(p):
 	'''
 	bloque_A1 : var stmt bloque_A1 | var bloque_A1 | stmt bloque_A1 | empty
 	'''

def estadistica(p):
 	'''
 	estadistica : PROM estadistica_A1 | MODA estadistica_A1 | MEDIAN estadistica_A1 | SUM estadistica_A1 | DESVIA estadistica_A2 
 				| PEND estadistica_A2 | VARIANCE estadistica_A1 | R_SQUARE estadistica_A2 | GRAPH_BAR estadistica_A2 | GRAPH_SCATTER estadistica_A4 
 				| BINOMIAL estadistica_A3 | BERNOULLI estadistica_A2
 	'''

def estadistica_A1(p):
 	'''
 	estadistica_A1 : PAREN_I ID PAREN_D SEMICOLON
 	'''

def estadistica_A2(p):
 	'''
 	estadistica_A2 : PAREN_I ID COMA ID PAREN_D SEMICOLON
 	'''

def estadistica_A3(p):
 	'''
 	estadistica_A3 : PAREN_I ID COMA ID COMA ID PAREN_D SEMICOLON
 	'''

def estadistica_A4(p):
 	'''
 	estadistica_A4 : estadistica_A2 | estadistica_A3
 	'''
