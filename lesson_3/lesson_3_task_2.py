from smartphone import Smartphone

# Создаем список телефонов (Catalog)
Catalog = [
    Smartphone("Nokia", 3120, number +7985),
    Smartphone("Nokia", 3133, number +8214),
    Smartphone("Nokia", 3154, number +6544),
    Smartphone("Nokia", 3166, number +1245),
    Smartphone("Nokia", 3220, number +2541)
]

# Печатаем каталог
for Smartphone in Catalog:
    print(f"{Smartphone.name}-{Smartphone.model}-{Smartphone.number}")
