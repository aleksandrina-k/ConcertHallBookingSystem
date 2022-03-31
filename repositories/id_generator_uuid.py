import uuid


class IdGeneratorUuid:
    def get_id(self):
        return uuid.uuid1()
