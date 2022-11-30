def main():
    with open('./2020/pagrindine/U2.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
        zveju_sk = int(duomenys[0])
        duomenys.pop(0)

    rezultatai = {}
    vertinamos_zuvys = {}
    zuvu_svoriai = {}
    duombazes = []
    
    if zveju_sk < 1 or zveju_sk > 30:
        return
    for i in range(zveju_sk):
        duombazes.append(ieskoti(duomenys))
    duomenys.pop(0)
    for line in duomenys:
        zuvis = line[:20].strip()
        taskai = int(line[20:].strip())
        vertinamos_zuvys[zuvis] = taskai
    for i in range(zveju_sk):
        taskai = 0
        duom = duombazes[i]
        vardas = list(duom.keys())[0]
        zuvys = duom.values()
        for zuvis in zuvys:
            for zuvis2 in zuvis:
                zuvies_pav = zuvis2[0]
                mase = int(zuvis2[1])
                if mase > 200:
                    taskai += 30
                    taskai += vertinamos_zuvys[zuvies_pav]
                    rezultatai[vardas] = taskai
                else:
                    taskai += 10
                    taskai += vertinamos_zuvys[zuvies_pav]
                    rezultatai[vardas] = taskai
    for i in duombazes:
        for values in i.values():
            for zuvyte in values:
                if zuvyte[0] not in zuvu_svoriai.keys(): 
                    zuvu_svoriai[zuvyte[0]] = int(zuvyte[1])
                else:
                    zuvu_svoriai[zuvyte[0]] += int(zuvyte[1])
    for v in vertinamos_zuvys:
        if v not in zuvu_svoriai:
            zuvu_svoriai[v] = 0

    with open('./2020/pagrindine/U2rez.txt', 'w') as f:
        f.write('Dalyviai\n')
        for v in rezultatai:
            f.write(f'{v} {rezultatai[v]}\n')
        f.write('Laimikis\n')
        for v in zuvu_svoriai:
            f.write(f'{v} {zuvu_svoriai[v]}\n')

        
def ieskoti(duomenys):
    zuvu_duom = {}
    zuvu_info = []
    vardas = duomenys[0][:20].strip()
    sugautos_zuvys = int(duomenys[0][20:].strip())
    duomenys.pop(0)
    zuvys = duomenys[0:sugautos_zuvys]
    for zuvis in zuvys:
        duomenys.pop(0)
        zuvies_pav = zuvis[:20].strip()
        zuvies_svoris = zuvis[20:].strip()
        zuvu_info.append((zuvies_pav, zuvies_svoris))
    zuvu_duom[vardas] = zuvu_info
    return zuvu_duom


main()