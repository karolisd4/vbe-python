def gauti_kaina_centais(produktai, kainos):
    # Einama per reikiamu produktu ir tu produktu kainos masyvus ir juos sudedama i pilnos kainos kintamaji
    # Jei kiekis yra 0, t.y produkto nereikia, ciklas praleidziamas ir tesiama su kitais kintamaisiais
    pilna_kaina = 0
    for kaina, kiekis in zip(produktai, kainos):
        if kiekis == 0:
            continue
        pilna_kaina += kaina * kiekis
    return pilna_kaina


def gauti_svecio_pietu_kaina_centais(patiekalai):
    # Gaunama visu zodyno value (kievieno patiekalo centu) suma
    return sum(patiekalai.values())


def main():
    # Perskaitomi duomenys ir sudedami i masyva, gaunamas patiekalu ir produktu skaicius, jie is karto pasalinami is masyvo
    with open('./2010/pagrindine/U2.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
        produktu_sk, patiekalu_sk = [int(sk) for sk in duomenys[0].split(' ')]
        duomenys.pop(0)

    # Tikrinama, ar tinkamas duomenu skaicius
    assert 1<=patiekalu_sk<=12
    assert 1<=produktu_sk<=10
    
    # Sukuriamas tuscias zodynas, kur bus laikomos patiekalu kainos centais bei sukuriamas kainu masyvas, kur sudedamos visos kainos, paverstos i integer tipa
    patiekalai = {}
    kainos = [int(kaina) for kaina in duomenys[0].split(' ')]

    # Einama per duomenis, neiskaitant kainu eilutes, perskaitomas pavadinimas, reikiami produktai ir viskas sudedama i zodyna
    for patiekalas in duomenys[1:]:
        pavadinimas = patiekalas[:16].strip()

        # Kiekvienas reikiamas produktas paverciamas i integer tipa
        produktai = [int(produktas) for produktas in patiekalas[16:].split(' ')]
        patiekalai[pavadinimas] = gauti_kaina_centais(produktai, kainos)

    # Gaunama pilna svecio kaina centais, ji paverciama i litus dalinant is 100 ir gaunant sveikaja dali
    # Centai gaunami naudojant modulus operatoriu ir gaunant liekana
    pilna_svecio_kaina_centais = gauti_svecio_pietu_kaina_centais(patiekalai)
    kaina_litais = str(pilna_svecio_kaina_centais // 100)
    kaina_centais = str(pilna_svecio_kaina_centais % 100)
    
    # Surasomi rezultatai einant per patiekalu zodyna
    with open('./2010/pagrindine/U2rez.txt', 'w') as f:
        for patiekalas, kaina in patiekalai.items():
            f.write(f'{patiekalas:15} {kaina}\n')
        f.write(f'{kaina_litais} {kaina_centais}')


main()