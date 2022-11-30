def main():
    with open('./2014/pagrindine/U1.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
        skyriu_sk = int(duomenys[0])
        duomenys.pop(0)
    if skyriu_sk < 1 or skyriu_sk > 10:
        return
    dir_pirmam, dir_antram, dir_treciam = duomenys[-1].split(' ')
    duomenys.pop(-1)

    pirmu_balai = 0
    antru_balai = 0
    treciu_balai = 0
    skyrius = {1: 0,
    2: 0,
    3: 0}

    for line in duomenys:
        pirmi, antri, treti = line.split(' ')
        pirmu_balai += int(pirmi)
        antru_balai += int(antri)
        treciu_balai += int(treti)

    for line in duomenys:
        pirmi, antri, treti = line.split(' ')
        pirmi = int(pirmi)
        antri = int(antri)
        treti = int(treti)
        if pirmi > antri and pirmi > treti:
            skyrius[1] += 4
        elif antri > pirmi and antri > treti:
            skyrius[2] += 4
        elif treti > pirmi and treti > antri:
            skyrius[3] += 4
        elif pirmi == antri:
            skyrius[1] += 2
            skyrius[2] += 2
        elif pirmi == treti:
            skyrius[1] += 2
            skyrius[3] += 2
        elif antri == treti:
            skyrius[2] += 2
            skyrius[3] += 2

    laimetojas = [value for value in skyrius if skyrius[value]==max(skyrius.values())][0]

    for i in range(1, 4):
        if i != laimetojas:
            if max(skyrius.values()) == skyrius[i]:
                if i == 1:
                    skyrius[i] += dir_pirmam
                elif i == 2:
                    skyrius[i] += dir_antram
                elif i == 3:
                    skyrius[i] += dir_treciam

    laimetojas = [value for value in skyrius if skyrius[value]==max(skyrius.values())][0]

    with open('./2014/pagrindine/U1rez.txt', 'w') as f:
        f.write(f'{str(pirmu_balai)} {str(antru_balai)} {str(treciu_balai)}\n')
        f.write(f'{skyrius[1]} {skyrius[2]} {skyrius[3]}\n{laimetojas}')


main()