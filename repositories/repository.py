from exceptions.entity_not_found_exception import EntityNotFoundException


class Repository:
    def __init__(self, id_gen=None):
        self._id_gen = id_gen
        self._entities = {}

    def find_by_id(self, id):
        found = self._entities.get(id)
        if found is None:
            raise EntityNotFoundException
        return found

    def update(self, entity):
        self.find_by_id(entity.id)
        self._entities[entity.id] = entity
        return entity

    def delete_by_id(self, id):
        to_delete = self.find_by_id(id)
        del self._entities[id]
        return to_delete

    def count(self):
        return len(self._entities)

    def show_all(self):
        for entity in self._entities.values():
            print(entity)
