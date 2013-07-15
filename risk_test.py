import risk


def print_state(testboard):
    print testboard.continents    

def test_counts(testboard):
    n = 0
    for continent in testboard.continents:
        n += len(testboard.continents[continent])
    assert n == 42


testboard = risk.Board()
test_counts(testboard)
