from repositories.id_generator_int import IdGeneratorInt
from repositories.id_generator_uuid import IdGeneratorUuid
from repositories.repository_concert import RepositoryConcert
from repositories.repository_concert_hall import RepositoryConcertHall
from repositories.repository_registered_user import RepositoryRegisteredUser
from repositories.repository_ticket import RepositoryTicket


class MainRepository:
    def __init__(self):
        self.registered_users_repo = RepositoryRegisteredUser(IdGeneratorUuid())
        self.concerts_repo = RepositoryConcert(IdGeneratorInt())
        self.concert_hall_repo = RepositoryConcertHall(IdGeneratorInt())
        self.ticket_repo = RepositoryTicket()

    def show_all(self):
        print('\n\n===Registered Users===')
        self.registered_users_repo.show_all()
        print('\n===Concerts===')
        self.concerts_repo.show_all()
        print('\n===Concert Halls===')
        self.concert_hall_repo.show_all()