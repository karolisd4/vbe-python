class Rectangle():
    def __init__(self, x, y, dx, dy, color, canvas):
        # Inicijuojamas staciakampio objektas su duotais kintamaisiais
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.canvas = canvas
    
    def draw(self):
        # Einama per duotas koordinates. Pradedama nuo pradzios kairiojo tasko, ir einama tiek, koks duotas ilgis ir plotis
        for color_y in range(self.x, self.dx + self.x):
            for color_x in range(self.y, self.dy+ self.y):
                self.canvas.row.append(color_x)  # I eiluciu ir stulpeliu masyvus sudedamos koordinates atitinkamos x;y, kur yra uzpiesti langeliai
                self.canvas.column.append(color_y)
                self.canvas.screen[(color_x, color_y)] = self.color  # Visur, kur einama, spalva pakeiciama i duota spalva


class Canvas():
    def __init__(self):
        # Inicijuojamas objektas su tusciu ekranu bei eiluciu ir stulpeliu masyvais
        self.row = []
        self.column = []
        self._create_screen()
        
    def get_lenght_width(self):
        # Pasalinami duplikatai is eiluciu ir stulpeliu masyvu su set(), randamas ilgis ir skaiciai paverciami i string tipa
        lenght = str(len(set(self.row)))
        width = str(len(set(self.column)))

        return lenght, width
    
    def _create_screen(self):
        '''Sukuriamas naujas tuscias 100x100 ekranas (zodynas), kurio kiekvienas koordinates taskas bus balta spalva ((255,255,255))
        Zodyno key bus koordinates (x;y), o value - spalva [R,G,B]'''
        self.screen = {}
        for screen_x in range(100): # Kiekviena koordinate tures po kiekviena skaiciu. Pvz.: (0;50), (1;50), (50;1) ir t.t.
            for screen_y in range(100):
                self.screen.setdefault((screen_x, screen_y), [255, 255, 255])


def assertion(x, y, width, lenght):
    '''Tikrinama ar kiekvienas duotas skaicius atitinka salygos ribojimus'''
    assert 0<=x<=99
    assert 0<=y<=99
    assert 1<=width<=20
    assert 1<=lenght<=20
    assert x+lenght<=100
    assert y+width<=100


def main():
    with open('./2017/pagrindine/U2.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]  # Perskaitomos linijos, pasalinamos nereikalingos linijos is duomenu, jeigu tokiu yra ir viskas sudedama i masyva
        squares = int(lines[0])  # Perskaitomas staciakampiu skaicius
        lines.pop(0)  # Pasalinamas staciakampiu skaicius is masyvo

    assert 1<=squares<=100  # Tikrinama, ar tinkamas staciakampiu skaicius pagal salyga
    canvas = Canvas()  # Sukuriamas ekrano objektas, ant kurio bus dedami staciakampiai

    for line in lines:
        # Einama per kiekviena linija duomenu masyve, kuri dar karta paverciama i masyva, kurios visi elementai padaromi integer tipo
        line = [int(num) for num in line.split(' ')]

        # Gaunama visa reikiama informacija is duomenu
        x, y = line[:2]
        dx, dy = line[2:4]
        rgb_color = line[4:]
        
        assertion(x, y, dx, dy)  # Tikrinama, ar tinkamas duotu skaiciu kiekis pagal salyga
        rect = Rectangle(x, y, dx, dy, rgb_color, canvas)  # Sukuriamas staciakampio objektas, jam duodamas ekrano objektas bei pradzios koordinates, ilgis, plotis ir spalva
        rect.draw()  # Staciakampis uzpiesiamas ant ekrano
    
    lenght, width = canvas.get_lenght_width()  # Gaunamas baigto paveikslo ilgis bei plotis, saukiant ekrano objekto funckija
    
    results = []  # Sukuriamas tuscias masyvas rezultatams saugoti
    
    with open('./2017/pagrindine/U2rez.txt', 'w') as f:
        f.write(f'{lenght} {width}\n')

        # Einama per kiekviena eilute bei stulpeli, sudedant spalva i rezultatu masyva, pasalinant nereikalingus skliaustus ir kablelius
        # Set() pasalina duplikatus is masyvo
        for x in set(canvas.row):
            for y in set(canvas.column):
                results.append(str(canvas.screen[x, y]).replace('[', '').replace(']', '').replace(',', ''))
        
        f.write('\n'.join(results))  # Rezultatai surasomi, sudedant naujas eilutes


if __name__ == '__main__':
    main()
