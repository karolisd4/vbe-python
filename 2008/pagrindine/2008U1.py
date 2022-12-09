def kuriam_marsrute_vezta_daugiausia(marsrutai):
    '''Atrandamas didziausias veztu keleiviu skaicius ir einant per dictionary
    ziurima, ar jis lygus masruto skaiciui. Jei taip, tai tas marsrutas
    nuveze daugiausia keleiviu'''

    daugiausia = max(marsrutai.values())
    for marsruto_nr, keleiviai in marsrutai.items():
        if keleiviai[0] == daugiausia[0]:
            return marsruto_nr


def marsrutu_nr_didejimo_tvarka(marsrutai):
    return sorted(marsrutai)


def skaityti_duomenis():
    with open('./2008/pagrindine/2008U1.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def main():
    # Perskaitomi duomenys bei marsrutu skaicius ir jie is karto pasalinami
    duomenys = skaityti_duomenis()
    marsrutu_sk = int(duomenys[0])
    duomenys.pop(0)

    # Sukuriami tusti masyvai
    marsrutai = {}
    islipe = []
    ilipe = []

    for marsruto_index in range(marsrutu_sk):
        # Is kiekvienos eilutes paimamas marsruto skaicius ir keleiviu skaicius, jie paverciami i int tipa
        marsrutas, keleiviu_sk = duomenys[marsruto_index].split(' ')
        marsrutas = int(marsrutas)
        keleiviu_sk = int(keleiviu_sk)

        # Viskas dedama i dictionary, pirmas elementas masyve bus ilipe keleiviai, antras - islipe
        marsrutai.setdefault(marsrutas, [0, 0])
        if keleiviu_sk < 0:
            marsrutai[marsrutas][1] += keleiviu_sk
        else:
            marsrutai[marsrutas][0] += keleiviu_sk

    max_marsrutas = kuriam_marsrute_vezta_daugiausia(marsrutai)
    rusiuoti_marsrutu_nr = marsrutu_nr_didejimo_tvarka(marsrutai)

    # Einama per dictionary, kuris isrusiuotas pagal marsrutu skaicius ir sudedama visus islipusius ir ilipusius keleiviu skaicius i atskirus masyvus
    for _, v in sorted(marsrutai.items()):
        ilipe.append(v[0])
        islipe.append(v[1])

    # Jeigu kazkurie skaiciavimai nepilnai atlikti, masyvai tusti - bus spausdinama NE
    if not rusiuoti_marsrutu_nr:
        rusiuoti_marsrutu_nr = ['NE']
    if not ilipe:
        ilipe = ['NE']
    if not islipe:
        islipe = ['NE']
    if not max_marsrutas:
        max_marsrutas = 'NE'

    # Surasomi rezultatai, kiekviena elementa masyvuose paverciant i string tipa
    with open('./2008/pagrindine/U1rez.txt', 'w') as f:
        f.write(' '.join([str(marsruto_nr) for marsruto_nr in rusiuoti_marsrutu_nr]) + '\n')
        f.write(' '.join([str(ilipe_kel) for ilipe_kel in ilipe]) + '\n')
        f.write(' '.join([str(islipe_kel) for islipe_kel in islipe]) + '\n')
        f.write(str(max_marsrutas))
    

main()
