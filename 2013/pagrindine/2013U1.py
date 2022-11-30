def main():
    with open('./2013/pagrindine/U1.txt', 'r', encoding='UTF-8') as f:
        lines = [line.strip() for line in f.readlines()]
    kilometru_limitas = lines[0].split(' ')[1]
    lines.pop(0)
    nuvaziuoti_km = 0
    pavadinimai = []
    for i, line in enumerate(lines):
        pavadinimas = line[:10]
        x, y = line[10:].split(' ')
        pavadinimai.append(pavadinimas)
        x = abs(int(x)) * 2
        y = abs(int(y)) * 2
        if nuvaziuoti_km + x >= int(kilometru_limitas) or nuvaziuoti_km + y >= int(kilometru_limitas):
            break
        nuvaziuoti_km += x +  y

    with open('./2013/pagrindine/U1rez.txt', 'w', encoding='UTF-8') as f:
        f.write(f'{str(i)} {str(nuvaziuoti_km)} {pavadinimai[i - 1]}')


main()