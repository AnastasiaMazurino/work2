# клас Student
class Student:
    def __init__(self, last_name, first_name, birth_date):
        """Ініціалізація прізвища, імені та дати народження"""
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date

    def get_info(self):
        """Метод для виведення інформації про студента"""
        return f"Студент: {self.last_name} {self.first_name}, Дата народження: {self.birth_date}"


# Клас Study, який наслідує Student
class Study(Student):
    def __init__(self, last_name, first_name, birth_date):
        """Ініціалізація класу Study"""
        super().__init__(last_name, first_name, birth_date)
        self.__marks = {}  # Приватне поле для зберігання оцінок

    def add_mark(self, subject, mark):
        """Публічний метод для додавання нової оцінки"""
        if subject not in self.__marks:
            self.__marks[subject] = []
        self.__marks[subject].append(mark)

    def get_marks(self):
        """Публічний метод для отримання словника з предметами та оцінками"""
        return self.__marks

    def __average_subject(self, subject):
        """Приватний метод для розрахунку середнього балу з конкретного предмета"""
        if subject in self.__marks and self.__marks[subject]:
            return sum(self.__marks[subject]) / len(self.__marks[subject])
        return 0

    def get_average_subject(self, subject):
        """Публічний метод для отримання середнього балу з конкретного предмета"""
        return self.__average_subject(subject)

    def __average_semester(self):
        """Приватний метод для розрахунку загального середнього балу за семестр"""
        total_marks = [mark for marks in self.__marks.values() for mark in marks]
        if total_marks:
            return sum(total_marks) / len(total_marks)
        return 0

    def get_average_semester(self):
        """Публічний метод для отримання загального середнього балу за семестр"""
        return self.__average_semester()


# Використання класів
if __name__ == "__main__":
    student = Study("Мазуренко", "Анастасія", "18.12.2006")

    # Додавання оцінок
    student.add_mark("Математика", 90)
    student.add_mark("Математика", 85)
    student.add_mark("Історія", 75)
    student.add_mark("Історія", 80)

    # Виведення інформації про студента
    print(student.get_info())

    # Виведення оцінок
    print("Оцінки:", student.get_marks())

    # Середній бал по предмету
    print("Середній бал з Математики:", student.get_average_subject("Математика"))
    print("Середній бал з Історії:", student.get_average_subject("Історія"))

    # Загальний середній бал за семестр
    print("Загальний середній бал за семестр:", student.get_average_semester())

