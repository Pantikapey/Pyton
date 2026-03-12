from smartphone import Smartphone

# Создаем список телефонов (Catalog)
Catalog = [
    Smartphone("Nokia", 3120, +7985),
    Smartphone("Nokia", 3133, +8214),
    Smartphone("Nokia", 3154, +6544),
    Smartphone("Nokia", 3166, +1245),
    Smartphone("Nokia", 3220, +2541)
]

# Печатаем каталог
for Smartphone in Catalog:
    print(f"{Smartphone.name}-{Smartphone.model}-{Smartphone.number}")
