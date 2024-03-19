def delete_note(note_id):
    found = False
    count_to_delete = 7  # Учитываем строку с ID, 5 строк после нее и 1 строку перед ней
    lines_to_delete = 0
    with open('notes.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open('notes.csv', 'w', encoding='utf-8') as file:
        for index, line in enumerate(lines):
            if note_id in line:
                found = True
                lines_to_delete = count_to_delete
            if lines_to_delete > 0:
                lines_to_delete -= 1
            else:
                if index > 0:  # Не записываем первую строку, т.к. она тоже будет удалена
                    file.write(line)

    if found:
        print("Заметка с ID", note_id, "была успешно удалена вместе с 5 строками после нее и 1 строкой перед ней.")
    else:
        print("Заметка с ID", note_id, "не найдена.")