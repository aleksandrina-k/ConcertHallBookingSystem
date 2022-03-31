from exceptions.entity_already_exists_exception import EntityAlreadyExistsException
from repositories.repository import Repository


class RepositoryConcertHall(Repository):
    def __init__(self, id_gen):
        super().__init__(id_gen)

    def add(self, entity):
        if self.find_by_name(entity.name) or self.find_by_address(entity.address):
            raise EntityAlreadyExistsException('There is already concert hall with the same rname or address in the system.')
        entity.id = self._id_gen.get_next_id()
        self._entities[entity.id] = entity

    def find_by_name(self, name):
        for hall in self._entities.values():
            if hall.name == name:
                return hall
        return None

    def find_by_address(self, address):
        for hall in self._entities.values():
            if hall.address == address:
                return hall
        return None
