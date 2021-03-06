"""
Jesteś informatykiem w firmie Noe's Animals Redistribution Center.
Firma ta zajmuje się międzykontynentalnym przewozem zwierząt.
---------
Celem zadania jest przygotowanie funkcji pozwalającej na przetworzenie
pliku wejściowego zawierającego listę zwierząt do transportu.
Funkcja ma na celu wybranie par (samiec i samica) z każdego gatunku,
tak by łączny ładunek był jak najlżeszy (najmniejsza masa osobnika
rozpatrywana jest względem gatunku i płci).
---------
Na 1 pkt.
Funkcja ma tworzyć plik wyjściowy zwierający listę wybranych zwierząt
w formacie wejścia (takim samym jak w pliku wejściowym).
Wyjście ma być posortowane alfabetycznie względem gatunku,
a następnie względem nazwy zwierzęcia.
---------
Na +1 pkt.
Funkcja ma opcję zmiany formatu wejścia na:
"<id>_<gender>_<mass>"
(paramter "compressed") gdzie:
- "id" jest kodem zwierzęcia (uuid),
- "gender" to jedna litera (F/M)
- "mass" zapisana jest w kilogramach w notacji wykładniczej
z dokładnością do trzech miejsc po przecinku np. osobnik ważący 456 gramów
ma mieć masę zapisaną w postaci "4.560e-01"
---------
Na +1 pkt.
* Ilość pamięci zajmowanej przez program musi być stałą względem
liczby zwierząt.
* Ilość pamięci może rosnąć liniowo z ilością gatunków.
---------
UWAGA: Możliwe jest wykonanie tylko jednej opcji +1 pkt.
Otrzymuje się wtedy 2 pkt.
UWAGA 2: Wszystkie jednoski masy występują w przykładzie.
"""
from pathlib import Path
import csv
from collections import namedtuple


def select_animals(input_path, output_path, compressed=False):

    with open(input_path, 'r') as file_:
        reader = csv.reader(file_, delimiter=',')
        headers = next(reader, None)
        Animal = namedtuple('Animal', ' '.join(headers))

        animals = []
        generations = set()
        for row in reader:
            animal = Animal(*row)
            animals.append(animal)
            generations.add(animal.generations)

        genders = ('male', 'female')

        selected_animals = []
        for generation in generations:
            for gender in genders:
                select_animal = min(animals, key=lambda anim: (anim.generations == generation,
                                                               anim.gender == gender,
                                                               float(anim.mass.split(' ')[0])))
                selected_animals.append(select_animal)

        sorted_animals = sorted(selected_animals, key = lambda anim: (anim.generations,
                                                                      anim.name))

        if not compressed:
            with open(output_path, 'w') as _file:
                writer = csv.writer(_file, delimiter=',', quotechar="*")
                writer.writerow(headers)
                writer.writerows(sorted_animals)

        elif compressed:
            units = {
                'mg': 0.001,
                'g': 1.,
                'kg': 1000.,
                'Mg': 1e6,
            }
            gender = {
                'male': 'M',
                'female': 'F',
            }
            with open(output_path, 'w') as _file:
                _file.write('_'.join(['uuid', headers[4], headers[1]]) + '\n')
                compressed_animals = []
                for animal in sorted_animals:
                    str_mass, prefix = animal.mass.split(' ')
                    mass = float(str_mass) * units[prefix] / 1000.
                    compressed_animal = '_'.join([animal.id,
                                                 gender[animal.gender],
                                                 '%.3e' % mass])
                    compressed_animals.append(compressed_animal)
                # import ipdb; ipdb.set_trace()

                for row in compressed_animals:
                    _file.write(row + '\n')


if __name__ == '__main__':
    input_path = Path('s_animals.txt')
    output_path = Path('s_animals_s.txt')
    select_animals(input_path, output_path)
    with open(output_path) as generated:
        with open('s_animals_se.txt') as expected:
            assert generated.read() == expected.read()

    output_path = Path('s_animals_sc.txt')
    select_animals(input_path, output_path, True)
    with open(output_path) as generated:
        with open('s_animals_sce.txt') as expected:
            assert generated.read() == expected.read()
