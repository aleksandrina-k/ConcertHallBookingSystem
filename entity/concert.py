from datetime import date
from entity.concert_hall import ConcertHall
from repositories.id_generator_int import IdGeneratorInt


class Concert:
    def __init__(self, singer, concert_date, ticket_number, place: ConcertHall):
        self.__id = None
        self.__singer = singer
        self.__date = date.fromisoformat(concert_date)
        self.__ticket_number = ticket_number
        self.__place = place
        self.__tickets = []

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def singer(self):
        return self.__singer

    @singer.setter
    def singer(self, new_singer):
        self.__singer = new_singer

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, new_date):
        self.__date = date.fromisoformat(new_date)

    @property
    def ticket_number(self):
        return self.__ticket_number

    @ticket_number.setter
    def ticket_number(self, new_ticket_number):
        self.__ticket_number = new_ticket_number

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, new_place):
        self.__place = new_place

    def __str__(self):
        return f'{self.__class__.__name__:15.15s}|{str(self.id):3.3s}|{self.singer:15.15s}|{str(self.date):15.15s}|{str(self.ticket_number):6.6s}|{self.place.name:15.15s}'
