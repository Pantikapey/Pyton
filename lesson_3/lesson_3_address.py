class Address:
    def __init__(self, city, street, house, apartment, index):
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
        self.index = index

    def __str__(self):
        return f"{self.index}, {self.city}, {self.street}, {self.house}-{self.apartment}"

    def __repr__(self):
        return (f"Address(city={self.city!r}, street={self.street!r}, house={self.house!r}, "
                f"apartment={self.apartment!r}, index={self.index!r})")
