def main():
    with open('./2005/DUOM.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
    nuskaityt_sugaista, atsiskaityt_sugaista = duomenys[0].split()[0:2]
    duomenys.pop(0)
    duomenys = [int(line) for line in duomenys]
    daugiausia_prekiu_pirkejo_eile = duomenys.index(max(duomenys)) + 1
    daugiausia_prekiu_sk = max(duomenys)
    sugais_atsiskaityt = int(atsiskaityt_sugaista) * daugiausia_prekiu_sk
    kasininke_sugais = (int(nuskaityt_sugaista) * daugiausia_prekiu_sk) + int(atsiskaityt_sugaista)
    with open('./2005/REZ.txt', 'w') as f:
        f.write(f'{str(daugiausia_prekiu_pirkejo_eile)} {daugiausia_prekiu_sk} {sugais_atsiskaityt} {kasininke_sugais}')

main()