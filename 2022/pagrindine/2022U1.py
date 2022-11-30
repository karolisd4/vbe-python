def main():
    with open('./2022/U1.txt') as f:
        duomenys = f.read().split('\n')

    uzdaviniu_taskai = [int(x) for x in duomenys[2] if x != ' ']
    uzdaviniu_laikas = [int(x) for x in duomenys[1].split()]
    dalyviai = [x for x in duomenys[3:]]

    rezultatas = []
    isspresti = []
    maziausi_taskai = []

    for index, i in enumerate(dalyviai):
        issprestu_uzd_skaicius = 0
        gauti_taskai = 0
        sugaistas_laikas = 0
        daugiausia_tasku = []
        rezultatai = []

        vardai = ''.join([x for x in i if not x.isdigit()])
        for eile in vardai.split('\n'):
            vardas = eile.rstrip()

        for dalyvis in dalyviai[index].split():
            if dalyvis.isdigit():
                rezultatai.append(int(dalyvis))

        for dalyvio_laikas, resultato_laikas, taskas in zip(rezultatai, uzdaviniu_laikas, uzdaviniu_taskai):
            sugaistas_laikas += dalyvio_laikas

            if dalyvio_laikas > resultato_laikas and dalyvio_laikas != 0:
                gauti_taskai += taskas // 2
                issprestu_uzd_skaicius += 1

            elif dalyvio_laikas <= resultato_laikas and dalyvio_laikas != 0:
                gauti_taskai += taskas
                issprestu_uzd_skaicius += 1

        maziausi_taskai.append(gauti_taskai)
        daugiausia_tasku.append(gauti_taskai)

        isspresti.append(issprestu_uzd_skaicius)

        if gauti_taskai <= min(maziausi_taskai):
            maziausiai_tasku_surinkes_zmogus = vardas

        rez_string = f'{vardas} {issprestu_uzd_skaicius} {sugaistas_laikas}'

        if issprestu_uzd_skaicius == max(isspresti):
            rezultatas.insert(0, rez_string)
        else:
            rezultatas.append(rez_string)

    with open('./2022/U1rez.txt', 'w') as f_rez:
        f_rez.write(f'{max(daugiausia_tasku)}\n')
        for rez in rezultatas:
            if maziausiai_tasku_surinkes_zmogus in rez:
                continue
            f_rez.write(rez + '\n')


if __name__ == '__main__':
    main()
