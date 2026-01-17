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

def testimine(kus_vas,N, nimi):
    punktid=0
    kusimused=random.sample(list(kus_vas.keys()), N)

    for kusimus in kusimused:
        vastus=input(f"{nimi}, {kusimus}")
        if vastus==kus_vas[kusimus]:
            punktid+=1

    sobis=punktid > N / 2
    return punktid, sobis


def andmete_salvestamine_failidesse(koik, oiged, valed):
    oiged.sort(key=lambda x: x[1], reverse=True)
    valed.sort(key=lambda x: x[0])
    
    with open("õiged.txt", "w", encoding="utf-8") as f:
        for inimene in oiged:
            nimi=inimene[0]
            punktid=inimene[1]
            print(f"{nimi}, {punktid}, õigesti", file=f)
    
    with open("valed.txt", "w", encoding="utf-8") as f:
        for inimene in valed:
            nimi=inimene[0]
            punktid=inimene[1]
            print(f"{nimi}, {punktid}, valesti", file=f)

    with open("koik.txt", "w", encoding="utf-8") as f:
        for inimene in koik:
            nimi=inimene[0]
            punktid=inimene[1]
            email=inimene[2]
            print(nimi, punktid, email, file=f)

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


