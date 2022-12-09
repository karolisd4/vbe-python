def skaityti_duomenis():
    '''Perskaitoma kiekviena linija, is jos pasalinami nereikalingi tarpai'''

    with open('./2008/pagrindine/U2.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def ilgiausias_marsrutas(marsrutai) -> tuple[dict, str]:
    '''Randamas ilgiausias marsrutas, jei tokie keli - maziausias numeris'''

    marsrutu_kiekiai = {}
    ilgiausi_marsrutai = []
    stoteles_istrinimui = []

    # Einama per kiekviena marsruto numeri ir skaiciuojama, kiek kartu jis buvo paminetas, viskas dedama i atskira dictionary
    for marsrutu_numeriai in marsrutai.values():
        for marsruto_numeris in marsrutu_numeriai:

            # Dictionary key yra tam tikras marsruto numeris, value yra kiek kartu jis buvo paminetas
            marsrutu_kiekiai.setdefault(marsruto_numeris, 0)
            marsrutu_kiekiai[marsruto_numeris] += 1

    # Atrandamas didziausias paminejimu skaicius
    ilgiausias_kiekis = max(marsrutu_kiekiai.values())
    
    # Visi marsrutai, kurie turi didziausia paminejimu skaiciu sudedami i atskira masyva
    for marsrutas, ilgis in marsrutu_kiekiai.items():
        if ilgis == ilgiausias_kiekis:
            ilgiausi_marsrutai.append(marsrutas)

    # Ziurima, kuriose stotelese nebuvo paminetas maziausias ilgiausio marsruto skaicius, tos stoteles dedamos i atskira masyva
    for stotele, marsruto_numeriai in marsrutai.items():
        if min(ilgiausi_marsrutai) not in marsruto_numeriai:
            stoteles_istrinimui.append(stotele)

    # Visos stoteles, kurios buvo sudetos i masyva, istrinamos is pagrindinio dictionary
    for stotele in stoteles_istrinimui:
        marsrutai.pop(stotele)
    
    # Grazinamas pakeistas dictionary ir ilgiausio marsruto maziausias skaicius, paverstas i string tipa
    return marsrutai, str(min(ilgiausi_marsrutai))


def main():
    # Perskaicius duomenis gaunamas duotas stoteliu skaicius, jis pasalinamas is duomenu
    duomenys = skaityti_duomenis()
    stoteliu_sk = int(duomenys[0])
    duomenys.pop(0)
    marsrutai = {}
    # Einama per duomenis tiek kartu, kiek nurodyta stoteliu
    for i in range(stoteliu_sk):
        # Pirmi 20 simboliu yra stoteles pavadinimas, toliau - marsrutu numeriai
        pavadinimas = duomenys[i][:20].strip()
        # Naudojama [1:], nes praleidziamas marsrutu kiekis
        marsurtu_numeriai = duomenys[i][20:].split(' ')[1:]
        # I dictionary key idedamas stoteles pavadinimas, i value - masyvas su integer tipo marsrutu numeriais
        marsrutai[pavadinimas] = [int(numeris) for numeris in marsurtu_numeriai]
    
    marsrutai, ilgiausia_stotele = ilgiausias_marsrutas(marsrutai)

    # Surasomi rezultatai, kurios gaunama is funkcijos i rezultatu faila
    with open('./2008/pagrindine/U2rez.txt', 'w') as f:
        f.write(ilgiausia_stotele + '\n')
        for stotele in marsrutai.keys():
            f.write(stotele + '\n')


main()