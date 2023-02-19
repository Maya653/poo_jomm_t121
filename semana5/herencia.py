""""
Nombre: Johan Obed Maya Morales
Fecha: 
Descripcion:  se utilizo clases 

"""""

#  una clase es una plantilla para crear objetos
class Persona:  # se creo una clase llamado persona 
    
#Al agregar dos guiones bajos antes del nombre de los atributos, se indica que estos son privados y no se pueden acceder desde fuera de la clase.
    __nombre = None # Esta lnea definen un atributo privados de la clase "Persona", "__nombre"
    __edad = None # esta linea defune un atributo privado de la clase (Personaa) llamado __edad

#El método constructor tiene el mismo nombre que la clase y se utiliza para inicializar los atributos de la clase.
    def __init__(self): # Este es el método constructor de la clase "Persona", que se llama automáticamente cuando se crea un objeto de la clase. 
        print("Persona") #  En este caso, el método simplemente imprime la palabra "Persona" en la consola.
   
#Los métodos públicos se pueden llamar desde fuera de la clase y se utilizan para modificar o acceder a los atributos de la clase
    def setNombre(self,nombre): #el método "setNombre" toma un argumento "nombre" y lo asigna al atributo "__nombre" de la instancia de la clase
        self.__nombre = nombre #Al agregar "self" como primer argumento del método, se indica que este método opera sobre la instancia de la clase
        
class Alumno(Persona):
   
    __nombre = None
    __matricula = None
    
    def __init__(self):
        super().__init__()
        print("Alumno")
        
objeto_persona=Persona()
objeto_alumno=Alumno()

print(dir(objeto_persona))
print(dir(objeto_alumno))

