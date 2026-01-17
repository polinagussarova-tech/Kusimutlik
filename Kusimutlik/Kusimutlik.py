from kusimutlik__module import *
import random

N=3
M=2

koik=[]
oiged=[]
valed=[]
juba_testitud=["Mari", "Paul", "Johan"]

read=[]
kus_vas={}
kus_vas, read=andmete_lugemine_failidest(read, kus_vas)

valik=input("Vali 1- Alusta küsimustlikku, 2- lisa uus küsimus, 3- välju.)
if valik=="1":

#2 Küsimustiku läbiviimine ja Vastajate hulk
    for i in range(M):
        nimi=input("Sisesta oma nimi: ")
    
        if nimi in juba_testitud:
            print("Seda kasutaja on juba testitud!")
            break
        else:
            print(f"Tere, {nimi}!")
            testitud.append(nimi)
            vastused = []

#3 Failide salvestamine
    andmete_salvestamine_failidesse(koik, oiged, valed)
    print("Failid õiged.txt, valed.txt ja kõik.txt on salvestatud.")

#4 E-kirjade saatmine
    emaili_saatmine(nimi, punktid, sobis)
    print("Emaili tulemused on saadetud.")

#5 Võimalus lisada küsimusi programmi kaudu
if valik=="2":
    lisada_kusimus=input("Sisesta uus küsimus: ")
    
#6 Ekraaniväljund töö lõpus

#välju kui valik on 3
if valik=="3":
    print("Head aega!)
