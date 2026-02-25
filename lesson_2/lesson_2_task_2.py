def is_year_lest(number):
    return "Да" if number % 4 == 0 else "Нет"
num = int(input("Год высокостный: "))
result = is_year_lest(num)
print(f"{result}")