class ConcertHall:
    def __init__(self, name, address, capacity: int):
        self.__id = None
        self.__name = name
        self.__address = address
        self.__capacity = capacity
        self.reserved_dates = []

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        self.__address = new_address

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, new_capacity):
        self.__capacity = new_capacity

    def __str__(self):
        return f'{self.__class__.__name__:15.15s}|{str(self.id):3.3s}|{self.name:15.15s}|{self.address:15.15s}|{str(self.capacity):6.6s}|{self.reserved_dates}'
