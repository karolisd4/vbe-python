class Participant():
    '''Klasė, kurioje laikomas dalyvių poros vardas ir taškų suma. Klasė turi funkcija, kuri pagal sąlygą skaičiuoja
    dalyvių taškų sumą.'''
    def __init__(self, name: str):
        self.name = name
        self.total_pts = 0
    
    def get_point_sum(self, points: list) -> None:
        '''Pagal sąlygą iš taškų atimamas vienas mažiausias ir vienas didžiausias balas, o tada randama taškų suma.'''
        points.remove(max(points))
        points.remove(min(points))
        self.total_pts += sum(points)


def read_data() -> list:
    with open('./2011/pagrindine/U2.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]    # Perskaitomi duomenys ir sudedami į masyvą, pašalinant nereikalingus tarpus.
    return lines


def sort_data(data: list) -> list:
    '''Rikiuojama masyvą mažėjančia tvarka pagal dalyvių taškų sumos skaičių.'''
    return sorted(data, reverse=True, key=lambda participant: participant.total_pts)


def main():
    lines = read_data()
    # Randamas porų ir teisėjų skaičius, pašalinamas iš masyvo ir tikrinama, ar atitinka sąlygą.
    pair_count, judge_count = lines[0].split(' ')
    lines.pop(0)
    assert 1 <= int(pair_count) <= 100
    assert 3 <= int(judge_count) <= 10

    participants = []   # Sukuriamas tuščias masyvas dalyvių objektams saugoti.

    # Einama per duomenų masyvą, visad laikant esamą indeksą.
    for i, line in enumerate(lines):
        # Vardas visad bus esama linija.
        name = line
        if i % 3 == 0:  # Kas 3 skaičių prasideda nauja dalyvių pora, tad randami skaičiai, kurie dalinasi iš 3 su % operatorium.
            # Pagal indeksus randami taškai už techniką ir artistiškumą, jie paverčiami į int tipą ir sudedami į masyvus.
            technic_pts = [int(point) for point in lines[i+1:i+2][0].split(' ')]
            artistry_pts = [int(point) for point in lines[i+2:i+3][0].split(' ')]
            # Sukuriamas dalyvio objektas, naudojantis funkcija suskaičiuojamos jų taškų sumos.
            participant = Participant(name)
            participant.get_point_sum(technic_pts)
            participant.get_point_sum(artistry_pts)
            # Į dalyvių masyvą sudedama dalyvių objektai.
            participants.append(participant)

    # Naudojantis funckija surikiuojama dalyvių informacija.
    participants = sort_data(participants)
    with open('./2011/pagrindine/U2rez.txt', 'w') as f:
        for participant in participants:
            # Surašomi rezultatai, duodant dalyvio vardui 20 simbolių.
            f.write(f'{participant.name:<20} {participant.total_pts}\n')


# Šaukiama pagrindinė funkcija.
if __name__ == '__main__':
    main()
