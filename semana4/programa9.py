""""
    Nombre: Johan Obed Maya Morales
    Fecha: 7-Feb-2023
    Descripción: diferentes formas de crear el programa8.py
"""""
numero1=int(input("ingresa el valor1: ")) # se creeo una variable de tipo entero que pida que ingrese un numero
numero2=int(input("ingresa el valor2:"))# se creo otra variable de tipo entero que pida que ingrese un numero
   
#SOLUCCIÓN 1
if numero1 > numero2:   #se puso una condicion que si numero1 es mayor que nuemro2
    print(numero1)  # se imprimira el numero1
if numero2 > numero1:  #se puso una condicion que ai numero2 es mayor que numero1
    print(numero2)  # se imprimira el numero2
if numero1 == numero2: # se puso una condicion que si numero1 es igual a numero2
    print(None) # se imprimira None (nulo)

#SOLUCCIÓN 2
if numero2 > numero1:
    print(numero2)
if numero1 > numero2:
    print(numero1)
else:
    print(None)
    
    #Solucción 3:
if numero1 > numero2: # se puso una condicion donde si nuemero1 es mayor que numero2
    print(numero1)  # si la condicion de cumple imprimira el resultado de numero1
elif numero2 > numero1: #si la condicion anterior fue falsa entonces se condicionar la siguente condicion donde si numero2 es mayot que numero1
    print(numero2) # si la condicion fue verdadera imprimira el resultado de numero2 y este automaticamente termina 
else: # si ninguna de las anteriores fue verdadera imprimira None
    print(None) # imprimira el resultado None

    #Solucción:4
if numero1 == numero2: # se puso una condicion donde si numero1 es igual a numero2
    print(None) #imprimira None si es verdadero
elif numero1 > numero2: # si el resultado anterior fue falso entonces la siguiente condicion es: si numero1 es mayor a numero2 
    print(numero1) # si fue verdadera imprimira el resultado de numero1 y automaticamente se termina
elif numero2 > numero1: # sino numero2 es mayor a numero 1 
    print(numero2) #imprimira el resultado de numero2
    
    #Solucción 5
if numero1 <numero2: # la siguiente condicion de numero1 es menor que numero2
	print(numero2) #imprimira  el resultado de numero2 si es verdadero
if numero2 <numero1: # si la anterior condicion fue falsa entonces si numero2 es menor a numero1 
	print(numero1) #imprimira numero1 si fue verdadera 
if numero1 == numero2: # si la condicion anterior entonces si numero1 es igual a numero2
	print(None) # imprimira NOne

    #Solucción 6
if numero2 > numero1: # si la condicion  numero2 es mayor a numero1 
	print(numero2) # imprimira el resultado de numero2 si fue verdadera
if numero2 < numero1: # si la la condicion anterior fue falsa entonces, si numero2 en menor a numero1
	print(numero1) #imprime el resultado de numero1
else: # sino las siguientes condiciones anteriores fueron falsas entonces
	print(None) # imprima None

    #Solucción 7 
if(numero2 < numero1 > numero2): # si la siguiente condicion de numero2 es menor a numero1 y mayor a numero2 
	print (numero1) #imprime el resultado de numero1
elif(numero1 < numero2 > numero1): # si el resultaado anterior fue falso entonces si numero1 es menor numero2 pero si es mayor a numero1 
	print(numero2) # imprimira el resultado de numero2 y terminara automaticamente
else: #si las anteriores condiciones fuero falsas entonces
	print(None) #imprimira none


