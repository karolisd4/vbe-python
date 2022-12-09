def rikiuoti_duomenis(pratimu_duom):
    '''Isrikiuojami pratimu duomenys mazejimo tvarka. Jeigu skaiciai vienodi, abeceles tvarka.'''

    # Sukuriamas naujas dictionary isrikiuotiems duomenims saugoti
    pratimu_duom_isrikuota = {}

    # Pirmiausia einama per visus pratimu kiekius, isrikiuotus mazejimo tvarka
    for pirmas_kiekis in sorted(pratimu_duom.values(), reverse=True):

        # Toliau einama per abeceles tvarka isrikiuotus duomenis. Jei abeceles tvarka isrikiuotu duomenu kiekis sutampa su pirmu kiekiu,
        # duomenys issaugomi naujame dictionary. Jei skaiciai vienodi, viskas bus saugoma abeceles tvarka
        for pavadinimas, antras_kiekis in sorted(pratimu_duom.items()):
            if antras_kiekis == pirmas_kiekis:
                pratimu_duom_isrikuota[pavadinimas] = pirmas_kiekis

    # Grazinamas naujas dictionary
    return pratimu_duom_isrikuota
                

def main():
    # Perskaitomi duomenys, pasalinami nereikalingi tarpai is liniju
    with open('./2016/pagrindine/U2.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
    
    # Perskaitomas eiluciu skaicius, jis pasalinamas is duomenu
    eil_sk = int(duomenys[0])
    duomenys.pop(0)
    pratimu_duom = {}

    # Einama per duomenis tiek kartu, koks yra eiluciu skaicius
    for i in range(eil_sk):
        # Pirmos 20 poziciju - pratimo pavadinimas, toliau - kiekis. Perskaicius pavadinima, pasalinami nereikalingi tarpai
        pavadinimas = duomenys[i][:20].strip()
        kiekis = int(duomenys[i][20:])

        # Pratimu pavadinimai sudedami i dictionary, susumuojami kiekiai
        pratimu_duom.setdefault(pavadinimas, 0)
        pratimu_duom[pavadinimas] += kiekis

    # Pratimu duomenu dictionary isrikiuojamas ir pakeiciamas nauju
    pratimu_duom = rikiuoti_duomenis(pratimu_duom)

    # Surasomi rezultatai. Pavadinimas padaromas 20 simboliu ilgumo (:<20)
    with open('./2016/pagrindine/U2rez.txt', 'w') as f:
        for pavadinimas, kiekis in pratimu_duom.items():
            f.write(f'{pavadinimas:<20}{kiekis}\n')


main()