class Model:
    _id: str
    data: str

    def __init__(self, id: str, data: str):
        self._id = id
        self.data = data

    @property
    def id(self):
        return self._id
