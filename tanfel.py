# print("1. feladat ")

beolvasas = open("beosztas.txt")
beosztasok = []
for egysor in beolvasas:
    nev = egysor.strip()
    tantargy = next(beolvasas).strip()
    osztaly = next(beolvasas).strip()
    heti_oraszam = int(next(beolvasas).strip())
    beosztasok.append([nev, tantargy, osztaly, heti_oraszam])
# print(beosztasok)

print("2. feladat")

print(f"A fájlban {len(beosztasok)} bejegyzés van.")

print("3. feladat")
osszes_ora = 0
for beosztas in beosztasok:
    osszes_ora += beosztas[3]
print(f"Az iskolában a heti összóraszám: {osszes_ora}")

print("4. feladat")
tanar_nev = "Albatrosz Aladin"  #input("Egy tanár neve= ")
oraszam = 0
for beosztas in beosztasok:
    if beosztas[0] == tanar_nev:
        oraszam += beosztas[3]
print(f"A tanár heti óraszáma: {oraszam}")

# HF: végig csinálni a 7. feladatig

# print("5. feladat")

with open("of.txt", "w", encoding="utf-8") as fajl:
    for beosztas in beosztasok:
        if beosztas[1] == "osztalyfonoki":
            fajl.write(f"{beosztas[2]} - {beosztas[0]}\n")



# print("6. feladat")
# osztaly = input("Osztály= ")
# tantargy = input("Tantárgy= ")
# for beosztas in beosztasok:
#     if osztaly == beosztas[2] and tantargy == beosztas[1]:

print("7. feladat")
tanarok = []

for beosztas in beosztasok:
    if beosztas[0] not in tanarok:
        tanarok.append(beosztas[0])
# print(tanarok)
print(f"Az iskolában {len(tanarok)} tanár tanít.")