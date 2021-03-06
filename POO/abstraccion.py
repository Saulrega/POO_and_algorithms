
class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='fria'):
        self._llenar_tanque_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()


    def _llenar_tanque_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print("Anadiendo jabon")


    def _lavar(self):
        print("lavando la ropa")

    def _centrifugar(self):
        print("Centrifugando la ropa")


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()