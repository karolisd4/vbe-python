def main():
    # Perskaitomi duomenis
    with open('./2012/pagrindine/U1.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
        kiek_zaid = duomenys[0] 
        duomenys.pop(0)

    # Sukuriami pradiniai masyvai ir indekso kintamasis, kad butu galima sekti, ar sarase yra penki pirmi zaidejai
    i = 0
    zaideju_duom = {}
    startinis_penketukas = []

    for zaidejas in duomenys:
        zaidejo_praleistas_laikas = 0
        zaidejo_sedetas_laikas = 0

        # Viskas sudedama i masyva, randamas esamo zaidejo numeris, bei jo visi zaidimo laikai
        zaidejas_list = zaidejas.split(' ')
        zaidejo_nr = zaidejas_list[0]
        
        # Pirmi penki zaidejai sudedami i masyva
        if i <= 5:
            i += 1
            startinis_penketukas.append(int(zaidejo_nr))

        # Einama per zaidejo laikus, jei jie yra neigiami, pridedama prie praleisto sedint laiko, jei ne - prie praleisto zaidziant laiko
        for laikas in zaidejas_list[2:]:
            if int(laikas) < 0:
                zaidejo_sedetas_laikas += int(laikas)
            else:
                zaidejo_praleistas_laikas += int(laikas)
        zaideju_duom[zaidejo_nr] = (zaidejo_praleistas_laikas, zaidejo_sedetas_laikas)
    
    # Atrandamas daugiausiai laiko zaides zaidejas, bei maziausiai laiko zaides t.y sedejes zaidejas
    daugiausia_laiko_zaide = max(zaideju_duom.values())[0]
    daugiausia_laiko_sedejo = min(zaideju_duom.values())[1]
    
    # Isrusiuojamas startinio penketuko zaideju masyvas didejancia tvarka ir visi jo elementai paverciami i string tipa
    startinis_penketukas = [str(nr) for nr in sorted(startinis_penketukas)]

    # Einama per dict items ir ziurima, kuris value sutampa su daugiausiai laiko sedejusiu bei zaidusiu zaideju
    # v[1] - visi laikai, kai buvo sedima, v[0], - visi laikai kai buvo zaidziama
    for k, v in zaideju_duom.items():
        if v[1] == daugiausia_laiko_sedejo:
            sedejes_zaidejas = (k, daugiausia_laiko_sedejo)
        elif v[0] == daugiausia_laiko_zaide:
            zaides_zaidejas = (k, daugiausia_laiko_zaide)   

    # Surasomi duomenys i rezultatu faila
    with open('./2012/pagrindine/U1rez.txt', 'w') as f:
        f.write(' '.join(startinis_penketukas) + '\n')
        f.write(f'{zaides_zaidejas[0]} {zaides_zaidejas[1]}\n')
        f.write(f'{sedejes_zaidejas[0]} {abs(sedejes_zaidejas[1])}')

main()
