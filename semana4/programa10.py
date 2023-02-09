""""
    Nombre: Johan Obed Maya Morales
    Fecha:9-Feb-2023
    Descripción: utilzando def y mayor
"""""
def mayor(numero1,numero2):
    result = None
    if numero1 >numero2:
       result = numero1
    elif numero2 > numero1:
       result = numero2
    return result
print(mayor(1,2))
print(mayor(2,1))