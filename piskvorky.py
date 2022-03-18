## Hra: Piškvorky

import sys

## Text colors:
## \033[ = Escape code, this is always the same
## 1 = Style, 1 for normal.
## 32 = Text colour, 32 for bright green.
##
## Text color
## 30   Gray
## 31	Red
## 32	Green
## 33	Yellow
## 34   Blue
## 35   Purple
## 36	Aqua
## 37   White
##
## BackGround color / White text
##      100     Gray
## 41   101 	Red
## 42	102     Green
## 43	103     Yellow
## 44   104     Blue
## 45   105     Purple
## 46	106     Aqua
## 47   107     White
##

player1 = "\033[1;31mx\033[0m"
player2 = "\033[1;32mo\033[0m"
players = [player1, player2]
player = 0
counter = range(0, 3)
i = 0
turn = 1
board = [
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
]

## získanie súradníc aktuálneho hráča
def get_input():
    print("\n\nJe na rade hráč", players[player])

    print("Zadaj stĺpec: ")
    while True:
        input_string1 = sys.stdin.readline()
        try:
            if int(input_string1) <= 2:
                break
            else:
                print("Neplatný stĺpec, skús ešteraz: ")
        except Exception as e:
            print("Neplatný stĺpec, skús ešteraz: ")
    print("Zadaj riadok: ")
    while True:
        input_string2 = sys.stdin.readline()
        try:
            if int(input_string2) <= 2:
                break
            else:
                print("Neplatný riadok, skús ešteraz: ")
        except Exception as e:
            print("Neplatný riadok, skús ešteraz: ")
    print()
    return int(input_string1), int(input_string2)

## vykreslenie hracieho poľa
def gameboard():
    print("   ", end = "")
    for count in counter:
        print(count, end = " ")
    for count in counter:
        print("\n", count, end = " ")
        for letter1 in board[count]:
            print(letter1, end = " ")

## výmena hráčov
def player_select(player):
    if player == 0:
        player = 1
    else:
        player = 0
    return player

## vypísanie čísla kola
print("\033[1;33mVitajte v kole\033[1;0m", turn)

## hlavná slučka hry
while turn < 9:
    ## vykreslenie hracieho poľa
    gameboard()

    ## zakreslenie symbolu hráča podľa zadaných súradníc
    number1, number2 = get_input()
    if(board[number2][number1] == "_"):
        board[number2][number1] = players[player]
    else:
        print("Miesto už obsadil hráč:", board[number2][number1])
        continue

    ## vyhodnotenie hracieho poľa pre aktuálneho hráča
    if board[0][0] == players[player] and board[0][1] == players[player] and board[0][2] == players[player]:
        print("0:-", "Vyhral hráč", players[player])
        break
    elif board[1][0] == players[player] and board[1][1] == players[player] and board[1][2] == players[player]:
        print("1:-", "Vyhral hráč", players[player])
        break
    elif board[2][0] == players[player] and board[2][1] == players[player] and board[2][2] == players[player]:
        print("2:-", "Vyhral hráč", players[player])
        break
    elif board[0][0] == players[player] and board[1][0] == players[player] and board[2][0] == players[player]:
        print("0:|", "Vyhral hráč", players[player])
        break
    elif board[0][1] == players[player] and board[1][1] == players[player] and board[2][1] == players[player]:
        print("1:|", "Vyhral hráč", players[player])
        break
    elif board[0][2] == players[player] and board[1][2] == players[player] and board[2][2] == players[player]:
        print("2:|", "Vyhral hráč", players[player])
        break
    elif board[0][0] == players[player] and board[1][1] == players[player] and board[2][2] == players[player]:
        print("D:\\", "Vyhral hráč", players[player])
        break
    elif board[0][2] == players[player] and board[1][1] == players[player] and board[2][0] == players[player]:
        print("D:/", "Vyhral hráč", players[player])
        break
    elif board[0].count("_") == 0 and board[1].count("_") == 0 and board[2].count("_") == 0:
        print("R::", "Remíza")
        break
    else:
        ## výmena hráčov
#        player = player_select(player)
        player = (1 + player) % 2

        i += 1
        if i % 2 == 0:
            turn += 1

            ## vypísanie čísla kola
            print("\033[1;33mVitajte v kole\033[1;0m", turn)

## vykreslenie hracieho poľa a ukončenie hry
gameboard()
print("\n\033[1;36mKoniec hry!\033[1;0m")
