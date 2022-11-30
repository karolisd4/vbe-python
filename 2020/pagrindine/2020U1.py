def gauti_zydejimo_intervalus(dienos: dict, didziausias_zydinciu_geliu_skaicius: int) -> str:
    
    def gauti_menesi_diena(dienos: int) -> int:
        if dienos <= 31:
            menesis = 6
            diena = dienos
        elif dienos > 31 and dienos <= 61:
            menesis = 7
            diena = dienos - 31
        elif dienos > 61 and dienos <= 92:
            menesis = 8
            diena = dienos - 61
        return menesis, diena

    zydejimu_laikotarpiai = []
    for diena in dienos:
        if dienos[diena] == didziausias_zydinciu_geliu_skaicius:
            zydejimu_laikotarpiai.append(diena)
    pirma_diena = zydejimu_laikotarpiai[0]
    paskutine_diena = zydejimu_laikotarpiai[-1]

    pr_menesis, pr_diena = gauti_menesi_diena(pirma_diena)
    pab_menesis, pab_diena = gauti_menesi_diena(paskutine_diena)
    
    pradzios_intervalas = f'{str(pr_menesis)} {str(pr_diena)}'
    pabaigos_intervalas = f'{str(pab_menesis)} {str(pab_diena)}'
    return pradzios_intervalas, pabaigos_intervalas


def gauti_zydejimo_duomenis(pr_menesis: int, pr_diena: int, pab_menesis: int, pab_diena: int, dienos: dict) -> dict:
    if pr_menesis == 6 and pab_menesis == 6:
        for i in range(pr_diena, pab_diena+1):
            dienos[i] += 1
    elif pr_menesis == 6 and pab_menesis == 7:
        for i in range(pr_diena, 31+pab_diena+1):
            dienos[i] += 1
    elif pr_menesis == 6 and pab_menesis == 8:
        for i in range(pr_diena, 61+pab_diena+1):
            dienos[i] += 1
    elif pr_menesis == 7 and pab_menesis == 7:
        for i in range(31+pr_diena, 31+pab_diena+1):
            dienos[i] += 1
    elif pr_menesis == 7 and pab_menesis == 8:
        for i in range(31+pr_diena, 61+pab_diena+1):
            dienos[i] += 1
    elif pr_menesis == 8:
        for i in range(61+pr_diena, 61+pab_diena+1):
            dienos[i] += 1

    return dienos


def main():
    with open('./2020/U1.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
        geliu_sk = int(duomenys[0])
        duomenys.pop(0)
    if geliu_sk < 1 or geliu_sk > 30:
        return

    dienos = {}
    for i in range(1, 93):
        dienos[i] = 0

    for line in duomenys:
        pr_menesis = int(line[5:6])
        pr_diena = int(line[7:9])
        pab_menesis = int(line[10:11])
        pab_diena = int(line[12:14])
        
        dienos = gauti_zydejimo_duomenis(pr_menesis, pr_diena, pab_menesis, pab_diena, dienos)

    didziausias_zydinciu_geliu_skaicius = max(dienos.values())
    pradzios_intervalas, pabaigos_intervalas = gauti_zydejimo_intervalus(dienos, didziausias_zydinciu_geliu_skaicius)

    with open('./2020/U1rez.txt', 'w') as f:
        f.write(f'{str(didziausias_zydinciu_geliu_skaicius)}\n{pradzios_intervalas}\n{pabaigos_intervalas}')


if __name__ == '__main__':
    main()
