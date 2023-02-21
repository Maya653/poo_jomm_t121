""""Nombre: johan Obed Maya Morales
Descripcion: clasese herencia y objetos
Fecha: 15-Feb-2023

"""""
class Persona: #se crea una clase que se llama Persona
  
    __nombre = None #se asigno un atributo privado de la clase Persona, llamado __nombre
    __edad = None # se asigno un atributo privado de la clase Pesona , llamado __edad 
   
    def __init__(self): #esta linea es un metodo que llama automaticamente cada vez que se crea un objeto
        print("Persona") # y cada vez que se crea un objeto imprimira la cadena de texto Persona
    
    def setNombre(self,nombre):# esta define un metodo llamado setNombre que utilza para establecer el nombre de una persona
        self.__nombre = nombre #cuando se llama al método setNombre con un valor nombre, el valor de la variable privada __nombre se establece en ese valor
        
    def getNombre(self): #esta linea define otro metodo llamado getNombre, que se utiliza para obtener el nombre de una persona
        #que es un parametro: son los valores que se pasan a una función o método para que los use durante su ejecución.
        return self.__nombre #entoces el método no toma ningún parámetro y simplemente devuelve el valor de la variable privada __nombre.
        
class Alumno(Persona): # se creo una clase llamada Alumno, que hereada atribudos de la clase Persona
   
    __nombre = None # se asigino un atributo privado de la clase Alumno llamado __nombre
    __matricula = None # se asigno un atributo privado de la clase Alumno llamdo __matricula
    
    def __init__(self):# Esta línea define el constructor de la clase Alumno
        super().__init__() # El constructor llama al constructor de la clase base (Persona) usando la función super()
        print("Alumno") # e imprimira la cadena de texto Alumno

    def setNombre(self,nombre): # de define un metodo llamado setNombre que se utilza para estalbecer el nombre del alumno
        self.__nombre = nombre #  El método toma un parámetro llamado nombre y establece el valor de la variable privada __nombre en ese valor
    def getNombre(self): # se define un metodo llamado getNombre que se utiliza para obtener el nombre de un alumno
        return self.__nombre #El método no toma ningún parámetro y simplemente devuelve el valor de la variable privada __nombre
    
    def setMatricula(self,matricula):# se define un metodo llamado setMatricula que se utilza para establecer la matricula del alumno
        self.__matricula = matricula #El método toma un parámetro llamado matricula y establece el valor de la variable privada __matricula en ese valor
    def getMatricula(self):# se define un metodo llamado getMatricula que se utiliza para obtener la matrícula de un alumno
        return self.__matricula #el metodo no tomara ningun parametro y solamente devuelve el valor de la variable privad __matricula
        
class Coordinador(Persona): #se creo una clase llamada Coordinador que hereda los atributos de la clase Persona
    
    __no_nomina = None # se asigno un atributo privado de la clase Coordinador llamdo __no_nomina
    __carrera_a_cargo = None #se asigno un atributo privado de la clase Coordinador llamado __carrera_a_cargo
    
    def __init__(self): #se definio un metodo que llama automaticamente cada vez que se crea un objeto
        super().__init__() # este contrutor invoca de la clase madre(Persona)
        print("Coordinador") #e imprimira la cadena de texto Coordinador
   
    def setNO_nomina(self,no_nomina):# se definio un metodo llamado setNo_nomina que se utiliza para establecer el no_de _nomina del Coordinador
        self.__no_nomina = no_nomina # el metodo toma un parametro llamado no_nomina y establece el valor de la variable privada __no_nomina en ese valor
   
    def getNo_nomina(self):  #se define un metodo llamado getNo_nomima que se utiliza para obtener el No_nomina del coordinador
        return self.__no_nomina#el metodo no tomara ninugn pararametro y solamente vuelve el valor de la variable que esta privada "__no_nomina"

    def setCarrera_a_cargo(self,carrera_a_cargo): #se define un metodo llamado setCarrera_a_cargo que se utilza para establecer la carrera_a_cargo del Coordinador
        self.__carrera_a_cargo = carrera_a_cargo #el metodo toma un parametro llamado carrera_a_cargo y establece el valor de la variable privada __carrera_a_cargo en ese valor
    def getCarrera_a_cargo(self): # se define un metodo llamado getCarrera_a_cargo  que se utilza para obtener la carrera a cargo del Coordinador
        return self.__carrera_a_cargo # el metodo no tomara ningun paramatro y va a regresar el valor de la variable que esta en privad __carrera_a_cargo


class Profesor(Persona):#se creo una clase llamada pRofesor que hereda los atributod de la clase Persona
    __no_nomina = None # se asigno un atributo privado llamado __no_nomina para la clase Profesor
    def __init__(self): # se definio un metodo que llamara automaticamente cuando se crea un objeto
        super().__init__() # el contructor llama al contructor de la clase madre(Persona)
        print("Profesor") #e imprimira la cadena de texto Profesor
    
    def setNO_nomina(self,no_nomina):# se definio un metodo llamado setNo_nomina que se utiliza para establecer el no_de _nomina del Profesor
        self.__no_nomina = no_nomina # el metodo toma un parametro llamado no_nomina y establece el valor de la variable privada __no_nomina en ese valor
   
    def getNo_nomina(self):  #se define un metodo llamado getNo_nomima que se utiliza para obtener el No_nomina del Profesor
        return self.__no_nomina#el metodo no tomara ninugn pararametro y solamente vuelve el valor de la variable que esta privada "__no_nomina"
    
objeto_persona=Persona() # crea una instancia de la clase Persona y la asigna a la variable objeto_persona
objeto_alumno=Alumno() #crea un objeto de la clase Alumno y le adigna a la variable objeto_alumno 
objeto_coordinador=Coordinador()#crea un objeto de la clase Coordiandor y le asigna a la variable objeto_coordinador
objeto_profesor=Profesor()# crea un objeto de la clase Profesor y le asigna a a la varaible objeto_profesor

print(dir(objeto_persona))#imprime una lista de todos los atributos y metodos de la clase Persona y su instancia objeto_persona
print(dir(objeto_alumno))#imprime una lista de todos los atributos y metodos de la clase Alumno y su instancia objeto_alumno
print(dir(objeto_coordinador)) #imprime una lista de todos los atributos y metodos disponilbes en la clase coordinador y su instancia objeto_coordinador
print(dir(objeto_profesor)) # imprime una lista de todos los atributos y métodos disponibles en la clase Profesor y en su instancia objeto_profesor.