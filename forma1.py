"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Melyik versenyző nyerte a legkevesebb futamot?
4. Ki teljesítette a legtöbb futamot?
5. Átlagosan hány futamot teljesítettek a versenyzők?"

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerezte a legtöbb futamgyőzelmet?

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""


# print("1. A beolvasott fájlban összesen ____ versenyző szerepel.")
# print("2. A legtöbb futamot nyert versenyző: ____")
# print("3. A legkevesebb futamot nyert versenyző: ____")
# print("4. A legtöbb futamot teljesített versenyző: ____")
# print("5. Az átlagos futamszám: ____")
# print("***A legtöbb futamgyőzelmet szerző csapat: ____")

versenyzok = []
with open(r'beolvasando_adatok\f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    #Név; Csapat; Győzelmek száma; Teljesített futamok száma
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nev = adatok[0]
        csapat = adatok[1]
        gyoz_szam = int(adatok[2])
        telj_fut = int(adatok[3])
        versenyzo = {'nev': nev, 'csapat': csapat, 'gyozelmek szama': gyoz_szam, 'teljesitett futamok': telj_fut}
        versenyzok.append(versenyzo)

# print(f'{versenyzok=}')

# 1. feladat
print(f"1. A beolvasott fájlban összesen {len(versenyzok)} versenyző szerepel.")


# 2. feladat
legtobb_gy = 0
for ver in versenyzok:
    if ver['gyozelmek szama'] > legtobb_gy:
        legtobb_gy = ver['gyozelmek szama']
        ver_nev = ver['nev']
print(f"2. A legtöbb futamot nyert versenyző: {ver_nev}")


# 3. feladat
legkev_gy = 1111
for ver in versenyzok:
    if ver['gyozelmek szama'] < legkev_gy:
        legkev_gy = ver['gyozelmek szama']
        ver_nev = ver['nev']
print(f"3. A legkevesebb futamot nyert versenyző: {ver_nev}")


# 4. feladat
legtobb_f = 0
for fut in versenyzok:
    if fut['teljesitett futamok'] > legtobb_f:
        legtobb_f = fut['teljesitett futamok']
        fut_nev = fut['nev']
print(f"4. A legtöbb futamot teljesített versenyző: {fut_nev}")


# 5. feladat

# print(f"5. Az átlagos futamszám: {round(sum(i['teljesitett futamok'] for i in versenyzok) / len(versenyzok), 2)}")

atlag = sum(i['teljesitett futamok'] for i in versenyzok) / len(versenyzok)
print(f"5.Az átlagos futamszám: {round(atlag, 2)}")



# *** feladat
# legt_fut_cs = {}

# csapat = versenyzok['csapat']
# futam = versenyzok['teljesitett futam']

# print("***A legtöbb futamgyőzelmet szerző csapat: ____")
