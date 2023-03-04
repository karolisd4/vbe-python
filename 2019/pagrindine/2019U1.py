def get_used(own_one: int, own_three: int, own_five: int, total_oil: int) -> tuple[tuple[int, int], int]:
    '''Funckija, kuri atranda, kiek buvo panaudotų ir nepanaudotų aliejaus indų.'''

    # Sukuriami tušti kintamieji, kuriuose bus saugomas panaudotų indų kiekis.
    used_five = 0
    used_three = 0
    used_one = 0

    # Trijuose for cikluose einama per turimų atitinkamų indų kiekį.
    for _ in range(own_five):
        # Jeigu iš viso turimo aliejaus kiekio atėmus atitinkamą litrų kiekį viso turimo aliejaus kiekis didesnis ar lygus nuliui,
        # iš aliejaus atimamas litrų kiekis ir prie panaudoto indo kintamojo pridedamas vienetas.
        if total_oil - 5 >= 0:
            total_oil -= 5
            used_five += 1
    # Analogiškai kartojama su trijų ir vieno litrio tūrio indų kiekiais.
    for _ in range(own_three):
        if total_oil - 3 >= 0:
            total_oil -= 3
            used_three += 1
    for _ in range(own_one):
        if total_oil - 1 >= 0:
            total_oil -= 1
            used_one += 1
    # Nepanaudotus indus randama iš turimų indų atėmus panaudotus indus.
    not_used_one = own_one - used_one
    not_used_three = own_three - used_three
    not_used_five = own_five - used_five

    # Grąžinami 3 tuple masyvai ir likęs aliejaus kintamasis. Masyvuose bus po 2 elementus. [0] - panaudotas, [1] - nepanaudotas aliejus.
    return (used_one, not_used_one), (used_three, not_used_three), (used_five, not_used_five), total_oil


def get_bonus(oil_left: int) -> tuple[int, int, int]:
    '''Funkcija atranda, kiek papildomai reiktų nusipirkti atitinkamų indų. Naudojamas // operatorius, kad dalinti be liekanos. 
    Iš likusio aliejaus vis atimama didžiausias kiekis tam tikro tūrio indų, iki tol, kol nelieka aliejaus.'''
    five = oil_left // 5
    oil_left -= five * 5
    three = oil_left // 3
    oil_left -= three * 3
    one = oil_left
    return one, three, five


def main():
    with open('./2019/pagrindine/U1.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]    # Perskaitomi duomenys, sudedami į masyvą, pašalintant nereikalingus tarpus.
    
    # Iš duomenų masyvo randama visa reikiama informacija, visi kintamieji paverčiami į int tipą, naudojant list comprehension.
    own_one, own_three, own_five, total_oil = [int(num) for num in lines[0].split(' ')]
    prod_cost, cost_one, cost_three, cost_five = [int(num) for num in lines[1].split(' ')]

    # Šaukiant funkcijas suskaičiuojama visa reikalinga informacija.
    one, three, five, oil_left = get_used(own_one, own_three, own_five, total_oil)
    bonus_one, bonus_three, bonus_five = get_bonus(oil_left)
    
    # Randamas pelnas; visi panaudotų indų kiekiai sudauginami su jų kainomis ir viskas susumuojama. Iš sumos atimamos gamybos išlaidos.
    profit = ((one[0] + bonus_one) * cost_one + (three[0] + bonus_three) * cost_three + (five[0] + bonus_five) * cost_five) - prod_cost
    
    # Į rezultatų failą surašoma visi rezultatai pagal sąlygą.
    with open('./2019/pagrindine/U1rez.txt', 'w') as f:
        f.write(f'{one[0]} {three[0]} {five[0]} {oil_left}\n')
        f.write(f'{one[1]} {three[1]} {five[1]}\n')
        f.write(f'{bonus_one} {bonus_three} {bonus_five}\n')
        f.write(f'{profit}')


# Šaukiama pagrindinė funckija.
if __name__ == '__main__':
    main()