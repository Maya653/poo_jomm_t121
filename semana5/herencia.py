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

# el método constructor es un método especial que se define en una clase y que se llama automáticamente cuando se crea una instancia de esa clase. 
    #El método constructor tiene el mismo nombre que la clase y se utiliza para inicializar los atributos de la clase. 
    def __init__(self): # Este es el método constructor de la clase "Persona", que se llama automáticamente cuando se crea un objeto de la clase. 
        print("Persona") #  En este caso, el método simplemente imprime la palabra "Persona" en la consola.
   
#Los métodos públicos se pueden llamar desde fuera de la clase y se utilizan para modificar o acceder a los atributos de la clase
    def setNombre(self,nombre): #el método "setNombre" toma un argumento "nombre" y lo asigna al atributo "__nombre" de la instancia de la clase
        self.__nombre = nombre #Al agregar "self" como primer argumento del método, se indica que este método opera sobre la instancia de la clase
        
class Alumno(Persona): # se creo una clase llmaada alumno que hereda atributos dela clase persona
   
    __nombre = None # se creo un atributo privado para la clase alumno
    __matricula = None #se creo u aributo privado para la clase alumno
    
    def __init__(self): # Define el constructor de la clase Alumno
        super().__init__() # Llama al constructor de la clase padre (Persona) para inicializar los atributos heredados
        print("Alumno") # Se imprime el mensaje alumno 


#una instancia es un objeto creado a partir de una clase.

objeto_persona=Persona() #Crea una instancia de la clase Persona y la asigna a la variable objeto_persona
objeto_alumno=Alumno()# se crea una intancia de la clase alumno y se le asigna a ala variable objeto_alumno

#La función dir() toma un objeto como argumento y devuelve una lista de los nombres de los atributos y métodos disponibles en ese objeto.
print(dir(objeto_persona)) #muestra todos los atributos y metodos del objeto objeto_persona, incluyendo los atributos y métodos heredados de la clase object
print(dir(objeto_alumno)) #del objeto objeto_alumno, incluyendo los atributos y métodos heredados de la clase Persona, la clase object y la propia clase Alumno

