import datetime     # Importuojama datetime biblioteka, kad būtų lengvai galima skaičiuoti laiką.


def read_data() -> list:
    with open('./2006/U2.txt', 'r', encoding='UTF-8') as f:     # UTF-8 encoding dėl lietuviškų raidžių.
        lines = [line.strip() for line in f.readlines()]     # Perskaitomi duomenys ir sudedami į masyvą, pašalinant nereikalingus tarpus.
    return lines


def write_data(data: dict) -> None:
    with open('./2006/U2rez.txt', 'w', encoding='UTF-8') as f:  # UTF-8 encoding dėl lietuviškų raidžių.
        # Einama per žodyną, miestui duodama 15 simbolių ir įrašomas laikas.
        for city in data:
            f.write(f'{city:<15} {data[city]}\n')


def main():
    lines = read_data()     # Perskaitomi duomenys ir gaunamas masyvas su jais.
    stop_count, avg_vel, dep_h, dep_min = [int(num) for num in lines[0].split(' ')]     # Pirmos eilutės duomenys paverčiami į int tipą.
    dep_time = datetime.timedelta(hours=dep_h, minutes=dep_min)
    
    assert 1 <= stop_count <= 100   # Tikrinama, ar stotelių skaičius atitinka sąlygą.

    def get_time(distance: float) -> float:
        '''Atrandamas laikas minutėmis pagal formulę t = s / v * 60, kur duotas kelias s ir greitis v.'''
        return distance / avg_vel * 60

    cities = {}     # Sukuriamas tuščias žodynas rezultatams saugoti.

    # Einama per kiekvieną duomenų eilutę, išskyrus pirmąją, nes ji jau perskaityta.
    for line in lines[1:]:
        city = line[:15].strip()    # Pirmi 15 simbolių - miesto pavadinimas.
        distance = float(line[15:].strip())     # Toliau - kelias.
        time = get_time(distance)   # Naudojamasi funkcija, kad gauti laiką minutėmis.
        dep_time += datetime.timedelta(minutes=time)   # Prie išvykimo laiko timedelta objekta pridedamas naujas timedelta objektas su gautomis minutėmis.
        hour, minute, _ = str(dep_time).split(':')  # Timedelta paverčiamas į string, randamos valandos ir minutės, o sekundės nereikalingos, tad žymimos _.
        if minute == '00': minute = '0'     # Dėl rezultatų - jeigu minutės yra 0, jos bus rašomos su vienu nuliu (0), ne dviem (00).
        res_str = f'{hour} val. {minute} min.'  # Sukuriamas rezultato string ir viskas sudedama į rezultatų žodyną.
        cities.setdefault(city, res_str)

    # Naudojantis funckija, viskas surašoma į rezultatų failą.
    write_data(cities)


# Šaukiama pagrindinė funkcija.
if __name__ == '__main__':
    main()