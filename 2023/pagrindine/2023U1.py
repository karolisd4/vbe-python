def read():
    with open('2023/U1.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()] # Perskaitomi duomenys, pašalinant nereikalingus tarpus, jeigu tokių yra.
    mok_sk = int(duomenys[0])   # Randamas ir tikrinamas mokinių skaičius pagal sąlygą, jis pašalinamas iš duomenų sąrašo, nes yra nereikalingas.
    assert 10 <= mok_sk <= 50
    duomenys.pop(0)
    return duomenys # Grąžinami duomenys.


def main():
    duomenys = read()   # Perskaitomi duomenys.
    mokiniai = {}   # Sukuriamas žodynas mokinių duomenims saugoti ir apdoroti.
    for eilute in duomenys:  
        neivesti_duomenys = False   # Jeigu mokinys neįveda duomenų, šis bool leidžia jį praleisti ateityje. Kievienoje naujoje eilutėje jis grįžta į False būseną.
        eilute = eilute.split(' ')  # Kiekviena eilutė padaroma į sąrašą.
        zingsniu_suma = 0   # Kiekvieno mokinio žingsnių suma pradžioje bus 0.
        kategorija = eilute[0]  # Randama mokinio kategorija ir jo žingsnio ilgis, ši informacija pašalinama iš eilutės, kad nesimaišytų.
        zingsnio_ilgis = int(eilute[1])
        eilute.pop(1)
        eilute.pop(0) 
        for zingsniu_sk in [int(numeris) for numeris in eilute]:    # Dar viename for cikle einama per visus žingsnius ir jie sumuojami.
            if zingsniu_sk == 0:    # Jeigu bent vieną kartą yra nenueiti žingsniai, naudojamas bool tikrinimas, kad praleisti mokinį.
                neivesti_duomenys = True    # Paverčiama bool į True ir baigiamas ciklas.
                break
            zingsniu_suma += zingsniu_sk    # Sumuojami žingsniai.
        if neivesti_duomenys:   # Jeigu bool buvo paverstas į True, iš karto einama prie kitos eilutės su continue.
            continue
        zingsniu_suma *= zingsnio_ilgis / 100000    # Centimetrai paverčiami į kilometrus. 1km = 100000cm.
        zingsniu_suma = round(zingsniu_suma, 2)     # Apvalinama iki šimtųjų.
        try:
            mokiniai[kategorija][1] += zingsniu_suma    # Bandoma jau pridėti duomenis prie senų, jeigu kartojasi kategorija.
            mokiniai[kategorija][0] += 1
        except KeyError: pass   # Jeigu kategorija nesikartoja, gaunama KeyError, šią klaidą praleidžiama ir įvedamas naujas key su value į žodyną.
        mokiniai.setdefault(kategorija, [1, zingsniu_suma])
        
    with open('2023/U1rez.txt', 'w') as f:  # Sukuriamas rezultatų failas ir jame surašomi gauti žodyno duomenys.
        for kategorija, v in mokiniai.items():
            kiek_mokiniu = v[0]
            atstumas = v[1]
            f.write(f'{kategorija} {kiek_mokiniu} {atstumas}\n')


# Pagrindinė funkcija.
if __name__ == "__main__":
    main()