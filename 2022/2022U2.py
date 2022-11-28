def main():
    with open('./2022/U2.txt', 'r') as f:
        duomenys = [duom.strip() for duom in f.readlines()]
        kiek_dienu_sportavo = int(duomenys[0])
        duomenys.pop(0)
    if kiek_dienu_sportavo > 31 or kiek_dienu_sportavo < 1:
        return

    pratimai_duom = {}
    pratimu_pavadinimai = []
    dienos_metai = []

    for line in duomenys:
        start_index = 0
        end_index = 3
        dienos_duomenys = line.split(' ')
        kiek_kartu_sportavo = int(dienos_duomenys[0])
        dienos_duomenys.pop(0)
        for i in range(kiek_kartu_sportavo):
            pratimas, dienos_metas, laikas = dienos_duomenys[start_index:end_index]
            if pratimas not in pratimu_pavadinimai:
                pratimu_pavadinimai.append(pratimas)
            if dienos_metas not in dienos_metai:
                dienos_metai.append(dienos_metas)

            if pratimas not in pratimai_duom.keys():
                pratimai_duom[pratimas] = int(laikas)
            else:
                pratimai_duom[pratimas] += int(laikas)
            for dienos_metas_index in dienos_metai:
                if dienos_metas == dienos_metas_index and f'{pratimas} {dienos_metas_index}' not in pratimai_duom.keys():
                    pratimai_duom[f'{pratimas} {dienos_metas_index}'] = 1
                elif dienos_metas == dienos_metas_index and f'{pratimas} {dienos_metas_index}' in pratimai_duom.keys():
                    pratimai_duom[f'{pratimas} {dienos_metas_index}'] += 1
            
            start_index += 3
            end_index += 3

        for pratimas in pratimu_pavadinimai:
            if pratimas in dienos_duomenys and f'{pratimas} kiekis' not in pratimai_duom.keys():
                pratimai_duom[f'{pratimas} kiekis'] = 1
            elif pratimas in dienos_duomenys and f'{pratimas} kiekis' in pratimai_duom.keys():
                pratimai_duom[f'{pratimas} kiekis'] += 1
        
    with open('./2022/U2rez.txt', 'w') as f:
        for pratimas in sorted(pratimu_pavadinimai):
            f.write(f'{pratimas} {pratimai_duom[f"{pratimas} kiekis"]} {pratimai_duom[pratimas]}\n')
            for dienos_metas in dienos_metai:
                key = f'{pratimas} {dienos_metas}'
                if key not in pratimai_duom.keys():
                    pass
                else:
                    f.write(f'{dienos_metas} {pratimai_duom[key]}\n')


main()