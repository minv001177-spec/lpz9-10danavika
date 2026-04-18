"""
Модуль Student - класс для представления студента.
"""

from datetime import datetime
from typing import List, Dict, Optional


class Student:
    """
    Класс, представляющий студента.
    
    Атрибуты:
        first_name (str): Имя
        last_name (str): Фамилия
        age (int): Возраст
        student_id (str): Номер студенческого билета
        grades (list): Список оценок
        email (str): Email студента
        created_at (datetime): Дата создания записи
    """
    
    _id_counter = 1  # Счетчик для генерации ID
    
    def __init__(self, first_name: str, last_name: str, age: int, email: Optional[str] = None):
        """
        Инициализация студента.
        
        Args:
            first_name (str): Имя
            last_name (str): Фамилия
            age (int): Возраст
            email (str, optional): Email студента
        """
        # Валидация входных данных
        if not first_name or not last_name:
            raise ValueError("Имя и фамилия не могут быть пустыми")
        if not isinstance(age, int) or age < 0 or age > 120:
            raise ValueError("Возраст должен быть целым числом от 0 до 120")
        if email and '@' not in email:
            raise ValueError("Некорректный email")
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.student_id = f"STU{Student._id_counter:04d}"
        self.grades = []
        self.created_at = datetime.now()
        
        Student._id_counter += 1
    
    def add_grade(self, grade: int, subject: str = "General") -> bool:
        """
        Добавляет оценку студенту.
        
        Args:
            grade (int): Оценка (2-5)
            subject (str): Предмет
            
        Returns:
            bool: True если оценка добавлена, False если некорректна
        """
        if not 2 <= grade <= 5:
            print(f"❌ Ошибка: оценка {grade} должна быть от 2 до 5")
            return False
        
        self.grades.append({
            'subject': subject,
            'grade': grade,
            'date': datetime.now()
        })
        print(f"✅ Оценка {grade} по {subject} добавлена")
        return True
    
    def add_multiple_grades(self, grades_list: List[Dict]) -> int:
        """
        Добавляет несколько оценок сразу.
        
        Args:
            grades_list (list): Список словарей с оценками, например:
                               [{"grade": 5, "subject": "Python"}, ...]
        
        Returns:
            int: Количество успешно добавленных оценок
        """
        added_count = 0
        for grade_info in grades_list:
            grade = grade_info.get('grade')
            subject = grade_info.get('subject', 'General')
            if self.add_grade(grade, subject):
                added_count += 1
        return added_count
    
    def get_average_grade(self) -> float:
        """Возвращает средний балл студента."""
        if not self.grades:
            return 0.0
        total = sum(g['grade'] for g in self.grades)
        return total / len(self.grades)
    
    def get_full_name(self) -> str:
        """Возвращает полное имя студента."""
        return f"{self.last_name} {self.first_name}"
    
    def to_dict(self) -> Dict:
        """Преобразует объект в словарь для JSON."""
        return {
            'student_id': self.student_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email,
            'grades': self.grades,
            'average_grade': self.get_average_grade(),
            'created_at': self.created_at.isoformat()
        }
    
    def __str__(self) -> str:
        return f"Student: {self.get_full_name()} (ID: {self.student_id}, возраст: {self.age})"
    
    def __repr__(self) -> str:
        return f"Student('{self.first_name}', '{self.last_name}', {self.age})"


# Пример использования модуля (для тестирования)
if __name__ == "__main__":
    # Создаем студента
    student = Student("Иван", "Петров", 19, "ivan@example.com")
    print(student)
    
    # Добавляем несколько оценок сразу
    student.add_multiple_grades([
        {"grade": 5, "subject": "Python"},
        {"grade": 4, "subject": "SQL"},
        {"grade": 5, "subject": "Git"}
    ])
    
    # Выводим информацию
    print(f"Средний балл: {student.get_average_grade():.2f}")
    print(f"Данные в JSON: {student.to_dict()}")
    
    # Демонстрация валидации
    try:
        invalid_student = Student("", "", -5, "invalid-email")
    except ValueError as e:
        print(f"\n❌ Ошибка валидации: {e}")