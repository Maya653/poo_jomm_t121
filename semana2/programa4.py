""""
  Nombre: Johan Obed MM
  Fecha: 25/01/2023
  Descripción: imprimiendo dos variables de diferentes formas
"""""

numero1=10 #creando un variable con con el valor de 10
numero2=5 # creando un variable con el valor de 5

print("{}+{}={}".format(numero1,numero2,numero1+numero2)) # se mostrará primero la suma de las variables numero1 y numero2, seguida por la cadena de texto que muestra la expresión matemática de la suma y su resultado de estos dos 

print("{n1}+{n2}={suma}".format(n1=numero1,n2=numero2,suma=numero1+numero2)) # se imprimira lo mismo que en la anteriror con la diferencia de su estructura, se puso valores en las etiquetas n1 + n2 = suma y con el format se le asignan los valores de la etiquetas a los marcadores 

print("{n2}+{n2}={n2}".format(n1=numero1,n2=numero2,suma=numero1+numero2))   #es lo mismo que en lo anterior noma que cambian los valores de las variables

print("{numero1}+{numero2}={suma}".format(numero1=numero1,numero2=numero2,suma=numero1+numero2)) # se imprimira lo mismo que la linea 12 solo que cambian los valores de lugar n1 ahora es numero1 solo cambia el texto

