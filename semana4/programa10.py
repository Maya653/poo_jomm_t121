""""
    Nombre: Johan Obed Maya Morales
    Fecha:9-Feb-2023
    Descripción: utilzando una funcion def y mayor
"""""
def mayor(numero1,numero2): # se utilzo un funcion(def) llamada mayor y se creo dos variables llamadas numero1 y numero2 y la funcion  hara que devuelve el mayor de los dos números
    
    result = None # se creo una variable llamada result  que tiene como valor none 
    
    if numero1 >numero2: # aqui se utiliza una condicion donde si numero1 es mayor a numero2 
       result = numero1 # se asignara  el valor de numero1
    
    elif numero2 > numero1: # si la anterior condicion anterior fue falsa entonces si numero2 es mayor a nuemro1
       result = numero2 # se pone la variable result y se asignara el valor de numero2 si la condicion fue verdadera,  y se termina el proceso  
    
    return result # Esta línea devuelve el valor de la variable "result" como resultado de la función


#Aqui se llama a la función "mayor" con diferentes argumentos y se imprime el resultado en la consola

print(mayor(1,2)) # aqui se llamo la funcion mayor donde los siguientes argumentos 1 y 2 y este imprimira el resultado 
print(mayor(2,1))#de igual manera solo que los argumentos son 2 y 1 y tras el calculo este imprimira el resultado