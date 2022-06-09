class Person:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):

        print("Ando caminando")


class Ciclista(Person):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        
        print("Ando moviendome en mi bicicleta")


def main():
    persona = Person("Saul")
    persona.avanza()

    ciclista = Ciclista("Juan")
    ciclista.avanza()

if __name__ == '__main__':
    main()