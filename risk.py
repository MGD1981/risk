
class Board:

    def __init__(self):
        self.country_list = open('risk_countries.txt')
        self.continents = self.populate_continents()

    def populate_continents(self):
        continents = {}
        for line in self.country_list:
            if 'CONTINENT' in line:
                i = line.find(' ')
                current_continent = line[i+1:-1]
                continents[current_continent] = []
            else:
                continents[current_continent].append(line[:-1])
        return continents


if __name__ == '__main__':
    board = Board()

