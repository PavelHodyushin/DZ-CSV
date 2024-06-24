import csv

def write_holiday_cities(first_letter):
    list_cities = []

    with open('travel-notes.csv', 'r', newline='') as cvs_file:
        reader = csv.reader(cvs_file)
        for row in reader:
            list_cities.append(row)

    sorting = []
    for n in list_cities:
        name, visited_cities, wanted_cities = n[0], n[1].split(';'), n[2].split(';')
        if name.startswith(first_letter):
            sorting.append((name, visited_cities, wanted_cities))
            print(name, visited_cities, wanted_cities)


    all_visited_cities = set()
    all_wanted_cities = set()
    for _, visited_cities, wanted_cities in sorting:
        all_visited_cities.update(visited_cities)
        print(f'Посетили: {visited_cities}')
        all_wanted_cities.update(wanted_cities)
        print(f'Хотят посетить: {wanted_cities}')
    never_visited_cities = all_wanted_cities - all_visited_cities
    print(f'Никогда не были в: {never_visited_cities}')
    first_city_to_visit = sorted(never_visited_cities)[0] if never_visited_cities else 'None'
    print(f'Следующим городом будет: {first_city_to_visit}')
    with open('holiday.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for name, visited_cities, wanted_cities in sorting:
            writer.writerow([name, visited_cities, wanted_cities, list(never_visited_cities), first_city_to_visit])

write_holiday_cities('R')