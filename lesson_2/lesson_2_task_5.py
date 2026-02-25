def quarter_of_year(month):
    if 1 <= month <= 2:
        return "зима"
    if 3 <= month <= 5:
        return "весна"
    if 6 <= month <= 8:
        return "лето"
    if 9 <= month <= 11:
        return "осень"
    if month == 12:
        return "зима"

    return "Неверный номер месяца"


month = int(input("Введите номер месяца (1-12): "))
print(quarter_of_year(month))
