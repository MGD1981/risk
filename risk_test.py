import risk


def print_state(testboard):
    print testboard.countries    

def test_counts(testboard):
    n = 0
    for continent in testboard.countries:
        n += len(testboard.countries[continent])
    assert n == 42

def test_borders(testboard):
    for country in testboard.bordering_countries:
        for bordering_country in testboard.bordering_countries[country]:
            assert country in testboard.bordering_countries[bordering_country]


testboard = risk.Board()
test_counts(testboard)
test_borders(testboard)
