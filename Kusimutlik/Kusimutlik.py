from kusimutlik__module import *
import random

N=3
M=2

koik=[]
oiged=[]
valed=[]

juba_testitud=["Mari", "Paul", "Johan"]

kus_vas={}

while True:
    valik=input("Vali 1- Alusta küsimustlikku, 2- lisa uus küsimus, 3- välju: ")
    
    #2 Küsimustiku läbiviimine ja Vastajate hulk
    if valik=="1":
        kus_vas=andmete_lugemine_failidest(kus_vas)
        for i in range(M):
            while True:
                nimi=input("Sisesta oma nimi: ")
                
                if nimi in juba_testitud:
                    print("See kasutaja on juba testitud! Sisesta teist nime.")
                else:
                    print(f"Tere, {nimi}! Alustame test.")
                    juba_testitud.append(nimi)
                    break
    #3 testimine
            punktid, sobis=testimine(kus_vas, N, nimi)
            email=nimi.replace(" ", ".")+"@example.com"
                    
            vastaja={"nimi":nimi, "punktid":punktid, "email":email, "sobis":sobis}
            koik.append(vastaja)
            
            if sobis:
                oiged.append(vastaja)
            else:
                valed.append(vastaja)
            
    #4 Failide salvestamine
            andmete_salvestamine_failidesse(koik, oiged, valed)
            print("Failid õiged.txt, valed.txt ja kõik.txt on salvestatud.")
        
    #5 E-kirjade saatmine
            emaili_saatmine(nimi, punktid, sobis)
            print("Emaili tulemused on saadetud.")
            
            raport_tooandjale(koik)
            
        
    #6 Võimalus lisada küsimusi programmi kaudu
    elif valik=="2":
            kusimus=input("Sisesta uus küsimus: ")
            vastus=input("Sisesta õige vastus: ")
        
            küsimuste_lisamine(kusimus, vastus)
            print("Uus küsimus on lisatud faili.")
            
    #7 Ekraaniväljund töö lõpus
            print("Edukalt vastanud:")
            for vastaja in oiged:
                print(vastaja["nimi"], "-", vastaja["punktid"], "õigesti")
        
            print("Tulemused saadetud e-posti aadressidele.")
            
    #8 välju kui valik on 3
    elif valik=="3":
            print("Head aega!")
            break
    else:
        print("Sisesta ainult 1, 2 või 3!")
