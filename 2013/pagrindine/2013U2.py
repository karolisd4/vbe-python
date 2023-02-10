def main():
    with open('./2013/pagrindine/U2.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]    # Perskaitomi duomenys, pasalinami nereikalingi tarpai.
    miestu_sk = int(lines[0])
    assert 1<=miestu_sk<=103    # Tikrinama, ar miestu skaicius atitinka salyga.
    lines.pop(0)    # Istrinamas pirmas elementas (miestu skaicius), nes jo nereikia.

    # Sukuriamas masyvas ir zodynai duomenims saugoti.
    apskritys = []
    apskriciu_duom = {}
    miestu_duom = {}

    # Einama per kiekviena eilute, atitinkamose pozicijose randami miestu pavadinimai, apskriciu pavadinimai ir gyventoju skaiciai.
    for line in lines:
        miestas = line[:20].strip()
        apskritis = line[20:33].strip()
        gyventoju_sk = line[33:].strip()
        assert 100<=int(gyventoju_sk)<=600000   # Tikrinama, ar gyventoju skaicius atitinka salyga.
        # Sudedami duomenys apie mietus ir apskritis i ju masyvus.
        miestu_duom[miestas] = int(gyventoju_sk)
        apskritys.append(apskritis)

    # Is apskriciu masyvo pasalinami visi duplikatai, lieka tik unikalus elementai su set() funkcija.
    apskritys = set(apskritys)
    apskriciu_sk = str(len(apskritys))

    # Einama per visas apskritis ir eilutes duomenyse.
    for apskritis in apskritys:
        # Kiekvienai apskriciai atsikirai sukuriamas tuscias masyvas.
        apskrities_info = []
        for line in lines:
            # Randama informacija apie miesta, apskriti.
            miestas = line[:20].strip()
            apskritis_line = line[20:33].strip()
            gyventoju_sk = line[33:].strip()
            if apskritis == apskritis_line:
                # Jeigu dabartine apskritis sutampa su apskritimi pirmame for cikle, i informacijos masyva idedamas atitinkamas miestas ir jo gyventoju skaicius.
                apskrities_info.append(f'{miestas} {gyventoju_sk}')
        # I apskriciu zodyna idedama apskritis ir jos informacijos masyvas su miestais ir ju gyventoju skaiciais.
        apskriciu_duom.setdefault(apskritis, apskrities_info)

    # Einama per apskritis ir ju informacijos masyvus.
    for apskritis in apskritys:
        gyventoju_info = []
        for value in apskriciu_duom[apskritis]:
            # Randamas miestas ir jo gyventoju skaicius, kiekvieno miesto gyventoju skaiciai sudedami i masyva. 
            miestas, gyventoju_sk = value.split(' ')
            gyventoju_info.append(int(gyventoju_sk))
        # I apskriciu duomenu masyva idedamas maziausias gyventoju skaicius is visu miestu ir gyventoju skaiciu suma.
        apskriciu_duom[apskritis] = min(gyventoju_info), sum(gyventoju_info)

    # Surikiuojamas duomenu zodynas didejimo tvarka. Jei gyventoju skaiciai vienodi, bus rikiuojama abeceliskai.
    apskriciu_duom = sorted(apskriciu_duom.items(), key=lambda x: x[::-1])

    # Surasomi rezultatai.
    with open('./2013/pagrindine/U2rez.txt', 'w') as f:
        f.write(f'{apskriciu_sk}\n')
        for data in apskriciu_duom:
            # Duomenu zodyne randama visa reikalinga informacija, naudojant indeksus.
            pavadinimas = data[0]
            min_gyv_sk = str(data[1][0])
            gyv_sk = str(data[1][1])
            # Pavadinimui duodama 13 poziciju.
            f.write(f'{pavadinimas:<13} {min_gyv_sk} {gyv_sk}\n')

# Pagrindine funkcija.
if __name__ == '__main__':
    main()
