"""""
Nombre: JOhan Obed Maya Morales
Fecha: 22 feb 2023
descripcion: par impar y nulo
"""""
numero = int(input("Introduce un número entero: ")) #qUE Se ingrese una variable llamada numero y que imprima un valor entero

if numero == 0: # si numero es igual a cero 
    print("El número es nulo.") #imprimira que es nulo
elif numero % 2 == 0: # si anteriormente fue falso entonces cheqcara si es entero
    print("El número es par.") # imprimira entero
else:
    print("El número es impar.")# si ninguno fue verdadero entonces imprimira impar
