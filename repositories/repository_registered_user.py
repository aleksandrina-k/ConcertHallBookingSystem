from exceptions.entity_already_exists_exception import EntityAlreadyExistsException
from repositories.repository import Repository


class RepositoryRegisteredUser(Repository):
    def __init__(self, id_gen):
        super().__init__(id_gen)

    def add(self, entity):
        if self.find_by_username(entity.username) or self.find_by_email(entity.email):
            raise EntityAlreadyExistsException('There is already user with the same username or email in the system.')
        entity.id = self._id_gen.get_id()
        self._entities[entity.id] = entity

    def find_by_username(self, username):
        for user in self._entities.values():
            if user.username == username:
                return user
        return None

    def find_by_email(self, email):
        for user in self._entities.values():
            if user.email == email:
                return user
        return None
