""""
  Nombre: Johan Obed MM
  Fecha: 24/01/2023
  Descripción:
"""""
print("calcular e imprimir el área y perímetro del Cículo y el cuadrado") #se va imprimir el texto del tema

PI=3.1416 #este es el valor de pi
radio=float(input("ingresa el valor de radio:"))#tine que pedir el valor de radio

perimetro= 2* PI*radio #se ingrea la formula del perimetro
area= PI*radio**2 # se ingresa la formula del área 

print("El perimetro de un circulo {} de radio es {}:".format(radio, perimetro)) #se va a imprimir el resultado del perimetro poniendo
print("El area de un círculo de {} de radioes:".format(radio,area)) #se va imprimir el resultado del area
      