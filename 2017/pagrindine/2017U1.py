def nustatyti(pirmas, antras):
    sesioliktainis = {10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'}

    for v in sesioliktainis:
        if pirmas == v:
            pirmas_skaitmuo = sesioliktainis[v]
        if antras == v:
            antras_skaitmuo = sesioliktainis[v]
    if pirmas == 0:
        pirmas_skaitmuo = 0
    if antras == 0:
        antras_skaitmuo = 0
    if pirmas in range(10):
        pirmas_skaitmuo = pirmas
    if antras in range(10):
        antras_skaitmuo = antras
        
    return str(pirmas_skaitmuo), str(antras_skaitmuo)


def gauti_sesioliktaini_skaiciu(rgb):
    res = ''
    rgb = [int(sk) for sk in rgb.split(' ')]

    for spalva in rgb:
        pirmas_skaitmuo, antras_skaitmuo = nustatyti(spalva // 16, spalva % 16)
        res += pirmas_skaitmuo + antras_skaitmuo
    
    return res


def main():
    with open('./2017/pagrindine/U1.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
        ilgis, plotis = (int(sk) for sk in duomenys[0].split(' '))
        duomenys.pop(0)
    
    assert 1<=ilgis<=10000
    assert 1<=plotis<=10000

    ilgio = []
    plocio = []

    for rgb in duomenys[:3]:
        sesioliktainis = gauti_sesioliktaini_skaiciu(rgb)
        ilgio.append(sesioliktainis)
    for rgb in duomenys[3:]:
        sesioliktainis = gauti_sesioliktaini_skaiciu(rgb)
        plocio.append(sesioliktainis)
    
    with open('./2017/pagrindine/U1rez.txt', 'w') as f:
        f.write(f'{ilgio[0]};{ilgio[1]};{ilgio[2]}\n')
        f.write(f'{plocio[0]};{plocio[1]};{plocio[2]}')


main()
