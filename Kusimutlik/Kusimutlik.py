1
sõnastik, loend=andmete_lugemine_failidest(loend,sõnastik)
print(sõnastik)
print(loend)

sõnastik={"A":"a"}
loend=["A"]

2
    while True:
        nimi=input("Sisesta oma nimi: ")
        N=5
        if nimi not in nimed:
            print(F"Tere, {nimi}! Test koosneb {str(N)}küsimusest.")
            nimed.append(nimi)
            break
        else:
            print("Seda kasutaja on juba testinud!")

4=3 (mi iz tretego zadaniya vinosim 4)
M = 3
testitud = []

for _ in range(M):
    nimi = input("Sisesta nimi: ")

    if nimi in testitud:
        print("See kasutaja on juba testitud!")
        continue

    testitud.append(nimi)
