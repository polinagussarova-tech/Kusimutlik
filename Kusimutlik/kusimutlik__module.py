import random
read=[]
kus_vas={} #sõnastik, kus võtmed on küsimused ja väärtused vastused
testitud=[]
nimed=["Mati", "Mari", "Augustina"]

def andmete_lugemine_failidest(read,kus_vas):
    with open("kusimused_vastused.txt", "r") as f:
        for rida in f:
            read.append(rida)
        
    for rida in read:
        kusimus,vastus=rida.split(':')
        kus_vas[kusimus.strip()]=vastus.strip()
    return kus_vas,read

# sõnastik={"A":"a"}
# loend=["A"]

def testimine(kus_vas,vastused,N):
    punktid=0

    kusimused=list(kus_vas.keys())
    indeksid=random.sample(range(len(kusimused)), N)

    for i in range(N):

        vastus_kasutajalt=vastused[i].lower()

        
        kusimus=kusimused[indeksid[i]]

        oige_vastus=kus_vas[kusimus].lower()

        if vastus_kasutajalt==oige_vastus:
            punktid+=1

    tulemus=punktid>N/2
    return punktid,tulemus


def andmete_salvestamine_failidesse():
    pass


def emaili_saatmine(nimi, punktid, sobis):
    email = nimi.replace(" ", ".") + "@example.com"

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


