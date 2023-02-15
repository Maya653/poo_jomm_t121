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

