class Solution():
    def __init__(self, path):
        '''Inicijuojamas objektas su duota duomenu failu lokacija. Sukuriamas kintamasis, skirtas rusiuoti duomenis pagal teisingai issprestu
        uzdaviniu skaiciu mazejanciai. Sukuriami du zodynai, kuriuose laikoma dalyviu informacija ir masyvas, kuriame laikomi rezultatai.'''

        self.path = path
        self.most_points = 0
        self.participant_points = {}
        self.participants = {}
        self.result = []
        
    def solve(self) -> None:
        with open(f'{self.path}U1.txt', 'r') as f:
            self.data = [line.strip() for line in f.readlines()]    # Perskaitomas duomenu failas, viskas sudedama i masyva.
        self.problem_count = int(self.data[0])

        assert 1 <= self.problem_count <= 12    # Tikrinama, ar uzdaviniu skaicius atitinka salyga.

        # Objekte sukuriami masyvai, kuriuose laikoma informacija apie uzdavinius (duotas laikas ir maksimalus balai).
        self.allocated_time = [int(time) for time in self.data[1].split(' ')]   
        self.maximum_points = [int(point) for point in self.data[2].split(' ')]

        for line in self.data[3:]:
            name = line[:10].strip()
            time_taken = [int(time) for time in line[11:].split(' ')]
            self.participants.setdefault(name, time_taken)  # Gaunamas dalyvio vardas ir sugaistas laikas, viskas sudedama i zodyna
        
        for name in self.participants:
            points, time = self.calculate(self.participants[name])  # Saukiama funkcija, kuri skaiciuoja dalyvio taskus ir sugaista laika
            self.participant_points.setdefault(name, sum(points))   # I kita zodyna idedamas tik dalyvio vardas ir tasku masyvas

            # Rikiuojama duomenis: jeigu tasku skaicius yra didesnis uz anksciau sukurta kintamaji, jis tampa didziausiu ir eina i masyvo prieki (nulinta indeksa).
            if len(points) > self.most_points:  
                self.result.insert(0, (name, len(points), time))
                self.most_points = len(points)
            else:
                self.result.append((name, len(points), time))

        # Pagal zodyna, kuriame yra tik dalyvio vardas ir taskai, atrandamas didziausias ir maziausas tasku skaicius.
        least_points = min(self.participant_points.values())
        most_points = max(self.participant_points.values())

        # Einama per zodyna ir randamas vardas dalyvio, kuris surinko maziausiai tasku.
        for name, points in self.participant_points.items():
            if points == least_points:
                worst_participant = name
        
        # Einama per rezultatu masyva ir pasalinamas tas elementas, kurio pirmas indeksas (vardas) atitinka maziausiai surinkusi dalyvi.
        for res in self.result:
            if res[0] == worst_participant:
                self.result.remove(res)
        
        with open(f'{self.filename}U1rez.txt', 'w') as f:
            f.write(f'{str(most_points)}\n')
            for res in self.result:
                f.write(f'{res[0]:<10} {str(res[1])} {str(res[2])}\n')  # Duomenys surasomi i rezultatu faila, vardui suteikiant 10 simboliu.
    
    def calculate(self, time_taken: list[int]) -> tuple[list[int], int]:
        '''Funkcija skaiciuoja dalyvio gautus taskus ir vis sumuoja sugaista dalyvio laika. Jeigu sugaista 0 laiko, uzduotis praleidziama.
        Jei surinko maziau ar tiek, kiek duota laiko tam uzdaviniui, duodami maksimalus balai. Jei surinko daugiau, nei skirta laiko,
        duodama puse maksimaliu balu sveikais skaiciais su // operatoriumi.'''

        points = [] # Sukuriamas masyvas ir kintamasis rezultatam saugot.
        total_time = 0
        for i, time in enumerate(time_taken): # Naudojama enumerate, kad gauti ta pati elementa is uzdaviniui duoto laiko ir tasku masyvu.
            total_time += time  # Sumuojamas laikas
            if time == 0:
                continue
            elif time <= self.allocated_time[i]:
                points.append(self.maximum_points[i])
            elif time > self.allocated_time[i]:
                points.append(self.maximum_points[i] // 2)  # Gaunamas sveikas maksimaliu tasku puses skaicius su //.

        return points, total_time   # Grazinamas masyvas su gautais taskais ir sugaistas laikas.


if __name__ == '__main__':
    Solution('./2022/pagrindine/').solve()   # Sukuriamas objektas su duomenu lokacija ir saukiama pagrindine solve() funkcija.
