
class Board:

    def __init__(self):
        self.country_lists = open('country_list.txt')
        self.countries = self.populate_countries()
        self.bordering_countries = self.populate_bordering_countries()
        self.card_values = self.populate_card_values()

    def populate_countries(self):
        for line in self.country_lists:
            if line[:9] == 'countries':
                countries = eval(line[12:])
                return countries

    def populate_bordering_countries(self):
        for line in self.country_lists:
            if line[:19] == 'bordering_countries':
                bordering_countries = eval(line[22:])
                return bordering_countries

    def populate_card_values(self):
        for line in self.country_lists:
            if line[:11] == 'card_values':
                card_values = eval(line[14:])
                return card_values


if __name__ == '__main__':
    board = Board()

