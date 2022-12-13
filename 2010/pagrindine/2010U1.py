def kiek_galima_sudaryti_komplektu(atnesti_sachmatai):
    # Sukuriamas tuscias masyvas, kuriame bus saugomas skaicius komplektu, kuriuos galima sudaryti tik su viena is figuru
    kiek_galima_sudaryt = []

    # Sukuriamas dictionary, kuriame yra tiek figuru, kiek reikia pilnam komplektui
    komplektas = {'pestininkai': 8,
    'bokstai': 2,
    'zirgai': 2,
    'rikiai': 2,
    'karaliai': 1,
    'valdoves': 1}

    # Einama per visu atnestu ir reikiamu figuru dictionaries ir kiekviena figuros kieki dalinama be liekanos, taip suzinoma kiek
    # galima padaryti komplektu tik su ta figura. Skaicius dedamas i masyva
    for reikia_figuru, atnestos_figuros in zip(komplektas.values(), atnesti_sachmatai.values()):
       kiek_galima_sudaryt.append(atnestos_figuros // reikia_figuru)
    
    # Maziausias skaicius bus komplektu skaicius, kuri galima sudaryti is visu atnestu figuru
    return str(min(kiek_galima_sudaryt))
        

def main():
    # Perskaitomas duomenu failas, duomenys sudedami i masyva, perskaitomas ir istrinamas mokiniu skaicius
    with open('./2010/pagrindine/U1.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
        mok_sk = int(duomenys[0])
        duomenys.pop(0)

    # Tikrinama, ar tinkamas mokiniu skaicus
    assert 1<=mok_sk<=100
    
    # Sukuriamas dictionary su visom turimom figurom, kiekvienos pradzioje turima po 0
    atnesti_sachmatai = {'pestininkai': 0,
    'bokstai': 0,
    'zirgai': 0,
    'rikiai': 0,
    'karaliai': 0,
    'valdoves': 0}

    # Einama per duomenu masyva bei sachmatu dictionary ir kiekvienai figurai pridedamas atitinkamas jos skaicius
    for atnesti_duom in duomenys:
        for figura, figuru_kiekis in zip(atnesti_sachmatai, atnesti_duom.split(' ')):
            atnesti_sachmatai[figura] += int(figuru_kiekis)

    # Gaunamas rezultatas ir irasomas i rezultatu faila
    res = kiek_galima_sudaryti_komplektu(atnesti_sachmatai)

    with open('./2010/pagrindine/U1rez.txt', 'w') as f:
        f.write(res)


main()