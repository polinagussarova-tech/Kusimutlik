import random
read=[]
kus_vas={} #sõnastik, kus võtmed on küsimused ja väärtused vastused
testitud=[]

def andmete_lugemine_failidest(read,kus_vas):
    with open("kusimused_vastused.txt", "r", encoding="utf-8") as f:
        for rida in f:
            read.append(rida)
            
    for rida in read:
        kusimus,vastus=rida.split(":")
        kusimus=kusimus.strip()
        vastus=vastus.strip()

        kus_vas[kusimus]=vastus
    return kus_vas, read

def testimine(kus_vas,vastused,N):
    punktid=0
    kusimused=list(kus_vas.keys())
    valitud_kusimused=random.sample(kusimused, N)

    for i in range(N):
        kusimus=valitud_kusimused[i]
        oige_vastus=kus_vas[kusimus]  
        
        vastus=vastused[i]
        if vastus==oige_vastus:
            punktid+=1

    if punktid > N / 2:
        tulemus=True
    else:
        tulemus=False
        return punktid, tulemus


def andmete_salvestamine_failidesse(koik, oiged, valed):
    with open("õiged.txt", "w", encoding="utf-8") as f:
        for inimene in oiged:
            nimi=inimene[0]
            punktid=inimene[1]
            print(nimi, punktid, "õigesti", file=f)
    
    with open("valed.txt", "w", encoding="utf-8") as f:
        for inimene in valed:
            nimi=inimene[0]
            punktid=inimene[1]
            print(nimi, punktid, "õigesti", file=f)

    with open("koik.txt", "w", encoding="utf-8") as f:
        for inimene in koik:
            nimi=inimene[0]
            punktid=inimene[1]

def emaili_saatmine(nimi, punktid, sobis):
    email=nimi.replace(" ", ".") + "@example.com"

    print(f"Saadetud {email}")
    print(f"Tere, {nimi}!")
    print(f"Sinu õigete vastuste arv on {punktid}")

    if sobis:
        print("Sa sooritasid testi edukalt.")
    else:
        print("Kahjuks testi ei sooritatud edukalt.")

def küsimuste_lisamine(kusimus, vastus):
    with open("kusimused_vastused.txt", "a", encoding="utf-8") as f:
        print(f"{kusimus}:{vastus}", file=f)


