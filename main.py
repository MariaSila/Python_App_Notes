from manager import NoteManager
from datetime import datetime

def main():
    note_manager = NoteManager()

    while True:
        print()
        print("Выберите действие:")
        print("1. Создать заметку")
        print("2. Показать все заметки")
        print("3. Найти заметку по id")
        print("4. Найти заметку по дате")
        print("5. Изменить заметку")
        print("6. Удалить заметку")
        print("0. Выйти")

        choice = input("Введите номер действия: ")
        print()

        match choice:
            case '1':
                name = input("Имя заметки: ")
                content = input("Текст заметки: ")
                note_manager.create_note(name, content)
            case '2':
                note_manager.read_notes()
            case '3':
                id = input("Введите id заметки для поиска: ")
                note_manager.read_note_by_id(id)
            case '4':
                start_data = input("Период с (гггг-мм-дд): ")
                end_data = input("Период до (гггг-мм-дд): ")
                note_manager.read_notes_by_data(start_data, end_data)
            case '5':
                id = input("Введите id заметки для изменения: ")
                note_to_update = next((note for note in note_manager.notes_arr if note.id == id), None)
                if note_to_update:
                    new_name = input("Новый заголовок заметки: ")
                    new_content = input("Новый текст заметки: ")
                    note_manager.update_note(id, new_name, new_content)
                else:
                    print(f"Ошибка: заметка с id {id} не найдена")
            case '6':
                note_manager.delete_note(id)
            case '0':
                print("Завершение работы")
                break
            case _:
                print("Введены не корректные данные")

if __name__ == "__main__":
    main()