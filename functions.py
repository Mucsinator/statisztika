from data import *


def Fajlbeolvasas():
    f=open("fob2016.txt", "r", encoding="utf-8")
    for sor in f:
        Versenyzok.append(Versenyzo(sor))
    f.close()
    
    
    
def NoiVersenyzok():
    noiDB=0
    for item in Versenyzok:
        if item.Kategoria=="Noi":
            noiDB+=1
    return noiDB/len(Versenyzok)*100

def Noibajnok():
    bajnokPoz=0
    for i in range(len(Versenyzok)):
        if Versenyzok[i].Kategoria=="Noi" and Versenyzok[i].Osszpont()>Versenyzok[bajnokPoz].Osszpont():
            bajnokPoz=i
    return bajnokPoz

def Ferfipontok():
    f=open("osszpontFF.txt", "w",encoding="utf-8")
    for item in Versenyzok:
        if item .Kategoria=="Felnott ferfi":
            f.write(f"{item.Nev};{item.Osszpont()}\n")
    f.close()
    
def Statisztika():
    stat={}
    for item in Versenyzok:
        if item.Egyesulet!="n.a.":
            if item.Egyesulet in stat.keys():
                stat[item.Egyesulet]+=1
            else:
                stat[item.Egyesulet]=1
    
    #Képernyőre:
    for key, value in stat.items():
        if value>2:
            print(f"{key} - {value}")
        
    #Fájlba:
    f=open("statisztika.txt", "w", encoding="utf-8")
    for key, value in stat.items():
        if value>2:
            f.write(f"{key} - {value}\n")
    f.close