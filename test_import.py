"""
Тестирование импорта пакета mypackage.
"""

print("=" * 50)
print("ТЕСТИРОВАНИЕ ИМПОРТА ПАКЕТА")
print("=" * 50)

# Тест 1: Импорт всего пакета
print("\n1. Импорт пакета:")
import mypackage
print(f"   ✅ Версия: {mypackage.__version__}")
print(f"   ✅ Доступные компоненты: {mypackage.__all__}")

# Тест 2: Импорт классов напрямую
print("\n2. Импорт классов:")
from mypackage import Student, Group, APIClient
print("   ✅ Student, Group, APIClient импортированы")

# Тест 3: Импорт функций валидации
print("\n3. Импорт функций валидации:")
from mypackage import validate_email, validate_age
print("   ✅ validate_email, validate_age импортированы")

# Тест 4: Проверка работы валидации
print("\n4. Проверка валидации:")
test_email = "student@example.com"
valid, msg = validate_email(test_email)
print(f"   Email '{test_email}': {msg}")

test_age = 19
valid, msg = validate_age(test_age)
print(f"   Возраст {test_age}: {msg}")

# Тест 5: Создание объекта Student
print("\n5. Создание студента:")
student = Student("Иван", "Петров", 19, "ivan@example.com")
print(f"   ✅ {student}")

# Тест 6: Добавление оценок
print("\n6. Добавление оценок:")
student.add_grade(5, "Python")
student.add_grade(4, "Математика")
print(f"   ✅ Средний балл: {student.get_average_grade():.2f}")

# Тест 7: Форматирование вывода
print("\n7. Форматирование:")
from mypackage import format_student_info
info = format_student_info(student)
print(info)

print("\n" + "=" * 50)
print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
print("=" * 50)