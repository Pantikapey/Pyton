import math

def square(items):
    return math.ceil(items * items )

float_items = float(input("Сторона квадрата: "))
print(f"Площадь квадрата: {square(float_items)}")