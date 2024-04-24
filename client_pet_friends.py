class Clients:
    def __init__(self,name, surname, city, balanсe):
        self.name = name
        self.surname = surname
        self.city = city
        self.balanсe = balanсe

    def __str__(self):
        return f'Clients : {self.name}, {self.surname}, {self.city}, Баланс : {self.balanсe} руб.'
        
 # метод, который будет возвращать информацию только об имени, фамилии и городе клиента.
    
    def get_client(self):
        return f'{self.name} {self.surname},г. {self.city}'
