class Marsaeigis():
    def __init__(self, pr_x, pr_y, pab_x, pab_y):
        # Inicijuojasi klase su visais kintamaisiais, pradzios x;y koordinates niekad nesikeis, tam sukurtos atskiros x;y koordinates

        self.pr_x = pr_x
        self.pr_y = pr_y
        self.x = pr_x
        self.y = pr_y
        self.pab_x = pab_x
        self.pab_y = pab_y
        self.komandos = []
        
    def judeti(self, komanda: int):

        '''Paima komanda ir pagal salyga atitinkamai judina marsaeigi tam tikra x;y kryptimi.
        I sarasa dedame visas gautas komandas, kad veliau jas butu galima irasyti i rezultatus'''

        self.komandos.append(str(komanda))
        if komanda == 1: self.y += 1
        elif komanda == 2: self.x += 1
        elif komanda == 3: self.y -= 1
        elif komanda == 4: self.x -= 1

    def gauti_rezultata(self):

        '''Patikrina, ar pasiektas keliones tikslas (pabaigos x;y koordinates).
        Jei tikslas pasiektas, i rezultato faila bus irasyta "pasiektas tikslas" ir visos komandos, kuriu prireike ji pasiekti.
        Jei tikslas nepasiektas, i rezultato faila bus irasyta "sekos pabaiga" ir visos komandos, kurios buvo pereitos'''

        if self.pasiektas_tikslas():
            sekos_res = 'pasiektas tikslas'
            res =  f'{sekos_res:<20} {" ".join(self.komandos)} {len(self.komandos)}'
        else:
            sekos_res = 'sekos pabaiga'
            res = f'{sekos_res:<20} {" ".join(self.komandos)} {len(self.komandos)}'

        self._isvalyti()
        return res

    def pasiektas_tikslas(self) -> bool:

        '''Patikrina, ar esamos x;y koordinates yra lygios pabaigos x;y koordinatems ir grazina boolean.'''

        if self.x == self.pab_x and self.y == self.pab_y:
            return True
        else:
            return False
    
    def _isvalyti(self):

        '''Pabaigus viena komandu seka, visas praeitu komandu sarasas yra isvalomas, is naujo nustatomos pradines x;y koordinates'''

        self.komandos.clear()
        self.x = self.pr_x
        self.y = self.pr_y

def main():
    with open('./2014/pagrindinis/U2.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
    # Nuskaitomi duomenys, pasalinami nereikalingi tarpai, paimamos visos reikalingos koordinates
    pr_x, pr_y = duomenys[0].split(' ')
    pab_x, pab_y = duomenys[1].split(' ')
    rezultatai = []

    # Sukuriamas marsaeigio objektas su nuskaitytomis pradzios ir pabaigos koordinatemis
    marsaeigis = Marsaeigis(int(pr_x), int(pr_y), int(pab_x), int(pab_y))
    for line in duomenys[3:]:
        komandos = line.split(' ')[1:]
        # Kiekvienai linijai faile nuskaitomas komandu laukas ir kiekviena komanda duodama marsaeigio objektui
        for komanda in komandos:
            marsaeigis.judeti(int(komanda))
            # Kas kart tikriname, ar buvo pasiektas tikslas
            if marsaeigis.pasiektas_tikslas():
                # Pasiekus tiksla, sustabdomas ciklas ir rezultatai yra issaugomi
                break

        # Kiekvienas rezultatas irasomas i rezultatu masyva, kuris veliau irasomas i rezultatu faila
        rezultatai.append(marsaeigis.gauti_rezultata())

    with open('./2014/pagrindinis/U2rez.txt', 'w') as f:
        for rezultatas in rezultatai:
            f.write(rezultatas + '\n')
    

main()
