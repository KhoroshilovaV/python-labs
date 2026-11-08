# swap.py — обмен аудиторий через третью переменную

first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")

print(f"Исходно: first_room = {first_room}, second_room = {second_room}")

temp = first_room
first_room = second_room
second_room = temp

print(f"После обмена: first_room = {first_room}, second_room = {second_room}")
