def get_eaten_plums_by_each_student(eaten_girl_plums):
    eat_count = [0 for _ in range(20)]  # Sukuriamas tuscias masyvas su nuliais, kuriame bus saugomi suvalgytu slyvu duomenys
    
    for i, eaten_plum in enumerate(eaten_girl_plums):
        remaining_plums = 10 - eaten_plum   # Einama per kiekviena suvalgytu slyvu skaiciu, ir skaiciuojama, kiek slyvu liko dubenelyje
        eat_count[i] += eaten_plum  # Prie suvalgytu slyvu masyvo pridedama tiek slyvu, kiek buvo suvalgyta
        for j in range(remaining_plums):
            eat_count[i+j+1] += 1  # Kiti mokiniai suvalgo po viena slyva tiek kartu, kiek yra like slyvu

    return [str(count) for count in eat_count]  # Grazinamas masyvas, pavertus kiekviena elementa i string tipa


def main():
    # Perskaitomi duomenys i masyva
    # Tuo paciu metu atidaromi ir duomenu, ir rezultatu failai, perskaityti duomenys is karto apdorojami funkcijos ir irasomi i rezultatu faila
    with open('./2015/pagrindine/U1.txt', 'r') as fr, \
        open('./2015/pagrindine/U1rez.txt', 'w') as fw:
        eaten_girl_plums = [int(num) for num in fr.readline().split(' ')]  # Kiekvienas skaitmuo paverciamas i integer tipa
        fw.write(' '.join(get_eaten_plums_by_each_student(eaten_girl_plums)))   # Masyvas paverciamas i string, atskirta tarpais ir irasomas


if __name__ == '__main__':
    main()