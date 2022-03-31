class Ticket:
    def __init__(self):
        self.__id = None
        self.__buyer = None
        self.__concert = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def buyer(self):
        return self.__buyer

    @buyer.setter
    def buyer(self, new_buyer):
        self.__buyer = new_buyer

    @property
    def concert(self):
        return self.__concert

    @concert.setter
    def concert(self, new_concert):
        self.__concert = new_concert
