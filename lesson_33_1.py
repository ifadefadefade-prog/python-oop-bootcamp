class Women:
    title = 'Объект класса для поля title'
    photo = 'Объект класса для поля photo'
    ordering = 'Объект класса для поля ordering'

    def __init__(self, user, psw):
        self.user = user
        self.psw = psw
        self.meta = self.Meta(self.user + '@' + self.psw)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access
            self._f = Women.title


w = Women('root', '12345')
#print(w.ordering)
#print(w.Meta.ordering)
print(w.__dict__)
print(w.meta.__dict__)
