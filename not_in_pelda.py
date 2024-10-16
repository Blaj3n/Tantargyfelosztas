'''
Ebben a példában a Kovács tanár már szerepel a tanarok listában,
így nem kerül újra hozzáadásra.
'''
tanarok = ["Kovács", "Nagy", "Szabó"]
uj_tanar = "Kovács"

print("1. Not in használata példa:")
if uj_tanar not in tanarok:
    tanarok.append(uj_tanar)
    print(f"{uj_tanar} hozzáadva a tanárok listájához.")
else:
    print(f"{uj_tanar} már szerepel a tanárok listájában.")

print("Tanárok listája:", tanarok)

gyumolcsok = ["alma", "banán", "alma", "eper", "banán", "körte", "alma", "eper"]

print()

print("2. Not in használata példa:")
# Üres lista az egyedi gyümölcsök tárolására
egyedi_gyumolcsok = []

# Iterálás a gyümölcsök listáján
for gyumolcs in gyumolcsok:
    # Csak akkor adjuk hozzá, ha még nincs benne
    if gyumolcs not in egyedi_gyumolcsok:
        egyedi_gyumolcsok.append(gyumolcs)

# Az egyedi gyümölcsök kiírása
print("Egyedi gyümölcsök listája:", egyedi_gyumolcsok)

'''
A kód végigmegy a gyumolcsok listán, és az egyedi_gyumolcsok listához csak akkor ad hozzá egy gyümölcsöt,
ha az még nem szerepel benne. Így biztosítja, hogy minden gyümölcs csak egyszer kerüljön a végső listába.
'''
