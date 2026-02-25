class Address:
    def __init__(self, index, city, street, house, flat):
          self.index = index
          self.city= city
          self.street = street
          self.house = house
          self.flat = flat

          def get_index(self):
              return self.index

          def get_city(self):
              return self.city

          def get_street(self):
              return self.street

          def get_house(self):
              return self.house

          def get_flat(self):
              return self.flat
