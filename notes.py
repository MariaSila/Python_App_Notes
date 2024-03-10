from datetime import datetime

class Note:
    def __init__(self, id, data, name, content):
        self.id = id
        self.data = data
        self.name = name
        self.content = content
        
    def __str__(self):
        return f"id: {self.id} \nДата создания: {self.data} \nЗаголовок: {self.name} \nТекст заметки: {self.content}"