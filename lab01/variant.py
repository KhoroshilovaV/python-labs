# variant.py — расчёт заказа, вариант 14: Магазин для животных
order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

# Позиция 1 — упаковки корма
item1_name = input("Название первой позиции: ")
item1_qty = int(input("Количество первой позиции: "))
item1_price = float(input("Цена первой позиции (руб.): "))

# Позиция 2 — игрушки
item2_name = input("Название второй позиции: ")
item2_qty = int(input("Количество второй позиции: "))
item2_price = float(input("Цена второй позиции (руб.): "))

delivery = float(input("Стоимость доставки (руб.): "))
paid = float(input("Внесённая сумма (руб.): "))

if item1_qty < 0 or item2_qty < 0:
    print("Ошибка: количество не может быть отрицательным.")
    raise SystemExit(1)
if item1_price < 0 or item2_price < 0 or delivery < 0:
    print("Ошибка: цены и доставка не могут быть отрицательными.")
    raise SystemExit(1)

item1_cost = item1_qty * item1_price
item2_cost = item2_qty * item2_price
goods_total = item1_cost + item2_cost
grand_total = goods_total + delivery
total_qty = item1_qty + item2_qty

if paid < grand_total:
    print("Ошибка: внесённой суммы недостаточно.")
    raise SystemExit(1)

change = paid - grand_total

print()
print(f"=== Заказ: {order_name} ===")
print(f"Заказчик: {customer_name}")
print(f"{item1_name} | {item1_qty} | {item1_price:.2f} | {item1_cost:.2f}")
print(f"{item2_name} | {item2_qty} | {item2_price:.2f} | {item2_cost:.2f}")
print(f"Товары без доставки: {goods_total:.2f} руб.")
print(f"Доставка: {delivery:.2f} руб.")
print(f"Итого с доставкой: {grand_total:.2f} руб.")
print(f"Общее количество единиц: {total_qty}")
print(f"Сдача: {change:.2f} руб.")
