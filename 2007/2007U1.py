def find_most_mushrooms(days: dict) -> list[int, int]:
    # Sukuriamas masyvas su dviem skaičiais - dienos skaičius ir grybų skaičius.
    most = [0, 0]

    # Einama per žodyno elementus, randama grybų skaičių suma.
    for key, value in days.items():
        current_sum = sum(value)
        # Jeigu suma didesnė už esančią masyve, ji tampa didžiausia. Diena taip pat yra išsaugoma.
        if current_sum > most[1]:
            most[0] = key
            most[1] = current_sum
        # Jeigu yra kelios dienos su vienodais grybų skaičiais, randama mažiausio skaičiaus diena.
        elif current_sum == most[1]:
            most[0] = min(most[0], key)
            
    return most     # Grąžinamas masyvas.


def write_result(days: dict, most_shrooms: list) -> None:
    with open('./2007/U1rez.txt', 'w') as f:
        # Einama per išrikiuotą dienų sąrašą didėjančia tvarka.
        for day in sorted(days):
            f.write(f'{day} {" ".join([str(day) for day in days[day]])}\n')     # Įrašomas dienos numeris, grybų skaičiai paverčiami į string tipą.
        f.write(f'{" ".join([str(num) for num in most_shrooms])}')  # Didžiausio grybų skaičiaus masyvas paverčiamas į string, jo elementai paverčiami į string.


def main():
    with open('./2007/U1.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]    # Perskaitomi duomenys ir sudedami į masyvą, pašalinant nereikalingus tarpus.
    
    # Randamas skaičius, kiek kartų buvo eita grybauti, jis pašalinamas iš masyvo ir tikrinama, ar jo kiekis atitinka sąlygą.
    mushrooming_count = int(lines[0])
    lines.pop(0)
    assert 1 <= mushrooming_count <= 100

    days = {}   # Sukuriamas tuščias žodynas dienų informacijai saugoti.

    for line in lines:
        # Suformatuojama eilutė - gražiai, pašalinant tarpus randama visa reikalinga informacija, viskas paverčiama į int tipą.
        day_num, boletus, leccinum, scaber_stalk = [int(line) for line in line.split(' ') if line != '']
        assert 1 <= day_num <= 31   # Tikrinama, ar dienų kiekis atitinka sąlygą.
        
        # Bandoma prie dienos value žodyne pridėti grybų skaičius į jiems atitinkamus indeksus.
        try:
            days[day_num][0] += boletus
            days[day_num][1] += leccinum
            days[day_num][2] += scaber_stalk
        except KeyError: pass   # Jeigu žodyno elementas dar neegzistuoja, gaunama KeyError klaida ir ji praleidžiama.

        # Į žodyną pirmą kartą įdedama diena ir jos grybų skaičiai.
        days.setdefault(day_num, [boletus, leccinum, scaber_stalk])

    # Šaukiama funckija, randama diena su daugiausia grybų ir tos dienos grybų skaičius.
    most_shrooms = find_most_mushrooms(days)

    # Šaukiama funkcija, kuri surašo rezultatus į rezultatų failą.
    write_result(days, most_shrooms)


# Šaukiama pagrindinė funkcija.
if __name__ == '__main__':
    main()