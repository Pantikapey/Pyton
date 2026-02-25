class Smartphone:
    def __init__(self, name, model, number):
        self.name = name
        self.model = model
        self.number = number

    def get_name(self):
        return self.name

    def get_model(self):
        return self.model

    def get_number(self):
        return self.number

    def get_smartphone_info(self):
        return f"Марка: {self.name}, модель: {self.model}, номер {self.number}"
