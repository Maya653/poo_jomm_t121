""""
  Nombre: Johan Obed MM
  Fecha: 24/01/2023
  Descripción:
"""""
print("calcular e imprimir el área y perímetro del Cículo y el cuadrado") #se va imprimir el texto del tema
print("CIRCULO: ")#imprime la palabra ciruclo

PI=3.1416 #este es el valor de pi
radio=float(input("ingresa el valor de radio:"))#tine que pedir el valor de radio

perimetro= 2* PI*radio #se ingrea la formula del perimetro
area= PI* radio**2 # se ingresa la formula del área 

print("El perimetro de un circulo {} de radio es {}:".format(radio, perimetro)) #se va a imprimir el resultado del perimetro poniendo un (.format)
print("El area de un círculo de {} de radio es{}:".format(radio, area)) #se va imprimir el resultado del area poniendole un .format

print("CUADRADO:")#imprime la palabra cuadrado
lado1 =int(input("ingrese el valor del lado:")) #aqui se va agragar el numero de un lado1
lado2 =int(input("ingrese el valor del lado:")) #aqui se va agragar el numero de un lado2
lado3 =int(input("ingrese el valor del lado:")) #aqui se va agragar el numero de un lado3
lado4 =int(input("ingrese el valor del lado:")) #aqui se va agragar el numero de un lado4

perimetro = lado1+lado2+lado3+lado4 #ponemos la formulita
area = lado1*lado2 #igualmente su fomulita
print("EL perimetro de un cuadrado de lado1 es {} lado2 es {} lado3 es {} es lado4 es {} su perimetro es:{}:".format(lado1,lado2,lado3,lado4, perimetro)) #me tarde como 20 min pa encontrar mi error pero ya se pudo, solamente era dejarle un espacio al perimetro y al area
print("el area de un cuadrado de lado1 es {} lado2 es {} su area es:{}.".format(lado1,lado2, area))# igualmente 


      