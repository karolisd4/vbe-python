def main():
    sunkiausia_kuprine = 0
    kiek_lengvesniu_kupriniu = 0

    with open('./2016/pagrindine/2016U1.txt', 'r') as f:
        duom = f.readlines()[1:]
        for kuprine in duom:
            kuprine = int(kuprine.strip())
            if kuprine > sunkiausia_kuprine:
                sunkiausia_kuprine = int(kuprine)
        for kuprine in duom:
            kuprine = int(kuprine.strip())
            if kuprine != sunkiausia_kuprine and kuprine * 2 >= sunkiausia_kuprine:
                kiek_lengvesniu_kupriniu += 1

    with open('./2016/2016U1rez.txt', 'w') as f:
        f.write(f'{str(sunkiausia_kuprine)} {str(kiek_lengvesniu_kupriniu)}')


main()