#definir una clase

class nombreClass (): #podemos hacer referencia a alguna super claase

    def __init__(self, parametro): #aqui indicamos la creacion del objeto
        pass

    def nombreMetodo (self, parametro): #creamos metodos para los objetos
        pass


#Definicion

class Person:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return f'Hola {otra_persona}, me llamo {self.nombre}.'

#Uso

David = Person('David', 35)
Erika = Person('Erika', 32)

David.saluda(Erika)