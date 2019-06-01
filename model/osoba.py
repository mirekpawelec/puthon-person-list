class Osoba():
    def __init__(self, id, imie, haslo):
        self.id = int(id)
        self.imie = imie
        self.haslo = haslo

    def get_row(self):
        return [self.id, self.imie, self.haslo]

    def get_json(self):
        return {'id': self.id, 'imie': self.imie, 'haslo': self.haslo}

    def __str__(self):
        return 'Osoba[id: {}, imie: {}, haslo: {}]'.format(self.id, self.imie, self.haslo)