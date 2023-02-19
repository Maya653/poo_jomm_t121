""""
  Nombre: Johan Obed MM
  Fecha: 24/01/2023
  Descripción: 
"""""
print("Cálculo del área y perímetro de un triángulo")  #imprima el titulo de lo que se va hacer

base = float(input("Ingrese la base: ")) # se creo una variable llamada base que es de tipo float y pedira que ingrese un valor
altura = float(input("Ingrese la altura: ")) # se creo una variable de tipo float que pida la altura 
lado1 = float(input("Ingrese el primer lado: ")) # se creo una variable de tipo decimal que pida que ingrese un nuemero 
lado2 = float(input("Ingrese el segundo lado: ")) # se creo una varible de tipo decimal que pida un numero de lado2
lado3 = float(input("Ingrese el tercer lado: ")) # se creo una varible de tipo decimal que pida un numero para el lado3

area = (base * altura) / 2 # se creo una variable  que realice la operacion del area 

perimetro = lado1 + lado2 + lado3 # se creo la varible que pida el perimetro de todos los lados 


print("Área:", area) # imprimira el  resultado de la varible area
print("Perímetro:", perimetro) # imprimira el resultado de la variable perimetro
