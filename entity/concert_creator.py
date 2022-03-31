from entity.concert import Concert
from entity.user import User


class ConcertCreator(User):
    def __init__(self, username, password, email, age):
        super().__init__(username, password, email, age)
        self.created_concerts = []

    # def create_concert(self):
    #     singer = input('Singer: ')
    #     concert_date = input('Date in format YYYY-MM-DD: ')
    #     ticket_number = int(input('Number of tickets: '))
    #     place_name = input('Place (concert hall): ')
    #
    #     new_concert = Concert(singer, concert_date, ticket_number, place)
