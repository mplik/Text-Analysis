name = input('Podaj nazwę pliku: ')

try:
    with open(name, 'r', encoding='utf-8') as handle:
        counts = dict()
        for line in handle:
            line = line.lower()
            words = line.split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1

        bigcount = None
        bigword = None
        for word, count in list(counts.items()):
            if bigcount is None or count > bigcount:
                bigword = word
                bigcount = count

        if bigword:
            print(bigword, bigcount)
        else:
            print('Plik jest pusty!')

except FileNotFoundError:
    print(f'Plik "{name}" nie istnieje!')
except Exception as e:
    print(f'Błąd: {e}')