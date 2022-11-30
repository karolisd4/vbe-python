def main():
    with open('./2013/2013U2.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    lines.pop(0)

    apskritys = []
    apskriciu_duom = {}
    miestu_duom = {}

    for line in lines:
        miestas, apskritis, gyventoju_sk = line.split(' ')
        miestu_duom[miestas] = int(gyventoju_sk)
        apskritys.append(apskritis)

    apskritys = set(apskritys)
    apskriciu_sk = str(len(apskritys))

    for apskritis in apskritys:
        apskrities_info = []
        for line in lines:
            miestas, apskritis_line, gyventoju_sk = line.split(' ')
            if apskritis == apskritis_line:
                apskrities_info.append(f'{miestas} {gyventoju_sk}')
        apskriciu_duom[apskritis] = apskrities_info

    for apskritis in apskritys:
        gyventoju_info = []
        for value in apskriciu_duom[apskritis]:
            miestas, gyventoju_sk = value.split(' ')
            gyventoju_info.append(int(gyventoju_sk))
        apskriciu_duom[apskritis] = min(gyventoju_info), sum(gyventoju_info)
    gyventoju_info = []

    for value in apskriciu_duom.values():
        gyventoju_info.append(value[0])
        gyventoju_info = sorted(gyventoju_info)

    with open('./2013/2013U2rez.txt', 'w') as f:
        f.write(f'{apskriciu_sk}\n')
        for gyventoju_sk in gyventoju_info:
            apskritis = [i for i in apskriciu_duom if apskriciu_duom[i][0]==gyventoju_sk][0]
            gyventoju_sum = apskriciu_duom[apskritis][1]
            f.write(f'{apskritis} {gyventoju_sk} {gyventoju_sum}\n')


main()
