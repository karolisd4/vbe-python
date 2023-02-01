def exchange(student_money: int, denominations: list[int]) -> dict:
    received = {}
    for denomination in denominations:
        receive = student_money // denomination
        student_money -= receive * denomination
        received.setdefault(denomination, receive)
    return received


def main():def exchange(student_money: int, denominations: list[int]) -> dict:
    # Sukuriamas tuščias žodynas, kuriame bus saugoma nominalų informacija. {nominalas: kiekis}
    received = {}
    # Einama per kiekvieną nominalą ir naudojamas // dalybos operatorius, kad gauti skaičių be liekanos. Taip randamas maksimalus reikiamų monetų kiekis.
    for denomination in denominations:
        receive = student_money // denomination
        # Atnaujinama turimų pinigų suma ir informacija sudedama į žodyną
        student_money -= receive * denomination
        received.setdefault(denomination, receive)
    return received


def main():
    with open('2009U1.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()] # Perskaitomi duomenys iš duomenų failo, pašalinant nereikalingus tarpus

    # Sukuriami du tušti kintamieji, kuriuose saugoma mokinių pinigų suma
    gilija_student = 0
    eglija_student = 0

    # Perskaitomi skirtingų šalių nominalai ir sudedami į masyvus
    gilija_denominations = [int(denomination) for denomination in lines[1].split(' ')]
    eglija_denominations = [int(denomination) for denomination in lines[4].split(' ')]

    # Einama per mokinių turimas nominalų monetas ir nominalus, juos padauginama ir sudedama į kintamuosius, kad gauti pinigų sumas 
    for coins, value in zip(gilija_denominations, lines[2].split(' ')):
        gilija_student += coins * int(value)
    for coins, value in zip(eglija_denominations, lines[5].split(' ')):
        eglija_student += coins * int(value)
    
    # Šaukiama funkcija, kuri duoda žodyną su nominalu ir turimų monetų skaičiumi. Randamos monetų sumos su sum() funkcija
    gilija_received = exchange(gilija_student, eglija_denominations)
    eglija_received = exchange(eglija_student, gilija_denominations)
    gilija_coin_amount = sum(gilija_received.values())
    eglija_coin_amount = sum(eglija_received.values())

    with open('./20019/pagrindine/2009U1rez.txt', 'w') as f:
        # Einama per abiejų šalių mokinių gautas monetas ir jas surašoma į rezultatų failą
        for denomination, amount in gilija_received.items():
            f.write(f'{str(denomination)} {amount}\n')
        f.write(str(gilija_coin_amount) + '\n')
        for denomination, amount in eglija_received.items():
            f.write(f'{str(denomination)} {amount}\n')
        f.write(str(eglija_coin_amount))
        

if __name__ == '__main__':
    main()
    with open('./2009/pagrindine/2009U1.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    gilija_student = 0
    eglija_student = 0
    gilija_denominations = [int(denomination) for denomination in lines[1].split(' ')]
    eglija_denominations = [int(denomination) for denomination in lines[4].split(' ')]

    for coins, value in zip(gilija_denominations, lines[2].split(' ')):
        gilija_student += coins * int(value)
    for coins, value in zip(eglija_denominations, lines[5].split(' ')):
        eglija_student += coins * int(value)
    
    gilija_received = exchange(gilija_student, eglija_denominations)
    eglija_received = exchange(eglija_student, gilija_denominations)
    gilija_coin_amount = sum(gilija_received.values())
    eglija_coin_amount = sum(eglija_received.values())

    with open('2009U1rez.txt', 'w') as f:
        for denomination, amount in gilija_received.items():
            f.write(f'{str(denomination)} {amount}\n')
        f.write(str(gilija_coin_amount) + '\n')
        for denomination, amount in eglija_received.items():
            f.write(f'{str(denomination)} {amount}\n')
        f.write(str(eglija_coin_amount))
        

if __name__ == '__main__':
    main()
