def main():
    with open('./2016/2016U2.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
        kiek_dienu_vedziojo = duomenys[0]
        duomenys.pop(0)
    if len(duomenys) < int(kiek_dienu_vedziojo) or int(kiek_dienu_vedziojo) > 30 or int(kiek_dienu_vedziojo) < 1:
        return

    parku_duom = {}

    for line in duomenys:
        parkas = line[:20].strip()
        kiek_laiko = int(line[20:].strip())
        if parkas in parku_duom.keys():
            parku_duom[parkas] += kiek_laiko
        else:
            parku_duom[parkas] = kiek_laiko

    with open('./2016/2016U2rez.txt', 'w') as f:
        for parkas in parku_duom:
            kiek_laiko_ejo = str(parku_duom[parkas])
            f.write(f'{parkas} {kiek_laiko_ejo}\n')


main()