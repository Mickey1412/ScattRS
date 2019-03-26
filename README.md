# ScattRS
Poryecto Final de Compiladores

El propósito de este proyecto es desarrollar un compilador para un lenguaje de programación imperativo enfocado a la enseñanza de probabilidad y estadística a nivel preparatoria en adelante, usando los fundamentos básicos de programación. El lenguaje les permitirá realizar operaciones sencillas, producir ecuaciones y desplegarlas de manera gráfica.

ScattRS es un lenguaje de programación que está basado en R con el similar objetivo de computación básica estadística y gráfica. Tiene el objetivo de desplegar el resultado de procedimientos esenciales de matematica estadistica como la moda, la media y la mediana de un set de datos utilizando funciones especiales. Igualmente el lenguaje debe utilizar datos para calcular la desviación, r cuadrada y desplegar gráficas de barras, scatter plots con su pendiente si se desea, como visualización de datos que se proporcionen.

# Funciones especiales
media(x): función que toma un arreglo de números enteros o flotantes para calcular el valor promedio del conjunto del arreglo.
mediana(x): función que toma un arreglo de números enteros o flotantes para calcular la mediana del conjunto del arreglo.
moda(x): función que toma un arreglo de números enteros o flotantes para sacar el valor con mayor frecuencia.
suma(x): función que toma un arreglo de números enteros o flotantes para realizar una sumatoria con todos los valores del arreglo.
desv(x, y): función que toma dos arreglos como entrada para calcular su valor de desviación estándar.
pendiente(x, y): función que toma dos arreglos e imprime la fórmula de la pendiente que puede utilizarse en la funcion “graf_scat”.
varianza(x): función que toma un arreglo de números enteros o flotantes para calcular el valor de la varianza.
r_cuad(x, y): función que toma dos arreglos para calcular el coeficiente de determinación o r cuadrada.
binomial(N,K,p): función que toma 3 números enteros para calcular el valor de la binomial.
bernoulli(K,P): función que toma 2 números enteros para calcular el valor de bernoulli.
graf_barra(x, y): función que toma dos arreglos para producir e imprimir en consola un diagrama de barras.
graf_scat(x, y): función que toma dos arreglos para producir e imprimir en consola un diagrama de puntos.
graf_scat(x, y, p): la funcion igualmente puede tomar un tercer parámetro que tenga una formula de la pendiente para imprimir la línea de la pendiente dentro del diagrama de puntos.

# Archivo Lexer:
ScattRS_AnalysisLex.py

# Archivo Parser:
ScattRS_AnalysisSintx.py
