def main():
    with open('./2005/2005u1.dat', 'r') as f:
        skaiciai = [int(skaicius.strip()) for skaicius in f.readlines()]

    tinkami_skaiciai = []
    for skaicius in skaiciai:
        if skaicius % 2 == 0 and (skaicius ** 0.5).is_integer():
            tinkami_skaiciai.append(skaicius)

    with open('./2005/2005u1.rez', 'w', encoding='UTF-8') as f:
        if not tinkami_skaiciai:
            f.write('Nėra')
        else:
            f.write('Surasti skaičiai:\n')
            for skaicius in tinkami_skaiciai:
                f.write(str(skaicius) + '\n')
            f.write(f'Iš viso:\n{len(tinkami_skaiciai)}')


if __name__ == '__main__':
    main()