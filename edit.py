import csv

def edit_note(note_id):
    with open('notes.csv', 'r', newline='', encoding='utf-8') as file:
        lines = file.readlines()

    found = False
    for index, line in enumerate(lines):
        if note_id in line:
            found = True
            
            title_index = index + 2
            title = input("Введите новое название заметки: ")
            lines[title_index] = 'Заголовок: ' + title + '\n'
            
            content_index = title_index + 1
            content = input("Введите новый текст заметки: ")
            lines[content_index] = 'Текст заметки:    ' + content + '\n'

            with open('notes.csv', 'w', newline='', encoding='utf-8') as file:
                file.writelines(lines)
            
            print("Заметка успешно отредактирована.")
            break

    if not found:
        print("Заметка с указанным ID не найдена.")

