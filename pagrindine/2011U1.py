class Pirstine():
    def __init__(self, lytis: int, ranka: int, dydis: int):
        # Inicijuojamas pirstines objektas, kuriame saugoma pirstines lytis, ranka ir dydis
        # Pagal salyga: 3 - vyriska pirstine, 4 - moteriska pirstine, 1 - kaire ranka, 2 - desine ranka
        self.lytis = lytis
        self.ranka = ranka
        self.dydis = dydis


def skaityti_duomenis():
    # Perskaitomi duomenys ir sudedami i masyva, pasalinant nereikalingus tarpus, jei tokiu yra
    with open('./2011/pagrindine/U1.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]

    # Perskaitomas pirstiniu skaicius ir tikrinama, ar yra tinkamas kiekis
    pirstiniu_sk = int(duomenys[0])
    assert 1<=pirstiniu_sk<=100

    return duomenys


def gauti_poras(pirstines: list[Pirstine]):
    mot_pirstines = []  # Sukuriami du masyvai saugoti ir atskirti moteriskas ir vyriskas pirstines
    vyr_pirstines = []

    # Suskirstomos pirstines i masyvus pagal lyti
    for pirstine in pirstines:
        if pirstine.lytis == 3:
            vyr_pirstines.append(pirstine)
        if pirstine.lytis == 4:
            mot_pirstines.append(pirstine)

    def skaiciuoti(pirstines: list[Pirstine]) -> int:
        poros = 0
        for i, pirma_pirstine in enumerate(pirstines):  # Einama per pirstiniu masyva, su kiekvienu elementu pereinant per visus kitus, neiskaitant jo
            for j, antra_pirstine in enumerate(pirstines[i+1:], start=1):
                if pirma_pirstine.ranka != antra_pirstine.ranka and pirma_pirstine.dydis == antra_pirstine.dydis:
                    # Jeigu rankos nesutampa (yra kaire ir desine) ir dydziai sutampa, gaunama pora ir antroji pirstine pasalinama is masyvo, kad ji vel nebutu priskaiciuota
                    poros += 1
                    pirstines.pop(j)
                    break
        return poros

    # Gaunamos ir grazinamos poros
    vyr_poros = skaiciuoti(vyr_pirstines)
    mot_poros = skaiciuoti(mot_pirstines)

    return vyr_poros, mot_poros

    
def gauti_atliekamas(pirstines: list[Pirstine], poros: tuple[int, int]):
    mot_pirstines = []  # Vel sukuriami masyvai skirtingu lyciu pirstinems ir jos suskirstomos
    vyr_pirstines = []
    for pirstine in pirstines:
        if pirstine.lytis == 3:
            vyr_pirstines.append(pirstine)
        if pirstine.lytis == 4:
            mot_pirstines.append(pirstine)
    # Atliekamos pirstines randamos is visu pirstiniu atemus pirstines, kurios sudaro poras, todel dauginama is 2
    vyr_atliekamos = len(vyr_pirstines) - poros[0] * 2
    mot_atliekamos = len(mot_pirstines) - poros[1] * 2

    return vyr_atliekamos, mot_atliekamos


def main():
    duomenys = skaityti_duomenis()  
    pirstines = []  # Sukuriamas masyvas, kuriama saugomi pirstiniu objektai

    for pirstine in duomenys[1:]:
        lytis, ranka, dydis = [int(skaicius) for skaicius in pirstine.split(' ')]
        pirstines.append(Pirstine(lytis, ranka, dydis)) # Atrandama pirstiniu informacija ir sukuriami pirstiniu objektai bei sudedami i masyva

    vyr_poros, mot_poros = gauti_poras(pirstines)
    vyr_atliekamos, mot_atliekamos = gauti_atliekamas(pirstines, (vyr_poros, mot_poros))

    with open('./2011/pagrindine/U1rez.txt', 'w') as f:
        f.write(f'{mot_poros}\n{vyr_poros}\n{mot_atliekamos}\n{vyr_atliekamos}')


if __name__ == '__main__':
    main()