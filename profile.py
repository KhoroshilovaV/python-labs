# profile.py — карточка студента

surname = input("Фамилия: ")
name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст (полных лет): "))
subject = input("Любимый предмет: ")
hours = float(input("Часов подготовки в неделю: "))

if not (1 <= age <= 120):
    print("Ошибка: возраст должен быть от 1 до 120.")
    raise SystemExit(1)
if hours < 0:
    print("Ошибка: часы подготовки не могут быть отрицательными.")
    raise SystemExit(1)

age_in_4 = age + 4
hours_4_weeks = hours * 4
hours_per_day = hours * 4 / 7  # среднее в день за семидневную неделю

print()
print("=== Карточка студента ===")
print(f"Полное имя: {name} {surname}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age}")
print(f"Любимый предмет: {subject}")
print(f"Возраст через 4 года: {age_in_4}")
print(f"Подготовка за 4 недели: {hours_4_weeks:.2f} ч")
print(f"Среднее в день: {hours_per_day:.2f} ч")
