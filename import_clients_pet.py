from client_pet_friends import Clients

client_1 = Clients ("Иван","Петров","Москва",50)
print(client_1)

# список будет возвращать информацию об имени, фамилии и городе клиента.

client_2 = Clients ("Зиновий","Эдмундов","Нижний Новгород",50)
client_3 = Clients ("Аристарх","Ридов","Тюмень",50)
client_4 = Clients ("Клавдия","Задонская","Липецк",50)
client_5 = Clients ("Тираида","Иванова","Москва",50)

client_list = [client_2,client_3,client_4,client_5]

for client in client_list:
    print(client.get_client())
