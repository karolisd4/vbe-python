def main():
    # Perskaitau duomenis
    with open('./2012/pagrindine/U1.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
        kiek_zaid = duomenys[0] 
        duomenys.pop(0)

    # Sukuriu pradinius masyvus ir indekso kintamaji, kad galeciau sekti, ar sarase yra penki pirmi zaidejai
    i = 0
    zaideju_duom = {}
    startinis_penketukas = []

    for zaidejas in duomenys:
        zaidejo_praleistas_laikas = 0
        zaidejo_sedetas_laikas = 0

        # Viska sudedu i masyva, randu esamo zaidejo numeri, bei jo visus zaidimo laikus
        zaidejas_list = zaidejas.split(' ')
        zaidejo_nr = zaidejas_list[0]
        
        if i <= 5:
            i += 1
            startinis_penketukas.append(int(zaidejo_nr))

        # Einu per zaidejo laikus, jei jis yra neigiamas, pridedu prie praleisto sedint laiko, jei ne - prie praleisto zaidziant laiko
        for laikas in zaidejas_list[2:]:
            if int(laikas) < 0:
                zaidejo_sedetas_laikas += int(laikas)
            else:
                zaidejo_praleistas_laikas += int(laikas)
        zaideju_duom[zaidejo_nr] = (zaidejo_praleistas_laikas, zaidejo_sedetas_laikas)

    daugiausia_laiko_zaide = max(zaideju_duom.values())[0]
    daugiausia_laiko_sedejo = min(zaideju_duom.values())[1]
    startinis_penketukas = [str(nr) for nr in sorted(startinis_penketukas)]

    for k, v in zaideju_duom.items():
        if v[1] == daugiausia_laiko_sedejo:
            sedejes_zaidejas = (k, daugiausia_laiko_sedejo)
        elif v[0] == daugiausia_laiko_zaide:
            zaides_zaidejas = (k, daugiausia_laiko_zaide)   

    with open('./2012/pagrindine/U1rez.txt', 'w') as f:
        f.write(' '.join(startinis_penketukas) + '\n')
        f.write(f'{zaides_zaidejas[0]} {zaides_zaidejas[1]}\n')
        f.write(f'{sedejes_zaidejas[0]} {abs(sedejes_zaidejas[1])}')

main()
