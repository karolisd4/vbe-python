from datetime import timedelta

def main():
    with open('./2018/pagrindine/U2.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
        slidininku_sk = int(duomenys[0])
        duomenys.pop(0)
    if slidininku_sk < 1 or slidininku_sk > 30:
        return
    
    slidininku_start_duom = {}
    slidininku_finish_duom = {}
    slidininku_rez_duom = {}
    vardai = []
    nepasieke_slidininkai = []

    for line in duomenys[:6]:
        vardas = line[:20].strip()
        if vardas not in vardai:
            vardai.append(vardas)
        valanda, minute, sekunde = line[20:].strip().split(' ')
        slidininku_start_duom[vardas] = (valanda, minute, sekunde)
    for line in duomenys[7:]:
        vardas = line[:20].strip()
        valanda, minute, sekunde = line[20:].strip().split(' ')
        slidininku_finish_duom[vardas] = (valanda, minute, sekunde)
    
    for vardas in sorted(vardai):
        if vardas not in slidininku_finish_duom.keys():
            nepasieke_slidininkai.append(vardas)
        if vardas not in nepasieke_slidininkai:
            s_valanda, s_minute, s_sekunde = slidininku_start_duom[vardas]
            f_valanda, f_minute, f_sekunde = slidininku_finish_duom[vardas]
            praejes_laikas = timedelta(hours=int(f_valanda), minutes=int(f_minute), 
            seconds=int(f_sekunde)) - timedelta(hours=int(s_valanda), minutes=int(s_minute), seconds=int(s_sekunde))
            minute = str(praejes_laikas.seconds // 60)
            sekunde = str(praejes_laikas.seconds - int(minute) * 60)
            slidininku_rez_duom[vardas] = (minute, sekunde)

    with open('./2018/pagrindine/U2rez.txt', 'w') as f:
        for laikas, vardas in sorted((v, k) for k, v in slidininku_rez_duom.items()):
            f.write(f'{vardas:<20} {laikas[0]} {laikas[1]}\n')
        

main()