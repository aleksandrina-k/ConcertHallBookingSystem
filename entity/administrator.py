from entity.concert_creator import ConcertCreator


class Administrator(ConcertCreator):
    def __init__(self, username, password, email, age):
        super().__init__(username, password, email, age)
