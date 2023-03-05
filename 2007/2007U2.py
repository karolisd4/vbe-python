def write_data(data: dict, most: tuple[str, int]) -> None:
    with open('./2007/U2rez.txt', 'w') as f:
        for person in data:
            # Einama per rezultatų žodyną, varduo duodama 15 simbolių.
            f.write(f'{person:<15}')
            # Toliau einama per to žmogaus grybus, kiekvienam skaičiui duodami 5 simboliai.
            for mushroom in data[person]:
                f.write(f'{mushroom:>5}')
            # Surašius vardą ir grybus, dedama nauja eilutė ir kartojama, kol nelieka grybautojų.
            f.write('\n')
        # Įrašomas daugiausia grybų surinkęs grybautojas, vardui duodama 15 simbolių, įrašomas jo grybų skaičius.
        f.write(f'{most[0]:<15} {most[1]}')


def read_data() -> list:
    with open('./2007/U2.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]    # Perskaitomi duomenys ir sudedami į masyvą, pašalinant nereikalingus tarpus.
    return lines


def most_mushrooms(data: dict) -> tuple[str, int]:
    '''Funkcija randa grybautoją, turintį daugiausiai grybų. Jeigų tokių yra keli, visad bus grąžinamas anksčiausiai duomenyse
    pasirodęs grybautojas.'''

    # Sukuriami tušti kintamieji saugoti grybų sumai ir grybautojo vardui.
    most = 0
    most_person = ''
    
    # Einama per grybautojus - jeigu grybų suma yra didesnė už išsaugotą, ji tampa didžiausia. Išsaugomas ir vardas.
    for person in data:
        if sum(data[person]) > most:
            most = sum(data[person])
            most_person = person
            
    return (most_person, most)  # Grąžinamas tuple objektas su (vardas, grybų skaičius).
    

def main():
    lines = read_data()     # Perskaitomi duomenys ir gaunamas masyvas su jais.

    # Grybautojų skaičius randamas, pašalinamas iš masyvo ir tikrinama, ar atitinka sąlygą.
    participant_count = int(lines[0])
    lines.pop(0)
    assert 1 <= participant_count <= 100

    participants = {}   # Sukuriamas tuščias žodynas, kuriame bus saugomi grybautojai ir jų grybai.

    # Einama per duomenų eilutes, visad saugant esamą indeksą.
    for i, line in enumerate(lines):
        name = line[:15].strip()    # Vardas yra pirmos 15 pozicijų.

        # Bandoma rasti grybautojo grybavimų skaičių. Jei tokio nėra, gaunama ValueError klaida ir ciklas praleidžaimas.
        try: count = int(line[15:].strip())
        except ValueError: continue

        # Grybautojai įdedami į žodyną su masyvu, kuris turi tris skaičius, kurie pradžioje yra 0.
        participants.setdefault(name, [0, 0, 0])

        # Jeigu ciklas buvo nepraleistas, einama per grybautojo grybus pagal duotą grybavimų skaičių ir esamą indeksą.
        for mushrooms in lines[i+1:i+count+1]:
            # Randami ir paverčiami į int tipą grybų skaičiai bei susumuojami į atitinkamas grybautojo masyvo vietas.
            boletus, leccinum, scaber_stalk = [int(num) for num in mushrooms.split(' ')]
            participants[name][0] += boletus
            participants[name][1] += leccinum
            participants[name][2] += scaber_stalk
    
    # Naudojantis funkcijomis, randamas geriausias grybautojas ir rezultatai surašomi į rezultatų failą.
    most = most_mushrooms(participants)
    write_data(participants, most)



# Šaukiama pagrindinė funkcija.
if __name__ == '__main__':
    main()