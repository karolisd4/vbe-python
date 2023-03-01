import datetime

class Participant():
    def __init__(self, name: str, group: int, time: datetime.time):
        self.name = name
        self.group = group
        self.time = time


def write_result(result):
    with open('./2009/pagrindine/U2rez.txt', 'w') as f:
        for participant in result:
            f.write(f'{participant.name} {participant.time.minute} {participant.time.second}\n')


def main():
    with open('./2009/pagrindine/U2.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    group_count = int(lines[0])
    lines.pop(0)
    assert 2 <= group_count <= 50

    participants = []
    groups = []
    results = []

    for _ in range(group_count):
        groups.append([])

    group = 0
    for line in lines:
        if len(line) <= 2:
            group += 1
            continue
        name = line[0:20].strip()
        minutes, seconds = line[21:].split(' ')
        time = datetime.time(minute=int(minutes), second=int(seconds))
        participants.append(Participant(name, group, time))

    for participant in participants:
        for i in range(1, group_count+1):
            if participant.group == i:
                groups[i-1].append(participant)

    for i in range(1, group_count+1):
        amount = len(groups[i-1]) // 2
        for j, person in enumerate(groups[i-1]):
            if j == amount - 1:
                continue
            chosen = min(groups[i-1], key=lambda participant: participant.time)
            results.append(chosen)
            groups[i-1].remove(chosen)

    results = sorted(results, key=lambda participant: participant.time)
    write_result(results)
        

if __name__ == '__main__':
    main()
