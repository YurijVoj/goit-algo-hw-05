import re

from typing import Callable

# Створюємо генератор для пошуку чисел з плаваючою крапкою у тексті
def generator_numbers(text: str):
    # Використовуємо регулярний вираз для пошуку чисел з плаваючою крапкою
    pattern_simple = r"\s+\d+\.\d*\s+"
    # Знаходимо всі відповідності в тексті на основі шаблону та зберігаємо їх у список
    numbers_simple = re.findall(pattern_simple, text)
    # Перетворюємо знайдені рядки у числа з плаваючою крапкою
    float_numbers_simple = [float(num) for num in numbers_simple]
    # Використовуємо yield для повернення чисел по одному
    for numbers in float_numbers_simple:
        yield numbers


# Функція для обчислення суми чисел, отриманих з генератора   
def sum_profit(text: str, func: Callable)-> float:
    # Викликаємо генератор для отримання чисел
    gen = func(text)
    # Ініціалізуємо змінну для збереження суми
    total = 0.0
    # Ітеруємося по числах, отриманих з генератора, і додаємо їх до суми
    for item in gen: 
        total += item
    # Повертаємо загальну суму    
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

