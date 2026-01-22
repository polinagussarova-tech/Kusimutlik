import random
import smtplib, ssl
from email.message import EmailMessage

kus_vas={} #sõnastik, kus võtmed on küsimused ja väärtused vastused

def andmete_lugemine_failidest(kus_vas):    
    with open("kusimused_vastused.txt", "r", encoding="utf-8") as f:
        for rida in f:
            rida=rida.strip()
            kusimus, vastus=rida.split(":")
            kus_vas[kusimus]=vastus #вместо keys ставим kusimus  словарь[КЛЮЧ] = ЗНАЧЕНИЕ Она делает в словаре запись:
    return kus_vas

def testimine(kus_vas,N, nimi):
    punktid=0
    
    if N>len(kus_vas):
        N=len(kus_vas)
    koik_kusimused=list(kus_vas.keys())
    kusimused=random.sample(koik_kusimused, N)

    for kusimus in kusimused:
        vastus=input(f"{nimi}, {kusimus}")
        if vastus==kus_vas[kusimus]:
            punktid+=1

    sobis=punktid > N/2 #возвращает true false 
    return punktid, sobis


def andmete_salvestamine_failidesse(koik, oiged, valed):
    oiged.sort(key=lambda vastaja: vastaja["punktid"], reverse=True)
    valed.sort(key=lambda vastaja: vastaja["nimi"])

    with open("oiged.txt", "w", encoding="utf-8") as f:
        for vastaja in oiged:
            print(vastaja["nimi"], "-", vastaja["punktid"], "oigesti", file=f)

    with open("valed.txt", "w", encoding="utf-8") as f:
        for vastaja in valed:
            print(vastaja["nimi"], "-", vastaja["punktid"], "valesti", file=f)

    with open("koik.txt", "w", encoding="utf-8") as f:
        for vastaja in koik:
            print(vastaja["nimi"], "-", vastaja["punktid"], "-", vastaja["email"], file=f)

    
def emaili_saatmine(nimi, punktid, sobis):

    saaja_email=nimi.lower().replace(" ", ".") + "@example.com"

    saatja_email="polina.gussarova@gmail.com"
    parool=input("Sisesta rakenduse parool: ")
    #ccyw hvxt nurc bqis

    teema="Küsimustiku tulemused"

    if sobis:
        tulemus="Sa sooritasid testi edukalt."
    else:
        tulemus="Kahjuks testi ei sooritatud edukalt."

    tekst=(f"Tere {nimi}!")
    tekst=(f"Tere {nimi}!")
    tekst=(f"Sinu õigete vastuste arv: {punktid}")
    tekst=(f"{tulemus}")
    tekst=(f"Lugupidamisega")
    tekst=(f"Küsimustiku Automaatprogramm")

    smtp_server="smtp.gmail.com"
    port=587
    context=ssl.create_default_context()

    msg=EmailMessage()
    msg["Subject"]=teema
    msg["From"]=saatja_email
    msg["To"]=saaja_email
    msg.set_content(tekst)

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(saatja_email, parool)
        server.send_message(msg)

        print(f"E-kiri saadetud:{saaja_email}")

def raport_tooandjale(koik):
    print("Saadetud: tootaja@firma.ee")
    print("Tere!")
    print("Tänased küsimustiku tulemused:")
    
    koik.sort(key=lambda vastaja: vastaja["punktid"], reverse=True)

    nr=1
    for vastaja in koik:
        if vastaja["sobis"]:
            staatus="SOBIS"
        else:
            staatus="EI SOBINUD"

        print(nr, ".", vastaja["nimi"], "–", vastaja["punktid"], "õigesti –",vastaja["email"], "–", staatus)
        nr+=1

    parim=koik[0]
    
    print(f"Parim vastaja: {parim['nimi']}-({parim['punktid']} õigesti)")
    print("Lugupidamisega,")
    print("Küsimustiku Automaatprogramm")


def küsimuste_lisamine(kusimus, vastus):
    with open("kusimused_vastused.txt", "a", encoding="utf-8") as f:
        print(f"{kusimus}:{vastus}", file=f)
