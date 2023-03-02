import datetime # Importuojama laiko skaičiavimo biblioteka, kad būtų galima lengvai laikyti ir skaičiuoti sportininkų laikus.


class Athlete():
    '''Sportininko klasė. Joje saugomas sportininko vardas, pradžios ir pabaigos laikas, baudos minutės.
    Klasė turi funkciją, kuri skaičiuoja rezultato laiką - iš finišo laiko atima pradžios laiką ir prideda baudos minutes.'''

    def __init__(self, name: str, start_time: datetime.timedelta):
        self.name = name
        self.start_time = start_time
        self.finish_time = None     # Pradžioje niekas neturės finišo laiko, tad jis yra None tipo.
        self.bonus_minutes = 0
    
    def calculate_result(self):
        '''Skaičiuojamas rezultatas - iš finišo laiko atimamas starto laikas ir pridedamos baudos minutės. Baudos minučių integer
        paverčiamas į timedelta objektą, kad būtų galima daryti sudėtį.'''
        self.result_time = self.finish_time - self.start_time + datetime.timedelta(minutes=self.bonus_minutes)


def sort_data(data: dict) -> list:
    '''Funkcija, kuri surikiuoja sportininkų rezultatus pagal laiką didėjančia tvarka. Jeigu rezultatai vienodi, rikiuoja abėcėliškai.
    Funkcijai duodamas žodynas, kuris paverčiamas į tuple tipą. Lambda funkcija pirmiausia rikiuoja pagal laiką, t.y antro indekso
    pirmą indeksą (x[1][0]). Jeigu laikai sutampa, rikiuojama pagal vardą, kuris yra tuple pirmas indeksas x[0].'''
    return sorted(data.items(), key=lambda x: (x[1][0], x[0]))


def write_result(gender: str, data: list, file):
    '''Funkcija, kuri surašo rezultatus į duomenų failą.'''
    file.write(gender + '\n')   # Parašoma, ar spausdinami vaikinai, ar merginos pagal duotą argumentą.
    for athlete in data:
        name = athlete[0]   # Pirmas indeksas ([0]) yra vardas, string tipas.
        # Antras indeksas ([1]) yra tuple, kuris turi laiką ir starto numerį.
        h, m, s = str(athlete[1][0]).split(':')     # Antro indekso pirmas indeksas yra laikas, antras indeksas yra starto numreis.
        id_num = str(athlete[1][1])
        file.write(f'{id_num} {name:<20} {h} {m} {s}\n')    # Vardui duodama 20 simbolių su :<20.


def main():
    with open('./2019/pagrindine/U2.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]     # Perskaitomi duomenys, pašalinami nereikalingi tarpai.
    # Perskaitomi sportininkų ir finišavusių sportininkų skaičiai, jie pašalinami iš duomenų masyvo. Tikrinama, ar jie atitinka sąlygą su assert.
    athlete_count = int(data[0])
    data.pop(0)
    finished_athlete_count = int(data[athlete_count])
    data.pop(athlete_count)
    assert 1 <= athlete_count <= 30
    assert 1 <= finished_athlete_count <= 30
    
    # Sukuriami tušti žodynai saugoti merginų ir vaikinų informacijai bei rezultatams.
    males = {}
    females = {}
    males_res = {}
    females_res = {}
    
    # Einama per duomenų masyvą, tiek eilučių, kiek yra dalyvaujančių sportininkų.
    for line in data[:athlete_count]:
        name = line[:20].strip()
        # Randamas vardas, starto numeris, starto laikas. Laikas įdedamas į timedelta objektą.
        id_num, s_hour, s_min, s_sec = [int(num) for num in line[20:].strip().split(' ')]
        start_time = datetime.timedelta(hours=s_hour, minutes=s_min, seconds=s_sec)
        # Sukuriamas sportininko objektas, kuriam duodamas vardas ir pradžios laikas.
        athlete = Athlete(name, start_time=start_time)
        # Merginų starto numeriai prasideda vienetu, vaikinų – dvejetu. Pagal atitinkamą lytį sportininkai sudedama į žodynus.
        if str(id_num)[0] == '1':
            females.setdefault(id_num, athlete)
        elif str(id_num)[0] == '2':
            males.setdefault(id_num, athlete)
    
    # Einama per finišavusius sportininkus.
    for line in data[athlete_count:]:
        id_num, f_hour, f_min, f_sec =  [int(num) for num in line.split()[:4]]  # Randamas starto numeris, finišavimo laikas. Viskas paverčiama į integer tipą.
        finish_time = datetime.timedelta(hours=f_hour, minutes=f_min, seconds=f_sec,)   # Finišavimo laikas įdedamas į timedelta objektą.
        shooting_range = [int(num) for num in line.split()[4:]]     # Randama ir paverčiama į interger tipą sportininko šaudyklos informacija.
        # Tikrinama sportininko lytis, sportininko objektui suteikiamas finišavimo laikas.
        if str(id_num)[0] == '1':
            females[id_num].finish_time = finish_time
            for points in shooting_range:
                # Einama per šaudyklos duomenis. Kadangi maksimalus taškų skaičius yra 5, baudų minutės skaičiuojamos iš 5 atėmus taškų skaičių.
                bonus_minutes = 5 - points
                females[id_num].bonus_minutes += bonus_minutes  # Į objektą pridedamos baudos minutės.
            females[id_num].calculate_result()  # Šaukiama objektų rezultatų skaičiavimo funkcija, kai turime finišo laiką ir baudos minutes.
        
        # Viskas analogiškai kartojama su vaikinais.
        elif str(id_num)[0] == '2':
            males[id_num].finish_time = finish_time
            for points in shooting_range:
                bonus_minutes = 5 - points
                males[id_num].bonus_minutes += bonus_minutes
            males[id_num].calculate_result()

    # Einama per vaikinus ir merginas.
    for athlete in females:
        # Jeigu sportininkas neturi finišo laiko, t.y jis nebuvo atnaujintas, nes nebuvo sąraše, jį praleidžiama.
        if not females[athlete].finish_time:
            continue
        # Į rezultatų žodyną įdedamas sportininko vardas kaip value, o (rezultato laikas, starto numeris) kaip žodyno key.
        females_res.setdefault(females[athlete].name, (females[athlete].result_time, athlete))
        
    # Viskas analogiškai kartojama su vaikinais.
    for athlete in males:
        if not males[athlete].finish_time:
            continue
        males_res.setdefault(males[athlete].name, (males[athlete].result_time, athlete))

    # Failas atidaromas prieš šaukiant funkcijas, kad viską būtų galima surašyti neuždarant failo, t.y per vieną kartą.
    with open('./2019/pagrindine/U2rez.txt', 'w') as f:
        # Funkcijai duodamas lyties argumentas, surikiuotas rezultatų žodynas ir failo objektas, kad būtų galima viską surašyti.
        write_result('Merginos', sort_data(females_res), file=f)
        write_result('Vaikinai', sort_data(males_res), file=f)


# Šaukiama pagrindinė funkcija.
if __name__ == '__main__':
    main()