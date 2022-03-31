from exceptions.entity_already_exists_exception import EntityAlreadyExistsException
from repositories.repository import Repository


class RepositoryConcert(Repository):
    def __init__(self, id_gen):
        super().__init__(id_gen)

    def add(self, entity):
        if self.find_by_date(entity.date) and self.find_by_place(entity.place):
            raise EntityAlreadyExistsException('There is already user with the same username or email in the system.')
        entity.id = self._id_gen.get_next_id()
        self._entities[entity.id] = entity

    def find_by_date(self, concert_date):
        for concert in self._entities.values():
            if concert.date == concert_date:
                return concert
        return None

    def find_by_place(self, place):
        for concert in self._entities.values():
            if concert.place is place:
                return concert
        return None
