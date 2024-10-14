# print("1. feladat ")

beolvasas = open("beosztas.txt")
beosztasok = []
for egysor in beolvasas:
    nev = egysor.strip()
    tantargy = next(beolvasas).strip()
    osztaly = next(beolvasas).strip()
    heti_oraszam = int(next(beolvasas).strip())
    beosztasok.append([nev, tantargy, osztaly, heti_oraszam])
print(beosztasok)

print("2. feladat")

print(f"A fájlban {len(beosztasok)} bejegyzés van.")

print("3. feladat")
osszes_ora = 0
for beosztas in beosztasok:
    osszes_ora += beosztas[3]
print(f"Az iskolában a heti összóraszám: {osszes_ora}")

print("4. feladat")
tanar_nev = input("Egy tanár neve= ")
oraszam = 0
for beosztas in beosztasok:
    if beosztas[0] == tanar_nev:
        oraszam += beosztas[3]
print(f"A tanár heti óraszáma: {oraszam}")

# HF: végig csinálni a 7. feladatig
