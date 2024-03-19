import csv
import datetime
from id import generate_unique_id

def writing_note():
    with open('notes.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        title = input("Введите название заметки: ")
        title_note = 'Заголовок: '  + title
        content = input("Введите текст заметки: ")
        content_note = 'Текст заметки:    ' + content
        unique_id = generate_unique_id()
        unique_id_note = 'Уникальный id заметки: ' + unique_id
        
        confirm = input("Хотите сохранить заметку? (y/n): ")
        if confirm.lower() == "y":
            # Передаем список данных в writerow()
            file.write("\n\n")
            writer.writerow([unique_id_note])
            file.write("\n")
            writer.writerow([title_note])
            writer.writerow([content_note])
            file.write("\n")
            # Преобразуем дату и время в нужный фотакрмат
            now = datetime.datetime.now()
            formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            file.write("Дата создания заметки: %s" % formatted_date_time)
            file.write("\n---------------------------------------")
        
            print("Заметка успешно сохранена.")
        else:
            print("Сохранение заметки отменено.")

   