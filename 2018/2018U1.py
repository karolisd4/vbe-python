from math import floor

def main():
    with open('./2018/U1.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
        kruveliu_skaicius = int(duomenys[0])
        duomenys.pop(0)
    if kruveliu_skaicius < 1 or kruveliu_skaicius > 30:
        return
    juosteliu_duom = {}

    for line in duomenys:
        spalva, juosteliu_kiekis = line.split(' ')
        if spalva not in juosteliu_duom.keys():
            juosteliu_duom[spalva] = int(juosteliu_kiekis)
        else:
            juosteliu_duom[spalva] += int(juosteliu_kiekis)
    veliaveliu_skaicius = str(floor(min(juosteliu_duom.values()) / 2))

    with open('./2018/U1rez.txt', 'w') as f:
        maziausias_juost_sk = min(juosteliu_duom.values())
        f.write(f'''{veliaveliu_skaicius}
G = {juosteliu_duom['G'] - maziausias_juost_sk}
Z = {juosteliu_duom['Z'] - maziausias_juost_sk}
R = {juosteliu_duom['R'] - maziausias_juost_sk}''')


main()