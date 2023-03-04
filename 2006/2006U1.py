def main():
    with open('./2006/U1.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]    # Perskaitomi duomenys ir sudedami į masyvą, pašalinant nereikalingus tarpus.
    
    # Randamas grandinės dalių skaičius, jis pašalinamas iš masyvo ir tikrinama, ar jo kiekis atitinka sąlygą.
    circuit_parts = int(lines[0])
    lines.pop(0)
    assert 1 <= circuit_parts <= 100

    sums = []   # Tuščias masyvas, kuriama bus saugomos visų grandinės dalių bendros varžos.

    # Einama per kiekvieną eilutę duomenyse.
    for line in lines:
        # Pradedama eiti nuo 1 indekso, nes pirmas indeksas yra varžų skaičius, tad jo nereikia.
        resistances = [int(resistance) for resistance in line.split(' ')[1:]]   # Kiekvienas skaičius paverčiamas į int tipą su list comprehension.
        sums.append(sum([1 / resistance for resistance in resistances]))    # Į anksčiau sukurtą masyvą įdedama varžų 1/R suma.

    result = str(round(sum([1 / resistance for resistance in sums]), 2))    # Einama per kiekvieną sumą, vienas dalinamas iš jos, viskas susumuojama ir apvalinama iki šimtųjų.
    
    with open('./2006/U1rez.txt', 'w') as f:
        f.write(result)     # Rezultatas įrašomas į rezultatų failą.
 

# Šaukiama pagrindinė funkcija.
if __name__ == '__main__':
    main()