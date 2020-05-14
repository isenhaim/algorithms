# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

print("Введите две буквы:")

letter_1 = input("1. ")
letter_2 = input("2. ")

location_letter_1 = ord(letter_1) - 96
location_letter_2 = ord(letter_2) - 96

beetwen_letter = location_letter_2 - location_letter_1

print(
    f"""Позиция первой буквы {location_letter_1}
Позиция второй буквы {location_letter_2}
Между ними {abs(beetwen_letter)} букв(ы)
"""
)
