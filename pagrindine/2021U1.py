from datetime import timedelta


def kiek_sugaiso_laiko(rytas, vakaras):
    rytas = [int(laikas) for laikas in rytas]
    vakaras = [int(laikas) for laikas in vakaras]
    if vakaras == [0, 0, 0, 0] or rytas == [0, 0, 0, 0]:
        return None

    rytas_pr_h, rytas_pr_min, rytas_pab_h, rytas_pab_min = rytas
    vakaras_pr_h, vakaras_pr_min, vakaras_pab_h, vakaras_pab_min = vakaras

    ryto_laikas = timedelta(hours=rytas_pab_h, minutes=rytas_pab_min) - timedelta(hours=rytas_pr_h, minutes=rytas_pr_min)
    vakaro_laikas = timedelta(hours=vakaras_pab_h, minutes=vakaras_pab_min) - timedelta(hours=vakaras_pr_h, minutes=vakaras_pr_min)
    total_laikas = int(str(ryto_laikas + vakaro_laikas).split(':')[1])

    return total_laikas
    

def main():
    with open('./2021/pagrindine/U1.txt', 'r') as f:
        duomenys = [line.split() for line in f.readlines()]
        dienu_sk = int(duomenys[0][0])
    if dienu_sk < 1 or dienu_sk > 31:
        return
    laurynas = {}

    for diena in range(dienu_sk):
        men_diena = int(duomenys[diena+1][0])
        rytas = duomenys[diena+1][1:5]
        vakaras = duomenys[diena+1][5:]
        res = kiek_sugaiso_laiko(rytas, vakaras)
        if res:
            if men_diena in laurynas.values(): laurynas[men_diena] += res
            else: laurynas[men_diena] = res

    maziausias_laikas = min(laurynas.values())
    maz_dienos = []
    for dienos_info in laurynas.items():
        if dienos_info[1] == maziausias_laikas:
            maz_dienos.append(str(dienos_info[0]))

    with open('./2021/pagrindine/U1rez.txt', 'w') as f:
        f.write(f'Minimalus laikas\n{maziausias_laikas}\nDienos\n{" ".join(maz_dienos)}')
        

main()