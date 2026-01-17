from kusimutlik__module import *
import random

N=3
M=2

koik=[]
oiged=[]
valed=[]

teeb_test=[]
juba_testitud=["Mari", "Paul", "Johan"]

valik=input("Vali 1- Alusta küsimustlikku, 2- lisa uus küsimus, 3- välju.")

read=[]
kus_vas={}
kus_vas, read=andmete_lugemine_failidest(read, kus_vas)

if valik=="1":

#2 Küsimustiku läbiviimine ja Vastajate hulk
    for i in range(M):
        while True:
            nimi=input("Sisesta oma nimi: ")
    
            if nimi in juba_testitud:
                print("See kasutaja on juba testitud! Sisesta teist nime.")
            else:
                print(f"Tere, {nimi}!")
                teeb_test.append(nimi)
                break
#testimine
        punktid, sobis=testimine(kus_vas, N, nimi)
        email=nimi.replace(" ", ".")+"@example.com"
        koik.append([nimi, punktid, email])

        if sobis:
            oiged.append([nimi, punktid])
        else:
            valed.append([nimi, punktid])

#3 Failide salvestamine
    andmete_salvestamine_failidesse(koik, oiged, valed)
    print("Failid õiged.txt, valed.txt ja kõik.txt on salvestatud.")

#4 E-kirjade saatmine
    emaili_saatmine(nimi, punktid, sobis)
    print("Emaili tulemused on saadetud.")

#5 Võimalus lisada küsimusi programmi kaudu
if valik=="2":
    kusimus=input("Sisesta uus küsimus: ")
    vastus=input("Sisesta õige vastus: ")

    küsimuste_lisamine(kusimus, vastus)
    print("Uus küsimus on lisatud faili.")
    
#6 Ekraaniväljund töö lõpus
    print("Edukalt vastanud:")
    for inimene in oiged:
        print(inimene[0], "-", inimene[1], "õigesti")

    print("Tulemused saadetud e-posti aadressidele.")
    
#välju kui valik on 3
if valik=="3":
    print("Head aega!")
