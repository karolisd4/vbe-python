class Marsaeigis():
    def __init__(self, pr_x, pr_y, pab_x, pab_y):
        self.pr_x = pr_x
        self.pr_y = pr_y
        self.x = pr_x
        self.y = pr_y
        self.pab_x = pab_x
        self.pab_y = pab_y
        self.komandos = []
        
    def judeti(self, komanda):
        self.komandos.append(str(komanda))
        if komanda == 1:
            self.y += 1
        elif komanda == 2:
            self.x += 1
        elif komanda == 3:
            self.y -= 1
        elif komanda == 4:
            self.x -= 1

    def gauti_rezultata(self):
        if self.pasiektas_tikslas():
            sekos_res = 'pasiektas tikslas'
            res =  f'{sekos_res:<20} {" ".join(self.komandos)} {len(self.komandos)}'
        else:
            sekos_res = 'sekos pabaiga'
            res = f'{sekos_res:<20} {" ".join(self.komandos)} {len(self.komandos)}'

        self._isvalyti()
        return res

    def pasiektas_tikslas(self):
        if self.x == self.pab_x and self.y == self.pab_y:
            return True
        else:
            return False
    
    def _isvalyti(self):
        self.komandos = []
        self.x = self.pr_x
        self.y = self.pr_y

def main():
    with open('2014/U2.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
    pr_x, pr_y = duomenys[0].split(' ')
    pab_x, pab_y = duomenys[1].split(' ')
    rezultatai = []

    marsaeigis = Marsaeigis(int(pr_x), int(pr_y), int(pab_x), int(pab_y))
    for line in duomenys[3:]:
        komandos = line.split(' ')[1:]
        for komanda in komandos:
            marsaeigis.judeti(int(komanda))
            if marsaeigis.pasiektas_tikslas():
                break
        rezultatai.append(marsaeigis.gauti_rezultata())

    with open('./2014/U2rez.txt', 'w') as f:
        for rezultatas in rezultatai:
            f.write(rezultatas + '\n')
    

main()
