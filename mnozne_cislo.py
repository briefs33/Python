samohlasky = ['a', 'e', 'i', 'o', 'u']

class MnozneCislo:
    def __init__(self, mn_cislo):
        self.mn_cislo = mn_cislo

    def mnozne_cislo(self):
        dictionaires = {
            "child" : "children",
            "mouse" : "mice",
            "louse" : "lice",
            "goose" : "geese",
            "foot" : "feet",
            "tooth" : "teeth",
            "penny" : "pence",
            "ox" : "oxen"
        }
        lengh = len(self.mn_cislo)
        letters2 = ['ss', 'sh', 'ch']
        letters1 = ['s', 'x', 'o']
        letters4 = ['fe']
        letters3 = ['f']

        ## Slová v ktorých sa mení koreň slova - úplne nepravidelne
        if dictionaires.get(self.mn_cislo, "NyN") != "NyN":
            print(dictionaires.get(self.mn_cislo))

        ## man a ich zloženiny
        elif self.mn_cislo[lengh - 3 : lengh] == "man":
            print(f"{self.mn_cislo[0 : lengh - 3]}men")

        ## ! Ak slovo končí na [y], ktorému predchádza spoluhláska, mení sa [y] na [ie] teda -ies
        elif self.mn_cislo[lengh - 1] == "y":
            if not(samohlasky.count(self.mn_cislo[lengh - 2])):
                print(f"{self.mn_cislo[0 : lengh - 1]}ies")
            else:
                print(f"{self.mn_cislo}s")

        ## Koncovka -es sa používa po hláskach [s, ss, sh, ch] a [x], alebo po samohláske [o] na konci slova
        elif letters2.count(self.mn_cislo[lengh - 2 : lengh]):
            print(f"{self.mn_cislo}es")

        elif letters1.count(self.mn_cislo[lengh - 1]):
            print(f"{self.mn_cislo}es")

        ## Pri podstatných menách končiacich na spoluhlásku [f] alebo slabiku [fe] sa neznelá spoluhláska [f] mení na [v]
        elif letters4.count(self.mn_cislo[lengh - 2 : lengh]):
            print(f"{self.mn_cislo[0 : lengh - 2]}ves")

        elif letters3.count(self.mn_cislo[lengh - 1]):
            print(f"{self.mn_cislo[0 : lengh - 1]}ves")

        ## Množné číslo sa tvorí pridaním koncovky -s alebo -es za podstatné meno
        else:
            print(f"{self.mn_cislo}s")



class MnozneCisloUpravene:
    def __init__(self, mn_cislo):
        self.mn_cislo = mn_cislo

    def doit(self, array):
        array = MnozneCisloUpravene(array)
        return array

    def mnozne_cislo(self):
        dictionaires = {
            "child" : "children",
            "mouse" : "mice",
            "louse" : "lice",
            "goose" : "geese",
            "foot" : "feet",
            "tooth" : "teeth",
            "penny" : "pence",
            "ox" : "oxen"
        }
        lengh = len(self.mn_cislo)
        letters2 = ['ss', 'sh', 'ch']
        letters1 = ['s', 'x', 'o']
        letters4 = ['fe']
        letters3 = ['f']

        ## Slová v ktorých sa mení koreň slova - úplne nepravidelne
        if dictionaires.get(self.mn_cislo, "NyN") != "NyN":
            return dictionaires.get(self.mn_cislo)

        ## man a ich zloženiny
        elif self.mn_cislo[lengh - 3 : lengh] == "man":
            return self.mn_cislo[0 : lengh - 3] + "men"

        ## ! Ak slovo končí na [y], ktorému predchádza spoluhláska, mení sa [y] na [ie] teda -ies
        elif self.mn_cislo[lengh - 1] == "y":
            if not(samohlasky.count(self.mn_cislo[lengh - 2])):
                return self.mn_cislo[0 : lengh - 1] + "ies"
            else:
                return self.mn_cislo + "s"

        ## Koncovka -es sa používa po hláskach [s, ss, sh, ch] a [x], alebo po samohláske [o] na konci slova
        elif letters2.count(self.mn_cislo[lengh - 2 : lengh]) or letters1.count(self.mn_cislo[lengh - 1]):
            return self.mn_cislo + "es"

        ## Pri podstatných menách končiacich na spoluhlásku [f] alebo slabiku [fe] sa neznelá spoluhláska [f] mení na [v]
        elif letters4.count(self.mn_cislo[lengh - 2 : lengh]):
            return self.mn_cislo[0 : lengh - 2] + "ves"

        elif letters3.count(self.mn_cislo[lengh - 1]):
            return self.mn_cislo[0 : lengh - 1] + "ves"

        ## Množné číslo sa tvorí pridaním koncovky -s alebo -es za podstatné meno
        else:
            return self.mn_cislo + "s"



#class Cild(MnozneCislo):
#    print(f{self.mn_cislo}"s")

strings_s = ('house', 'hand', 'book')
strings_es = ('bus', 'touch', 'mix', 'dish', 'class', 'hero', 'cargo', 'tomato')
strings_ies = ('baby', 'city', 'story')
strings_f = ('leaf', 'calf', 'shelf', 'knife', 'wife')
strings_vynimky = ('child', 'mouse', 'louse', 'goose', 'foot', 'tooth', 'penny', 'ox')
strings_man = ('man', 'woman', 'gentleman')
strings_overit = ('boy', 'money')

#for string in strings_s:
#for string in strings_es:
#for string in strings_ies:
#for string in strings_f:
#for string in strings_vynimky:
#for string in strings_man:
#for string in strings_overit:
#    MnozneCislo(string).mnozne_cislo()


#for string in strings_s:
#for string in strings_es:
#for string in strings_ies:
for string in strings_f:
#for string in strings_vynimky:
#for string in strings_man:
#for string in strings_overit:
    print(MnozneCisloUpravene(string).mnozne_cislo())




















