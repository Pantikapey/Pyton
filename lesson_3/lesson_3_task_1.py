from user import User

# Создаем экземпляр класса User
my_user = User("Anton", "Teslenko")

# Вызываем методы и выводим результат
print(my_user.get_first_name())  # Ожидаемый результат: Anton
print(my_user.get_last_name())  # Ожидаемый результат: Teslenko
print(my_user.get_user_info())  # Ожидаемый результат: Anton Teslenko
