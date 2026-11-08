# debug.py — исправленные фрагменты

# Фрагмент А
first_str = "2"
second_str = "3"
first = int(first_str)
second = int(second_str)
print(f"А: типы до — {type(first_str).__name__}, {type(second_str).__name__}; "
      f"после — {type(first).__name__}, {type(second).__name__}")
print(f"А: сумма = {first + second}")  # 5

# Фрагмент Б
age_str = input("Возраст: ")
age = int(age_str)
print(f"Б: тип до — {type(age_str).__name__}, после — {type(age).__name__}")
print(f"Б: возраст через год = {age + 1}")  # 18

# Фрагмент В
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print(f"В: среднее = {average}")  # 7.0
