import math
import random


"""
Kérj be 1 páros számot a felhasználótól
Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!
"""

def elsofeladat():
    szam=int(input("Kérlek adj meg egy páros számot:"))

    while szam % 2 != 0:
        print("nem páros")
        szam=int(input("Páros számot adj: "))
        if szam % 2 == 0:
            print("Helyes válasz")



"""
Írass ki a konzolra 13 db  [10, 150] zárt intervallumba eső véletlen számot. 
Hány 3-mal osztható van közöttük? A kiírás formátuma: 
„A számok között X db 3-mal osztható van!”
"""

def masodikfeladat():
    i = 0
    szamlalo = 0

    while i < 13:
        szam = math.floor(random.random() * 149 + 10)
        if szam % 3 == 0:
            szamlalo += 1
            i += 1

        print(f"A számok között {szamlalo} db 3-mal osztható szám van")
    return szamlalo


"""
Írj eljárást, mely paraméterként kap egy text szöveget, és egy N számot. 
 Amennyiben a szöveg rövidebb, mint a megadott N szám, akkor írjuk ki „Nincs N. karakter!”
Ha hosszabb, akkor a text szövegnek az N. karakterét írjuk ki csupa nagybetűvel 3-szor! 
"""

def harmadikfeladat(szam,szoveg):
    hossz=len(szoveg)
    if hossz < szam:
        print("Nincs N karakter")
    else:
        print(szoveg.upper()[szam-1]*3)


"""
Írj metódust, mely neveket kér a felhasználótól, amíg a @ jelet nem kapja.
Hány nevet adott meg a felhasználó? 
A kiírás formája: „A felhasználó 12 nevet adott meg.”

"""

def negyedikfeladat():
    szamlalo = 0
    nev = str(input("adj meg egy nevet:"))

    while nev !="@":
        nev = str(input("Adj meg egy nevet: "))
        szamlalo += 1
    print(f"A felhasznaló {szamlalo} nevet adott meg")
    return szamlalo
