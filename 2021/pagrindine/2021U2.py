def rusiuoti(mok_duom):
    rez_duom = {}
    mok_skaiciai = []

    for mokinys in mok_duom.items():
        mok_skaiciai.append(len(mokinys[1]))
        mok_duom[mokinys[0]].insert(0, len(mokinys[1]))

    for mok_skaicius in mok_skaiciai:
        for i in sorted(mok_duom):
            if mok_duom[i][0] == mok_skaicius:
                rez_duom.setdefault(i, (mok_duom[i][0], mok_duom[i][1:]))

    return rez_duom


def main():
    with open('./2021/pagrindine/U2.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
        mok_sk = int(duomenys[0])

    mok_duom = {}

    for i in range(mok_sk):
        info = duomenys[i+1].split(' ')
        vardas, dalykas = info[0:2]
        pazymiai = [int(pazymys) for pazymys in info[3:]]
        vidurkis = sum(pazymiai) / len(pazymiai)
        if vidurkis >= 9:
            mok_duom.setdefault(dalykas, []).append(vardas)

    if not mok_duom:
        with open('./2021/pagrindine/U2rez.txt', 'w') as f:
            f.write('Neatitinka vidurkis')
            return
            
    mok_duom = rusiuoti(mok_duom)

    with open('./2021/pagrindine/U2rez.txt', 'w') as f:
        for duom in mok_duom:
            f.write(f'{duom} {mok_duom[duom][0]}\n')
            f.write('\n'.join(mok_duom[duom][1]) + '\n')
    
    
if __name__ == '__main__':
    main()