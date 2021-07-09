class Uno:
    def hazlo(self):
        print("hazlo de Uno")

    def haz_algo(self):
        self.hazlo()


class Dos(Uno):
    def hazlo(self):
        print("hazlo de Dos")


uno = Uno()
dos = Dos()

uno.haz_algo()
dos.haz_algo()

"""
hazlo de Uno
hazlo de Dos"""
