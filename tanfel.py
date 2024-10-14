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

