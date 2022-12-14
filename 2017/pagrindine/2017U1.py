def nustatyti(pirmas, antras):
    # Sukuriamas zodynas, kuriame rodoma, kaip koduojami skaiciai i raides
    sesioliktainis = {10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'}

    # Einama per zodyno skaicius, jei duoti skaiciai sutampa, rezultato skaitmuo tampa atitinkama raide
    for reiksme in sesioliktainis:
        if pirmas == reiksme:
            pirmas_skaitmuo = sesioliktainis[reiksme]
        if antras == reiksme:
            antras_skaitmuo = sesioliktainis[reiksme]
    
    # Jeigu skaiciai yra intervale nuo 0 iki 9, jie islieka tokie patys
    if pirmas in range(10):
        pirmas_skaitmuo = pirmas
    if antras in range(10):
        antras_skaitmuo = antras
        
    return str(pirmas_skaitmuo), str(antras_skaitmuo)


def gauti_sesioliktaini_skaiciu(rgb):
    # Sukuriamas tuscias rezultato string, i kuri bus dedami atskiri sesioliktainio skaiciaus skaitmenys
    rez = ''

    # Gauti skaiciai paverciami i integer tipa
    rgb = [int(sk) for sk in rgb.split(' ')]

    # Einama per kiekviena spalva, kiekvienas numeris paverciamas i sesioliktainio skaiciaus skaitmenis pagal salyga
    # Naudojamas // operatorius gauti skaiciaus sveikaja dali ir % operatorius, kad gauti liekana
    for spalva in rgb:
        pirmas_skaitmuo, antras_skaitmuo = nustatyti(spalva // 16, spalva % 16)

        # Gauti skaitmenys prijungiami i rezultato string
        rez += pirmas_skaitmuo + antras_skaitmuo

    return rez


def main():
    # Perskaitomi pradiniai duomenys i duomenu masyva. Perskaitomas ilgis bei plotis ir jie pasalinami is duomenu masyvo
    with open('./2017/pagrindine/U1.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
        ilgis, plotis = (int(sk) for sk in duomenys[0].split(' '))
        duomenys.pop(0)
    
    # Tikrinama, ar ilgis ir plotis atitinka salyga
    assert 1<=ilgis<=10000
    assert 1<=plotis<=10000

    # Sukuriami tusti masyvai, kuriuose bus laikomi rezultatai
    skaiciai = []
    rezultatas = ''

    # Einama per visus duotus skaicius, jei paverciami i sesioliktainius ir sudedami i masyva
    for rgb in duomenys:
        sesioliktainis = gauti_sesioliktaini_skaiciu(rgb)
        skaiciai.append(sesioliktainis)

    # Formatuojamas rezultatas, kad butu tiek eiluciu ir tiek stulpeliu, koks yra plotis ir ilgis
    for _ in range(ilgis):

        # I kiekviena stulpeli sudedamas toks skaicius sesioliktainiu skaiciu, koks duotas plotis duomenu faile        
        rezultatas += ';'.join(skaiciai[:plotis])

        # Jeigu jau kazkas irasyta i rezultata, dedama nauja eilute, kad atskirti stulpelius
        if rezultatas:
            rezultatas += '\n'
        
        # Jau surasyti skaiciai yra pasalinami, o jei nera ka salinti sugaunama ir praleidziama IndexError klaida
        for i in range(plotis):
            try:
                skaiciai.pop(i)
            except IndexError:
                pass
    
    # Irasomas gautas rezultatas
    with open('./2017/pagrindine/U1rez.txt', 'w') as f:
        f.write(rezultatas)


if __name__ == '__main__':
    main()
