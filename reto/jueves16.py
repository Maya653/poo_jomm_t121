""""
    Nombre:johan Obed Maya Morales
    Fecha:16-Feb-2023
    Descripción: calificacion de un alimno mayor a 8
""""" 

print("Ingresa la calificacion de un alumno mayor a 8")

nombre = input("ingresa el nombre del Alumno: ")

print("el alumno se llama: ", nombre)
calificacion1 =int(input("Ingresa la calificacion: "))
calificacion2 = 8

if calificacion1 < calificacion2:
    print("Reprobado: ", calificacion1)
if calificacion1 >= calificacion2:
    print("Aprobado", "su calificacion es: ", calificacion2)
    