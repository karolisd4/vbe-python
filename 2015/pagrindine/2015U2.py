class Sheep():
    def __init__(self, name: str, dna_fragment: list):
        # Inicijuojamas objektas su duotu vardu ir DNR fragmentu
        self.name = name
        self.dna_fragment = dna_fragment

    def get_coefficient(self, other_fragment: list) -> int:
        coefficient = 0
        for own_nucleodite, other_nucleotide in zip(self.dna_fragment, other_fragment):  # Einama per abu fragmentus vienu metu
            if own_nucleodite == other_nucleotide:  # Jei nukleotidai sutampa, koeficientas padidedja vienetu
                coefficient += 1
        return coefficient


def read_data() -> list:
    with open('./2015/pagrindine/U2.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]     # Duomenys sukeliami i masyva, pasalinami nereikalingi tarpai, jei tokiu yra
    return data


def write_data(data: str) -> None:
    with open('./2015/pagrindine/U2rez.txt', 'w') as f:
        f.write(data)


def sort_data(results: dict[str, int]) -> str:
    # Sukuriamas tuscias zodynas ir string rezultatams saugoti
    sorted_results = {}
    result_string = ''

    for value in sorted(results.values(), reverse=True):    # Surikiuojami koeficientai mazejimo tvarka
        for key, second_value  in sorted(results.items()):  # Surikiuojami aviu vardai abeceles tvarka
            if value == second_value:   # Jeigu koeficientai sutampa, rezultatai irasomi i rezultatu zodyna
                sorted_results.setdefault(key, results[key])

    # Rezultatai sudedami i string, kad butu lengvai galima surasyti i rezultatu faila
    for key, value  in sorted(sorted_results.items()):
        result_string += f'{key} {value}\n'

    return result_string.strip()  # .strip() pasalina paskutini newline


def main():
    data = read_data()
    sheep_count, fragment_length = data[0].split(' ')   # Randamas aviu skaicius ir DNR fragmento ilgis
    
    # Tikrinama, ar duoti skaiciai yra salygos intervale
    assert 2<=int(sheep_count)<=20    
    assert 4<=int(fragment_length)<=20

    # Paimama tiriama avis, sukuriamas jos objektas ir ji pasalinama is duomenu masyvo
    studied_sheep_data = data[int(data[1]) + 1]
    studied_sheep = Sheep(studied_sheep_data[:10].strip(), list(studied_sheep_data[10:].strip()))
    data.remove(studied_sheep_data)

    # Sukuriamas tuscias masyvas ir zodynas rezultatams bei aviu objektams saugoti
    sheep_list = []
    results = {}

    for sheep_data in data[2:]:
        name = sheep_data[:10].strip()  # Randamas vardas pirmose 10 poziciju
        dna_fragment = list(sheep_data[10:].strip())    # Viskas toliau - DNR fragmentas
        sheep = Sheep(name, dna_fragment)   # Sukuriamas avies objektas su gauta informacija, jis idedamas i masyva
        sheep_list.append(sheep)

    # Einama per objektus, gaunamas koeficientas ir rezultatai sudedami i zodyna
    for sheep in sheep_list:
        coefficient = sheep.get_coefficient(studied_sheep.dna_fragment)
        results.setdefault(sheep.name, coefficient)

    # Surikiuojami rezultatai ir irasomi i rezultatu faila
    results = sort_data(results)
    write_data('\n'.join((studied_sheep.name, results)))    # I pradzia idedamas tiriamas avies vardas


if __name__ == '__main__':
    main()