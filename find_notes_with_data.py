import csv
import datetime

def find_notes_date(date_str, num_lines=5):
    with open('notes.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        found_occurrences = 0

        for i, line in enumerate(lines):
            if date_str in line:
                found_occurrences += 1
                print(f"Найдена дата {date_str} в строке {i}:")
                for j in range(max(0, i - num_lines), i):
                    print(lines[j].strip())
        
        if found_occurrences == 0:
            print("Заданная дата не найдена в файле.")
        else:
            print(f"Найдено всего {found_occurrences} записей с датой {date_str}.")




