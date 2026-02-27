from lesson_3_address import Address
from lesson_3_mailing import Mailing

to_address = Address("Москва", "Тверская", 1, 10, "125009")
from_address = Address("Курск", "Ленина", 5, 12, "305000")

mailing = Mailing(to_address, from_address, 1500, "123654")
print(mailing)

