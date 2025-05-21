import random
jatekos = input("Kivel szeretnél játszani (emberrel/géppel)? ")
if jatekos == "géppel":
    print("Játékosok száma: 1 (Te vs Gép)")
    jatekosLap = random.randint(2, 11) + random.randint(2, 11)
    gepLap = random.randint(2, 11) + random.randint(2, 11)

    print("A te lapjaid összértéke:", jatekosLap)
    print("A gép lapjainak összértéke:", gepLap)
    if jatekosLap > 21:
        print("Sajnálom, vesztettél.")
    elif gepLap > 21:
        print("Gratulálok, nyertél!")
    elif jatekosLap > gepLap:
        print("Gratulálok, nyertél!")
    elif gepLap > jatekosLap:
        print("Sajnálom, vesztettél.")
    else:
        print("Döntetlen!")
elif jatekos == "emberrel":
    print("Játékosok száma: 2 (Játékos1 vs Játékos2)")
    jatekos1 = random.randint(2, 11) + random.randint(2, 11)
    jatekos2 = random.randint(2, 11) + random.randint(2, 11)

    print("Játékos1 lapjainak összértéke:", jatekos1)
    print("Játékos2 lapjainak összértéke:", jatekos2)

    if jatekos1 > 21 and jatekos2 > 21:
        print("Mindketten vesztettek.")
    elif jatekos1 > 21:
        print("Játékos2 nyert!")
    elif jatekos2 > 21:
        print("Játékos1 nyert!")
    elif jatekos1 > jatekos2:
        print("Játékos1 nyert!")
    elif jatekos2 > jatekos1:
        print("Játékos2 nyert!")
    else:
        print("Döntetlen!")
else:
    print("Írd be pontosan: 'emberrel' vagy 'géppel'.")
