import json


objekt_python = [
    "řetězec",                          # string
    25,                                 # int
    -3.14,                              # float
    5j,                               # complex
    ["jablko", "banán", "pomeranč"],    # list
    ("jablko", "banán", "pomeranč"),    # tupple
    range(3),                         # range
    {"jméno" : "Ján", "stáří" : 36},    # dict
    {"jablko", "banán", "pomeranč"},  # set
    frozenset({"jablko", "banán"}),   # frozenset
    True, False,                        # bool
    b"Ahoj",                          # bytes
    bytearray(5),                     # bytearray
    memoryview(bytes(5)),             # memoryview
    None]                               # NoneType

objekt_python_upr = [
    "řetězec",                          # string
    25,                                 # int
    -3.14,                              # float
    ["jablko", "banán", "pomeranč"],    # list
    ("jablko", "banán", "pomeranč"),    # tupple
    {"jméno" : "Ján", "stáří" : 36},    # dict
    True, False,                        # bool
    None]                               # NoneType




### zakódování JSON: ###

## Vypíše zakódovaný objekt JSON z celého pola Python
objekt_json = json.dumps(objekt_python_upr)
# print(objekt_json, "\n")

## Aby byl výpis čitatelný použijeme premennú indent, která zalomý řádky na stasnovený počet mezer (v témto případě dvě).
objekt_json = json.dumps(objekt_python_upr, indent = 2)
# print(objekt_json, "\n")

## Vypíše typ proměnné, objekt z objekt_python a zakódovaný objekt JSON
def detailny_vypis_Python():
    for i in objekt_python:
        print(type(i), "\u001b[32;1m", i, "\u001b[0m", end = " => ")
        try:
            print("\u001b[33m", json.dumps(i), "\u001b[0m")
        except:
            print(u"\u001b[36mÚdajový typ nelze zakódovat\u001b[0m")
            ##https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
    print()
# detailny_vypis_Python()

## Zakóduje a utřídí zoznam JSON a následne jej vypíše.
netrideny_zoznam_python = {"jablko": 2, "banán": 45, "auto": 450}
netrideny_zoznam_json = json.dumps(netrideny_zoznam_python, sort_keys=True)
# print((netriedeny_zoznam_json), "\n")


## Uložení do souboru priklad.json
# soubor = open("priklad.json", "w")
# soubor.write(objekt_json) # na výber jsou dvě proměnné objekt_json, které se ukladají do souboru rozdílne! Viz řádek 37 a 41.
# soubor.close()




### dekódování JSON: ###

## Vypíše zakódovaný objekt JSON z celého pola Python.
# print(json.loads(objekt_json), "\n")


## Vypíše typ typ dekódovaného objektu, zakódovaný objekt JSON a dekódovaný objekt.
def detailny_vypis_JSON():
    # print(objekt_json, "\n")
    for i in json.loads(objekt_json):
        print(type(i), "\u001b[33m", json.dumps(i), "\u001b[0m", "=>", "\u001b[32;1m", i, "\u001b[0m")
    print()
# detailny_vypis_JSON()

## Načtení JSON ze souboru který se dekóduje a následne vypíše.
# soubor = open("priklad.json", "r")
# print(json.loads(soubor.read()))

## Vypíše načtený soubor bez dekódování.
# print(soubor.read())
