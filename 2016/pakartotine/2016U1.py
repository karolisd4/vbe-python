class Uzduotis():
    def __init__(self, duomenys: str, kiek_mok: int):
        '''Inicijuojama klase, gaunamas duomenu string, mokiniu kiekio integer. Ugiu sumos ir mokiniu, kurie aukstesni
        uz vidurki kintamieji nustatomi i 0 '''

        self.duomenys = duomenys
        self.kiek_mok = kiek_mok
        self.ugiu_suma = 0
        self.aukstesni_uz_vidurki = 0

    def gauti_ugius(self):
        '''Skaitomi visi ugiai be masyvu tiek kartu, kiek nurodyta duomenu faile'''

        self.nustatyti_indexus()
        for _ in range(kiek_mok):
            ugis = int(self.duomenys[self.pr_index:self.pab_index])
            self.pr_index += 4
            self.pab_index += 4
            yield ugis

    def vidurkio_sveikoji_dalis(self) -> int:
        '''Pasiima klases ugiu suma bei mokiniu kiekis, naudojamas // operatorius gauti vidurkio sveikaja dali'''

        self.vidurkis = self.ugiu_suma // self.kiek_mok

    def kiek_aukstesni_uz_sveikaja_dali(self) -> int:
        '''Nusistatomi indexai, pagal kuriuos bus skaitomi ugiai.
        Skaitomi ugiai, jei jie didesni uz klases vidurki, prie kintamojo pridedamas vienetas'''

        for ugis in self.gauti_ugius():
            if ugis > self.vidurkis:
                self.aukstesni_uz_vidurki += 1

    def main(self):
        '''Perskaitomi ugiai, kiekvienas ugis pridedamas prie klases ugiu sumos kintamojo. Sukuriami klases vidurkio sveikosios dalies
        ir mokiniu kiekio, kurie aukstesni uz vidurki kintamieji saukiant atitinkamas funkcijas'''

        for ugis in self.gauti_ugius():
            self.ugiu_suma += ugis

        # Saukiamos funkcijos, kurios sukurs atitinkamus self kintamuosus
        self.vidurkio_sveikoji_dalis()
        self.kiek_aukstesni_uz_sveikaja_dali()

        # Rezultatai surasomi i faila
        with open('./2016/pakartotine/U1rez.txt', 'w') as f:
            f.write(f'{str(self.vidurkis)} {self.aukstesni_uz_vidurki}')
    
    def nustatyti_indexus(self):
        '''Indexai visad kis kas 4, bet prasides skirtingose pozicijose, pagal mokiniu kieki, kiekvienas skaitmuo
        mokiniu kiekyje prides vieneta prie indexo pradzios ir pabaigos'''

        if self.kiek_mok in range(10):
            self.pr_index = 2
            self.pab_index = 5
        elif self.kiek_mok in range(100):
            self.pr_index = 3
            self.pab_index = 6
        elif self.kiek_mok == 100:
            self.pr_index = 4
            self.pab_index = 7


if __name__ == '__main__':
    # Perskaitomi duomenys i string formata, kad nebutu naudojami masyvai
    with open('./2016/pakartotine/U1.txt', 'r') as f:
        duomenys = f.read().strip()

    # Vel atidaromas failas ir perskaitoma tik pirma eilute su mokiniu kiekiu
    with open('./2016/pakartotine/U1.txt', 'r') as f:
        kiek_mok = int(f.readline().strip())

    # Tikrinama, ar mokiniu ugiu kiekis telpa i salygos intervala
    assert 1<=kiek_mok<=100

    # Sukuriamas objektas, kuriam duodamas duomenu string ir mokiniu kiekis, tuo paciu metu saukiama klases main funkcija
    Uzduotis(duomenys, kiek_mok).main()
