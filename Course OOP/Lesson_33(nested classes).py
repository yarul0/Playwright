class Men:
    title = 'values of TITLE field'
    photo = 'values of PHOTO field'
    ordering = 'values of ORDERING field'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self._meta = self.Meta(user + ':' + psw)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access

m = Men('admin', '1234')

# print(Men.ordering)
# print(Men.Meta.ordering)

# print(m.ordering)
# print(m.Meta.ordering)

print(m.__dict__)
print(m._meta.__dict__)