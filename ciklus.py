
nev_osztalyzat = []
jegyek = []





kerdes = int(input("Hány diákot szeretnél hozzáadni? "))

szamlalo = 0

for szam in range(kerdes):
    szamlalo += 1
    nevbekerdezes = input(f"Add meg a(z) {szamlalo} diák nevét: ")
    
    
    osztalyzat = int(input(f"Add meg {nevbekerdezes} jegyét: "))
    nev_osztalyzat.append((nevbekerdezes, osztalyzat))
    jegyek.append(osztalyzat)
    

szeretne_e_megtekinteni = input("Szeretnéd látni az összes diákot? (igen/nem): ")
if szeretne_e_megtekinteni == "nem" or "Nem":
    exit
if szeretne_e_megtekinteni == "igen" or "Igen":
    print(f"Diákok:\nNév     | Jegy\n----------------")
    for lista in nev_osztalyzat:
        print(lista)


atlagosjegy_megtekintes = input("Szeretnéd tudni az átlagos jegyet? (igen/nem): ")
if atlagosjegy_megtekintes == "nem" or "Nem":
    exit
if atlagosjegy_megtekintes == "igen" or "Igen":
    print("Az átlagos jegy:",sum(jegyek) / len(jegyek))



kerdes_legmagasabb_legalacsonyabb_jegyek = input("Szeretnéd tudni a legmagasabb és legalacsonyabb jegyet? (igen/nem): ")
if kerdes_legmagasabb_legalacsonyabb_jegyek == "nem" or "Nem":
    exit
if kerdes_legmagasabb_legalacsonyabb_jegyek == "igen" or "Igen":
    print(f"Legmagasabb jegy: {max(jegyek)} \nLegalacsonyabb jegy: {min(jegyek)}")



szeretne_e_eltavolitani = input("Szeretnél eltávolítani egy diákot? (igen/nem): ")
if szeretne_e_eltavolitani == "nem" or "Nem":
    exit
if szeretne_e_eltavolitani == "igen" or "Igen":
    kit_tavolitsunk_el = input("Add meg a diák nevét, akit el szeretnél távolítani: ")
    print(kit_tavolitsunk_el, "eltávolítva.")

    db = 0
    
    for torles in nev_osztalyzat:
        
        for vegleges in torles:
            if vegleges == kit_tavolitsunk_el:
                nev_osztalyzat.pop(db)
        
        db += 1
    for lista in nev_osztalyzat:
        print(lista)
    
