import datetime # Importuojama laiko biblioteka, kad būtų galima lengvai saugoti minutes ir sekundes.

class Participant():
    def __init__(self, name: str, group: int, time: datetime.time):
        # Inicijuojamas dalyvio klasės objektas; dalyvis turi vardą, grupę ir laiką.
        self.name = name
        self.group = group
        self.time = time


def write_result(result: list) -> None:
    '''Funkcija paima rezultatų masyvą ir eina per jį, surašydama masyve esančio dalyvio objekto vardą, minutes ir sekundes.
    Vardui skiriama 20 pozicijų.'''
    with open('./2009/pagrindine/U2rez.txt', 'w') as f:
        for participant in result:
            f.write(f'{participant.name:<20} {participant.time.minute} {participant.time.second}\n')


def main():
    with open('./2009/pagrindine/U2.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()] # Perskaitomi duomenys, pašalinami nereikalingi tarpai, jei tokių yra.
    group_count = int(lines[0]) # Randamas grupių skaičius, jis pašalinamas iš duomenų masyvo, kad nesimaišytų.
    lines.pop(0)
    assert 2 <= group_count <= 50   # Tikrinama, ar grupių skaičius atitinka sąlygą.

    # Sukuriami masyvai duomenims saugoti - dalyviams, visoms grupėms ir atrinktiems dalyviams, t.y rezultatams.
    participants = []
    groups = [[] for _ in range(group_count)]   # Grupių masyvas savyje turės po tuščią masyvą kiekvienos grupės dalyviams saugoti.
    results = []

    group = 0   # Sukuriamas kintamasis, kuriame saugomas esamos grupės skaičius.
    for line in lines:
        if len(line) <= 2:  # Jeigu duomenų eilutės ilgis yra mažesnis už 2, t.y jis yra grupės narių skaičius, ciklas praleidžiamas ir prie grupės skaičiaus pridedamas vienetas.
            group += 1
            continue
        # Pirmos 20 simbolių - vardas, toliau - minutės ir sekundės.
        name = line[0:20].strip()
        minutes, seconds = line[21:].split(' ')
        time = datetime.time(minute=int(minutes), second=int(seconds))  # Naudojantis datetime biblioteka, minutės ir sekundės sudedamos į laiko objektą.
        participants.append(Participant(name, group, time)) # Į dalyvių masyvą įdedamas dalyvio objektas su vardu, grupe ir laiku.

    # Einama per kiekvieną dalyvį, tikrinant jo grupę.
    for participant in participants:
        # Einama per grupių skaičiaus aibę, jei dalyvio grupė sutampa su skaičiumi, dalyvis įdedamas į atitinkamą masyvą grupių masyve.
        for i in range(1, group_count+1):
            if participant.group == i:
                # Jeigu dalyvio grupė yra pirma, jo grupių masyvo indeksas atitinkamai bus 0. Jei antra, indeksas bus 1 ir t.t.
                groups[i-1].append(participant)

    # Einama per grupių skaičiaus aibę.
    for i in range(1, group_count+1):
        # Einama per kiekvieną grupę, iš jos atrenkant pusę mažiausiai laiko turinčių dalyvių.
        for j, _ in enumerate(groups[i-1]):
            if j == len(groups[i-1]) // 2 - 1:  # // operatorius dalina be liekanos. Jei yra 5 dalyviai, atrinkti bus 2.
                continue    # Jeigu pereinama per visą galimą dalyvių kiekį, einama į kitą grupę.
            chosen = min(groups[i-1], key=lambda participant: participant.time) # Randamas mažiausiai laiko turintis dalyvis.
            # Dalyvis yra įdedamas į rezultatų masyvą ir pašalinamas iš atitinkamos grupės masyvo, kad vėl būtų galima ieškoti mažiausiai laiko turinčio dalyvio.
            results.append(chosen)
            groups[i-1].remove(chosen)

    # Rezultatų masyvas išrikiuojamas didėjančia tvarka pagal dalyvių laiką.
    results = sorted(results, key=lambda participant: participant.time)
    # Naudojant funkciją, surašomi rezultatai.
    write_result(results)
        
# Šaukiama pagrindinė funkcija.
if __name__ == '__main__':
    main()
