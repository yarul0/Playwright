class Mono_state:
    __sharred_attr = {
        'id': 1,
        'name': 'Will',
        'data': {}
    }

    def __init__(self):
        self.__dict__ = self.__sharred_attr

