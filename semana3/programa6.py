""""
  Nombre: Johan Obed MM
  Fecha: 24/01/2023
  Descripción: 
"""""
print("Cálculo del área y perímetro de un triángulo")

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

area = (base * altura) / 2

perimetro = lado1 + lado2 + lado3


print("Área:", area)
print("Perímetro:", perimetro)
