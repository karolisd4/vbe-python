def sort_data(results: dict) -> dict:
    '''Rikiuoja zodyna abeceliskai ir pagal skaicius mazejancia tvarka.'''
    return sorted(results.items(), key=lambda x: (-x[1], x[0])) # Rikiuojamas skaicius paverciamas negatyviu, kad butu mazejimo tvarka.


def main():
    with open('./2020/pagrindine/U2.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()] # Perskaitomi duomenys, sudedami i masyva.
    fishermen_count = int(data[0])  # Gaunamas zveju skaicius, tikrinama, ar atitinka salyga.
    assert 1 <= fishermen_count <= 30

    # Sukuriami tusti zodynai ir kintamasis visai informacijai saugoti.
    rating_index = 0
    participants = {}
    ratings = {}
    fish_dict = {}
    results = {}

    # Einama per duomenu masyva kartu su indeksu.
    for i, line in enumerate(data):
        if i == 0:  # Pacia pirma eilute visad praleidziama - ji yra zveju skaicius
            continue
        if len(line) == 1 or len(line) == 2:    # Jeigu eilutes ilgis tik 1 ar 2 simboliai, prasideda vertinamu zuvu sarasas.
            rating_index = i    # Issaugomas indeksas, nuo kurio prasideda vertinamu zuvu sarasas.
            break
        name = line[:20].strip()    # Randamas vardas, zuvu skaicius
        fish_count = int(line[20:].strip())
        if fish_count > 30: continue    # Jeigu zuvu skaicius yra daugiau nei 30, t.y randama mase, ciklas nutraukiamas ir einama tolyn.
        else: participants.setdefault(name, []) # Jeigu zuvu skaicius maziau nei 30, zinoma, kad tai dalyvis ir jis idedamas i masyva.
        for fish in data[i+1:i+1+fish_count]: # Einama per zmogaus zuvu sarasa su duotu zuvu skaicium.
            fish_name = fish[:20].strip()
            fish_mass = int(fish[20:].strip())
            fish_dict.setdefault(fish_name, fish_mass)  # I zuvu masyva sudedamos zuvys ir sumuojama ju mase.
            participants[name].append((fish_name, fish_mass))   # Atitinkamam dalyviui sudedamos jo zuvys ir mases.

    # Einama per vertinamas zuvis, jos sudedamos i zodyna.
    for rating in data[rating_index+1:]:
        fish_name = rating[:20].strip()
        points = int(rating[20:].strip())
        ratings.setdefault(fish_name, points)
        fish_dict.setdefault(fish_name, 0)  # Jeigu zuvis anksciau buvo nepagauta, jos mase nustatoma i 0.
    
    # Einama per dalyvius ir ju zuvis, skaiciuojami taskai pagal salyga ir vertinamu zuvu zodyna.
    for name, fish_info in participants.items():
        results.setdefault(name, 0)
        for fish in fish_info:
            if fish[1] < 200:
                results[name] += 10
            elif fish[1] > 200:
                results[name] += 30
            results[name] += ratings[fish[0]]
    
    # Surikiuojami rezultatai ir zuvu informacija, naudojant funkcija.
    results = sort_data(results)
    fish_dict = sort_data(fish_dict)
    
    # Surasomi rezultatai.
    with open('./2020/pagrindine/U2rez.txt', 'w') as f:
        f.write('Dalyviai\n')
        for participant in results:
            f.write(f'{participant[0]:<20} {participant[1]}\n') # Pavadinimams duodama 20 simboliu.
        f.write('Laimikis\n')
        for fish in fish_dict:
            f.write(f'{fish[0]:<20} {fish[1]}\n')

# Pagrindine funkcija
if __name__ == '__main__':
    main()
