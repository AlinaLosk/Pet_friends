class Clients:
    def __init__(self,name, surname, city, balanсe):
        self.name = name
        self.surname = surname
        self.city = city
        self.balanсe = balanсe

    def __str__(self):
        return f'Clients : {self.name}, {self.surname}, {self.city}, Баланс : {self.balanсe} руб.'
