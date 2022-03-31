class IdGeneratorInt:
    def __init__(self):
        self._id = 0

    def get_next_id(self):
        self._id += 1
        return self._id
