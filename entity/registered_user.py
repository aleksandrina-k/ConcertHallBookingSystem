from entity.user import User
from entity.ticket import Ticket


class RegisteredUser(User):
    def __init__(self, username, password, email, age):
        super().__init__(username, password, email, age)
        self.bought_tickets = []

    def buy_ticket(self, ticket):
        pass

    def __str__(self):
        return f'{self.__class__.__name__:15.15s}|{str(self.id):15.15s}|{self.username:15.15s}|{self.password:15.15s}|{self.email:15.15s}|{self.age:3d}|{self.bought_tickets}'
