class Yarul0:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        Yarul0.__instance = None

    def __init__(self, x = 11, y = 22):
        print('call __init__ to: ' + str(self))
        self.x = x
        self.y = y

yar = Yarul0(12, 23)
yar2 = Yarul0(10, 20)

print(yar.__dict__)
print(yar2.__dict__)





