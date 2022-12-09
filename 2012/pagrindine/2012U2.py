class Dievas():
    '''Klase, kurioje saugomas dievo vardas ir jo visi ismesti kauliuku skaiciai'''

    def __init__(self, vardas: str, kauliukai: list):
        '''Inicijuojama klase, duodamas vardas ir masyvas su skaiciais'''

        self.vardas = vardas
        self.kauliukai = kauliukai

    def kauliuku_suma(self) -> int:
        '''Atrandama suma visu skaiciu kauliuku masyve, paverciant visus kauliukus i int tipa'''

        return sum([int(numeris) for numeris in self.kauliukai])
    
    def kiek_lyginiu_tasku(self) -> int:
        '''Atrandamas visu lyginiu kauliuku skaiciu kiekis. Visi skaiciai paverciami i int tipa,
        naudojama liekanos operacija, ziureti, ar skaicius yra lyginis t.y, ji dalinant is dvieju, liekana 0'''

        return len([int(numeris) for numeris in self.kauliukai if int(numeris) % 2 == 0])


def skaityti_duomenis() -> list:
    '''Perskaitomos visos linijos, is kiekvienos linijos pasalinant nereikalingus tarpus'''

    with open('./2012/pagrindine/U2.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def rasti_valdova(dievai: list) -> str:
    '''Randamas valdovas pagal salyga. Naudojama :<9 lygiuoti teksta 10 eiluciu i desine, iskaitant pirma raide'''

    sumos = [dievas.kauliuku_suma() for dievas in dievai]
    daugiausia_surinkes = max(sumos)
    sumos.remove(daugiausia_surinkes)

    # Atrandamas didziausias tasku sumos skaicius ir tikrinama, ar jis kartojasi
    for suma in sumos:
        if suma == daugiausia_surinkes:
            # Jei yra keli vienodi didziausi tasku sumos skaiciai, tikrinamas lyginiu skaiciu kiekis
            # Jeigu visi dievai turi po vienoda lyginiu skaiciu kieki, visados bus grazinamas pirmas sarase dievas, nes jie sudedami is eiles
            lyginiai = [(dievas.kiek_lyginiu_tasku(), dievas.vardas) for dievas in dievai]
            daugiausia_lyginiu = max(lyginiai)
            return f'{daugiausia_lyginiu[1]:<9} {daugiausia_lyginiu[0]}'
        else:
            # Jei daugiausia tasku surinkes skaicius yra vienintelis, pagal ji atrandamas valdovo vardas ir grazinamas rezultatas
            for dievas in dievai:
                if daugiausia_surinkes == dievas.kauliuku_suma():
                    return f'{dievas.vardas:<9} {daugiausia_surinkes}'


def main():
    # Perskaitomi duomenys, randamas ir pasalinamas dievu kiekis, sukuriamas masyvas visiems dievu objektams saugoti
    duomenys = skaityti_duomenis()
    dievu_sk = int(duomenys[0].split(' ')[0])
    duomenys.pop(0)
    dievai = []

    # Einama per tiek eiluciu, kiek yra nurodyta dievu
    for i in range(dievu_sk):

        # Randamas vardas pirmose 10 poziciju, kauliuku skaiciai kitose eilutese
        vardas = duomenys[i][:10].strip()
        mesti_kauliukai = duomenys[i][10:].split(' ')

        # Sukuriamas dievo objektas, jam duodamas vardas ir kauliuku skaiciu masyvas, viskas sudedama i dievu masyva
        dievas = Dievas(vardas, mesti_kauliukai)
        dievai.append(dievas)

    with open('./2012/pagrindine/U2rez.txt', 'w') as f:
        f.write(rasti_valdova(dievai))
    

main()
