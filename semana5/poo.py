""""
Descripcion:  

"""""
class Persona:
    __nombre = None
    __edad = None
    def __init__(self):
        print("Persona")
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre 
        
class Alumno(Persona):
   
    __nombre = None
    __matricula = None
    
    def __init__(self):
        super().__init__()
        print("Alumno")

    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    
    def setMatricula(self,matricula):
        self.__matricula = matricula
    def getMatricula(self):
        return self.__matricula
        
class Coordinador(Persona):
    
    __no_nomina = None
    __carrera_a_cargo = None
    
    def __init__(self):
        super().__init__()
        print("Coordinador")
    def setNO_nomina(self,no_nomina):
        self.__no_nomina = no_nomina
    def getNo_nomina(self):
        return self.__no_nomina

    def setCarrera_a_cargo(self,carrera_a_cargo):
        self.__carrera_a_cargo = carrera_a_cargo
    def getCarrera_a_cargo(self):
        return self.__carrera_a_cargo


class Profesor():
    __no_nomina = None
    def __init__(self):
        super().__init__()
        print("Profesor")
    
    def setNO_nomina(self,no_nomina):
        self.__no_nomina = no_nomina
    def getNo_nomina(self):
        return self.__no_nomina
    
objeto_persona=Persona()
objeto_alumno=Alumno()
objeto_coordinador=Coordinador()
objeto_profesor=Profesor()

print(dir(objeto_persona))
print(dir(objeto_alumno))
print(dir(objeto_coordinador))
print(dir(objeto_profesor))