# variant.py — расчёт заказа с учетом скидки (Вариант 14)

order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

# Позиция 1
item1_name = input("Название первой позиции: ")
item1_qty = int(input("Количество первой позиции: "))
item1_price = float(input("Цена первой позиции (руб.): "))

# Позиция 2
item2_name = input("Название второй позиции: ")
item2_qty = int(input("Количество второй позиции: "))
item2_price = float(input("Цена второй позиции (руб.): "))

delivery = float(input("Стоимость доставки (руб.): "))
discount_percent = float(input("Скидка в процентах (от 0 до 100): "))
paid = float(input("Внесённая сумма (руб.): "))

# Проверки на отрицательные значения
if item1_qty < 0 or item2_qty < 0:
    print("Ошибка: количество не может быть отрицательным.")
    raise SystemExit(1)
if item1_price < 0 or item2_price < 0 or delivery < 0:
    print("Ошибка: цены и доставка не могут быть отрицательными.")
    raise SystemExit(1)
if not (0 <= discount_percent <= 100):
    print("Ошибка: скидка должна быть от 0 до 100 процентов.")
    raise SystemExit(1)

# Расчеты
item1_cost = item1_qty * item1_price
item2_cost = item2_qty * item2_price
goods_total = item1_cost + item2_cost

# Скидка и итоговая сумма
discount_rub = goods_total * (discount_percent / 100)
discounted_goods = goods_total - discount_rub
grand_total = discounted_goods + delivery
total_qty = item1_qty + item2_qty

# Проверка оплаты
if paid < grand_total:
    print(f"Ошибка: внесённой суммы недостаточно. Нужно минимум {grand_total:.2f} руб.")
    raise SystemExit(1)

change = paid - grand_total

print()
print(f"=== Заказ: {order_name} ===")
print(f"Заказчик: {customer_name}")
print(f"{item1_name} | {item1_qty} | {item1_price:.2f} | {item1_cost:.2f}")
print(f"{item2_name} | {item2_qty} | {item2_price:.2f} | {item2_cost:.2f}")
print(f"Товары без доставки: {goods_total:.2f} руб.")
print(f"Скидка ({discount_percent:.1f}%): -{discount_rub:.2f} руб.")
print(f"Товары со скидкой: {discounted_goods:.2f} руб.")
print(f"Доставка: {delivery:.2f} руб.")
print(f"Итого с доставкой: {grand_total:.2f} руб.")
print(f"Общее количество единиц: {total_qty}")
print(f"Сдача: {change:.2f} руб.")
