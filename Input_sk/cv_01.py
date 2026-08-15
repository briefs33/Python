class Priklad_01:
    def __init__(self):
        self.a1 = 3 ** (1/2)                # môžeme zapísať 3 ** 0.5
        self.a2 = 5 ** (1/3) / 3
        self.a3 = (1024 ** (1/5)) ** 5      # (1024 ** 0.2) ** 5
        self.a4 = (2 ** 20) ** (1/10)       # (2 ** 20) ** 0.1
    
    def out(self):
        print('a1 =', self.a1)
        print('a2 =', self.a2)
        print('a3 =', self.a3)
        print('a4 =', self.a4)
        print()

class Priklad_02:
    def __init__(self):
        self.meno = input('zadaj meno: ')
        self.vek = int(input('zadaj vek: '))
    
    def out(self):
        print(self.meno, 'má', self.vek, 'rokov')
        print(self.meno, 'bude mať o rok', self.vek + 1)
        print(self.meno, 'bude mať o 10 rokov', self.vek + 10)
        print()

class Priklad_03:
    def __init__(self):
        self.PI = 3.14159

    def kruh(self):
        self.polomer = float(input('Zadaj polomer: '))
        
        self.obvod = 2 * self.PI * self.polomer
        self.obsah = self.PI * self.polomer ** 2

        print('obvod je: ', self.obvod)
        print('obsah je: ', self.obsah)
        print()

    def kocka(self):
#        self.strana = float(input('Zadaj veľkosť strany kocky: '))

#        self.stenova_uhlopriecka = ((self.strana ** 2) + (self.strana ** 2)) ** 1/2
#        self.telesova_uhlopriecka = ((self.strana ** 2) + (self.strana ** 2)) ** 3/2

#        print('obvod je: ', self.stenova_uhlopriecka)
#        print('obsah je: ', self.telesova_uhlopriecka)
        print()

class Priklad_04:
    def __init__(self):
        self.text = input('Zadaj text: ')

    def out(self):
        for i in range(10):
            print(self.text)
        print()










class Priklad_19:
    def __init__(self):
        self.n = int(input('zadaj n: '))

    def out(self):
        for i in range(self.n):
            for j in range(3):
                for k in range(self.n):
                    print(f'{i * self.n + k + 1:2}', end=' ')
                print(end='   ')
            print()
        print()