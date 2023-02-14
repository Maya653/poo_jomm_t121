class Persona:
    __nombre = None
    def __init__(self):
        print("Persona")

    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre

dejah = Persona()
dejah.setNombre("Dejah")
print(dejah.getNombre())



class Persona:
    __email = None
    __nombre = None
    def __init__(self):
        print("Persona")

    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    
    def setemail(self,email):
        self.__email = email
    def getemail(self):
        return self.__email

dejah = Persona()
dejah.setNombre("Dejah")
print(dejah.getNombre())

dejah.setemail("dejah@hotmail.com")
print(dejah.getemail())