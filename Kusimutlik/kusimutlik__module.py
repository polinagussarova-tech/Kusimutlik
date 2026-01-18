import random
kus_vas={} #sõnastik, kus võtmed on küsimused ja väärtused vastused

def andmete_lugemine_failidest(kus_vas):    
    with open("kusimused_vastused.txt", "r", encoding="utf-8") as f:
        for rida in f:
            if rida.strip() !="":
                kusimus, vastus=rida.split(":")
                kus_vas[kusimus.strip()]=vastus.strip()
    return kus_vas

def testimine(kus_vas,N, nimi):
    punktid=0
    kusimused=random.sample(list(kus_vas.keys()), N)

    for kusimus in kusimused:
        vastus=input(f"{nimi}, {kusimus}").strip()
        if vastus==kus_vas[kusimus]:
            punktid+=1

    sobis=punktid > N/2
    return punktid, sobis


def andmete_salvestamine_failidesse(koik, oiged, valed):
    oiged.sort(key=lambda inimene: inimene["punktid"], reverse=True)
    valed.sort(key=lambda inimene: inimene["nimi"])

    with open("oiged.txt", "w", encoding="utf-8") as f:
        for inimene in oiged:
            print(inimene["nimi"], "-", inimene["punktid"], "oigesti", file=f)

    with open("valed.txt", "w", encoding="utf-8") as f:
        for inimene in valed:
            print(inimene["nimi"], "-", inimene["punktid"], "valesti", file=f)

    with open("koik.txt", "w", encoding="utf-8") as f:
        for inimene in koik:
            print(inimene["nimi"], "-", inimene["punktid"], "-", inimene["email"], file=f)

    
def emaili_saatmine(nimi, punktid, sobis):
    email=nimi.lower().replace(" ", ".") + "@example.com"

    print(f"Saadetud:{email}")
    print(f"Tere, {nimi}!")
    print(f"Sinu õigete vastuste arv on: {punktid}")

    if sobis:
        print("Sa sooritasid testi edukalt.")
    else:
        print("Kahjuks testi ei sooritatud edukalt.")

def raport_tooandjale(koik):
    print("Saadetud: tootaja@firma.ee")
    print("Tere!")
    print("Tänased küsimustiku tulemused:")
    
    koik.sort(key=lambda inimene: inimene["punktid"], reverse=True)
    parim=koik[0]

def küsimuste_lisamine(kusimus, vastus):
    with open("kusimused_vastused.txt", "a", encoding="utf-8") as f:
        print(f"{kusimus}:{vastus}", file=f)
