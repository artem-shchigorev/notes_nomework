import csv

def display_notes(note_id):
    if note_id == 'all':
        with open('notes.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                for item in row:
                    print(item)
            print("\n")  
    else:
        found = False
        with open('notes.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    if note_id in row[0]:
                        found = True
                        for item in row:
                            print(item)
                    print("")  
                    for _ in range(6):
                        next_row = next(reader, None)
                        if next_row:
                            for item in next_row:
                                print(item)
                    break

        if not found:
            print("Заметка с указанным ID не найдена.")

