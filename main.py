from functions import *

Fajlbeolvasas()
print(f"3.feladat: Versenyzők száma: {len(Versenyzok)}")


NoiVersenyzok()
print(f"4. feladat: A női versenyzők aránya: {round(NoiVersenyzok(),2)}%")

print(f"6. feladat: A bajnok női versenyző")
print(f"\tNév: {Versenyzok[Noibajnok()].Nev}")
print(f"\tEgyesület: {Versenyzok[Noibajnok()].Egyesulet}")
print(f"\tÖsszpont: {Versenyzok[Noibajnok()].Osszpont()}")


Ferfipontok()


print("8. feladat: Egyesölet statisztika")
Statisztika()