"""
Модуль validators - функции для валидации данных.
"""

import re


def validate_email(email):
    """
    Проверяет корректность email адреса.
    
    Args:
        email (str): Email для проверки
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not email:
        return False, "Email не может быть пустым"
    
    # Простая проверка формата email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True, "Email корректен"
    else:
        return False, "Некорректный формат email"


def validate_age(age):
    """
    Проверяет корректность возраста.
    
    Args:
        age: Возраст для проверки
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not isinstance(age, (int, float)):
        return False, "Возраст должен быть числом"
    
    if age < 16:
        return False, "Студент должен быть старше 16 лет"
    
    if age > 100:
        return False, "Некорректный возраст"
    
    return True, "Возраст корректен"


def validate_grade(grade):
    """
    Проверяет корректность оценки.
    
    Args:
        grade: Оценка для проверки
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not isinstance(grade, (int, float)):
        return False, "Оценка должна быть числом"
    
    if grade < 2 or grade > 5:
        return False, "Оценка должна быть от 2 до 5"
    
    return True, "Оценка корректна"


def validate_name(name):
    """
    Проверяет корректность имени/фамилии.
    
    Args:
        name (str): Имя для проверки
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not name or not isinstance(name, str):
        return False, "Имя не может быть пустым"
    
    if len(name) < 2:
        return False, "Имя должно содержать минимум 2 символа"
    
    if not name.replace('-', '').replace(' ', '').isalpha():
        return False, "Имя должно содержать только буквы"
    
    return True, "Имя корректно"

def validate_student_name(first_name, last_name):
    """
    Проверяет корректность имени и фамилии студента.
    
    Args:
        first_name (str): Имя студента
        last_name (str): Фамилия студента
        
    Returns:
        tuple: (is_valid, error_message)
    """
    # Проверка имени
    if not first_name or not isinstance(first_name, str):
        return False, "Имя не может быть пустым"
    
    if not last_name or not isinstance(last_name, str):
        return False, "Фамилия не может быть пустой"
    
    # Проверка, что имя и фамилия не пустые строки (после удаления пробелов)
    first_name_stripped = first_name.strip()
    last_name_stripped = last_name.strip()
    
    if not first_name_stripped:
        return False, "Имя не может быть пустым"
    
    if not last_name_stripped:
        return False, "Фамилия не может быть пустой"
    
    # Проверка, что начинаются с заглавной буквы
    if not first_name_stripped[0].isupper():
        return False, "Имя должно начинаться с заглавной буквы"
    
    if not last_name_stripped[0].isupper():
        return False, "Фамилия должна начинаться с заглавной буквы"
    
    # Проверка, что содержат только буквы (можно с дефисом)
    pattern = r'^[A-Za-zА-Яа-я]+(-[A-Za-zА-Яа-я]+)?$'
    
    if not re.match(pattern, first_name_stripped):
        return False, "Имя должно содержать только буквы (можно с дефисом)"
    
    if not re.match(pattern, last_name_stripped):
        return False, "Фамилия должна содержать только буквы (можно с дефисом)"
    
    return True, "Имя и фамилия корректны"

# Тестирование валидаторов
if __name__ == "__main__":
    print("=== Тестирование validate_email ===")
    test_emails = ["test@example.com", "invalid-email", "user@domain", "a@b.c"]
    for email in test_emails:
        valid, msg = validate_email(email)
        print(f"{email}: {msg}")
    
    print("\n=== Тестирование validate_student_name ===")
    test_names = [
        ("Иван", "Петров"),
        ("", "Петров"),
        ("иван", "Петров"),
        ("Иван", "петров"),
        ("Анна-Мария", "Иванова"),
        ("Иван123", "Петров"),
        ("Джон", "Доу-Джонсон")
    ]
    
    for first, last in test_names:
        valid, msg = validate_student_name(first, last)
        print(f"Имя: '{first}', Фамилия: '{last}' -> {'✅' if valid else '❌'} {msg}")