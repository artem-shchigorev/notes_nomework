from writing import writing_note
from delete import delete_note
from edit import edit_note
from show import display_notes
from find_notes_with_data import find_notes_date
a = True
while a == True:
        print("1: Добавить заметку")
        print("2: Редактировать заметку")
        print("3: Удалить заметку")
        print("4: Просмотр заметок")
        print("5: Выборка по дате")
        print("0: Закрыть программу")
        choice = input("Введите ваш выбор: ")
        if choice == "1":
            writing_note()
        elif choice == "2":
            id_note = input("Введите id заметки, которую хотите редактировать: ")
            edit_note(id_note)
        elif choice == "3":
            id_note = input("Введите id заметки, которую хотите удалить: ")
            delete_note(id_note)
        elif choice == "4":
            choice_show = input("Если хотите вывести на экран все заметки, введите 'all' /n Если хотите посмотреть определенную заметку, введите её id  ")
            display_notes(choice_show)
        elif choice == "5":
            data_notes = input("Введите дату в формате YYYY-MM-DD ")
            find_notes_date(data_notes)
        elif choice == "0":
            a = False
        else:
            print("Некорректное значение.")
