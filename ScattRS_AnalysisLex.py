#Lenguaje ScattRS
#Analizador Lexico V1.0
#11/03/2019

import ply.lex as lex
import sys

#Lista de Tokens del lenguaje
tokens = [
	'OP_SUMA', 
	'OP_RESTA', 
	'OP_MULT', 
	'OP_DIV', 
	'PAREN_I', 
	'PAREN_D', 
	'SEMICOLON', 
	'COMA', 
	'CURLY_I', 
	'CURLY_D', 
	'BRACKET_I', 
	'BRACKET_D', 
	'EQUAL', 
	'MENOR_EQ', 
	'MAYOR_EQ', 
	'MENOR', 
	'MAYOR', 
	'NOT_EQ',
	'ASSIGN', 
	'ID', 
	'INT_VALOR', 
	'FLOAT_VALOR', 
	'CHAR_VALOR', 
	'STRING_VALOR',
	'COLON'
	]

#Palabras reservadas = 'lexema' : 'token'
p_reservadas = {
	'programa': 'PROGRAM',
	'funcion': 'FUNC',
	'var': 'PARAMS',
	'retornar': 'RETURN',
	'int': 'INT',
	'float': 'FLOAT',
	'bool': 'BOOL',
	'char': 'CHAR',
	'void': 'VOID',
	'SI': 'IF',
	'SI_NO': 'ELSE',
	'Y': 'AND',
	'O': 'OR',
	'inicio': 'MAIN',
	'verdadero': 'TRUE',
	'falso': 'FALSE',
	'leer' : 'READ',
	#funciones especiales del lenguaje
	'pend': 'PEND',
	'suma': 'SUM',
	'desv': 'DESVIA',
	'media': 'PROM',
	'moda': 'MODA',
	'mediana': 'MEDIAN',
	'varianza': 'VARIANCE',
	'r_cuad': 'R_SQUARE',
	'graf_barra': 'GRAPH_BAR',
	'graf_scatter': 'GRAPH_SCATTER',
	'binomial': 'BINOMIAL',
	'bernoulli': 'BERNOULLI',
	'limpiar': 'ERASE',
	'imprimir': 'PRINT',
	'mientras': 'WHILE'
}

#Union de los tokens de las palabras reservadas y tokens de operadores
tokens = tokens + list(p_reservadas.values())

#Expresiones regulares de los tokens
t_OP_SUMA = r'\+'
t_OP_RESTA = r'\-'
t_OP_MULT = r'\*'
t_OP_DIV = r'/'
t_PAREN_I = r'\('
t_PAREN_D = r'\)'
t_SEMICOLON = r';'
t_COMA = r','
t_CURLY_I = r'\{'
t_CURLY_D = r'\}'
t_BRACKET_I = r'\['
t_BRACKET_D = r'\]'
t_EQUAL = r'=='
t_COLON = r':'
t_MENOR = r'<'
t_MAYOR = r'>'
t_MENOR_EQ = r'<='
t_MAYOR_EQ = r'>='
t_NOT_EQ = r'!='
t_ASSIGN = r'='
t_CHAR_VALOR = r'\'.?\''
# t_STRING_VALOR = r'\".*\"'
t_STRING_VALOR = r'\"[a-zA-Z_ 0-9]+\"'
#Token para ignorar
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = p_reservadas.get(t.value, 'ID')
    return t

def t_FLOAT_VALOR(t):
    r'-?[0-9]+\.[0-9][0-9]*'
    return t
	
def t_INT_VALOR(t):
    r'-?[0-9]+'
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

#Correr el analizador lexico
scattRS_AnalysisLex = lex.lex()
scattRS_AnalysisLex.input("\"Hola\"")
while True:
    token = scattRS_AnalysisLex.token()
    if not token:
        break
    print(token)
