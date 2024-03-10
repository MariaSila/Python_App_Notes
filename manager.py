import csv
from datetime import datetime
from notes import Note


class NoteManager:
    def __init__(self):
        self.notes_arr = []
        self.load_from_file()

    def load_from_file(self):
        self.notes_arr = []
        try:
            with open("notes.csv", newline="") as file:
                reader = csv.reader(file, delimiter=";")
                next(reader)
                for row in reader:
                    id, name, content, data = row
                    self.notes_arr.append(Note(id, data, name, content))
        except FileNotFoundError:
            self.create_empty_file()

    def create_empty_file(self):
        with open("notes.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["ID", "Data", "Name", "Content"])

    def create_note(self, name, content):
        id = self.generate_unique_id()
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(id, data, name, content)
        self.notes_arr.append(note)
        self.save_to_file()
        self.load_from_file()

    def generate_unique_id(self):
        if not self.notes_arr:
            return 1
        else:
            id = int(self.notes_arr[-1].id)
            id += 1
            return id

    def read_notes(self):
        delimiter = "-" * 35
        sorted_notes = sorted(self.notes_arr, key=lambda x: x.data, reverse=True)
        for note in sorted_notes:
            print(note)
            print(delimiter)

    def update_note(self, id, new_name=None, new_content=None):
        is_note = False
        for note in self.notes_arr:
            if note.id == id:
                is_note = True
                if new_name is not None:
                    note.name = new_name
                if new_content is not None:
                    note.content = new_content
                note.data = datetime.now().date()
                self.save_to_file()
                print("Заметка изменена.")
                break

        if not is_note:
            print("Ошибка: Заметка с id не найдена.")

    def delete_note(self, id):
        is_note = False
        for note in self.notes_arr:
            if note.id == id:
                self.notes_arr.remove(note)
                is_note = True
                break

        if not is_note:
            print("Ошибка: Заметка с id не найдена.")
            return

        self.save_to_file()
        print("Заметка удалена.")

    def save_to_file(self):
        with open("notes.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["ID", "Name", "Content", "Data"])
            for note in self.notes_arr:
                writer.writerow([note.id, note.name, note.content, note.data])

    def read_notes_by_data(self, start_data, end_data):
        self.load_from_file()
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_data = datetime.strptime(end_data, "%Y-%m-%d")

        delimiter = "-" * 35
        filtered_notes = []

        for note in self.notes_arr:
            note_created_at = datetime.strptime(note.data, "%Y-%m-%d %H:%M:%S")
            if start_data <= note_created_at <= end_data:
                filtered_notes.append(note)

        if filtered_notes:
            for note in filtered_notes:
                print(note)
                print(delimiter)
 
        else:
            print(f"В период с {start_data} по {end_data} заметки не найдены")

    def read_note_by_id(self, id):

        delimiter = "-" * 35
        note = next((note for note in self.notes_arr if note.id == id), None)
        if note:
            print("Заметка найдена:")
            print(note)
            print(delimiter)
        else:
            print("Заметка с указанным ID не найдена.")