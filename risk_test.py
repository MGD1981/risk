import risk


def print_state(testboard):
    print testboard.countries    

def test_counts(testboard):
    n = 0
    for country in testboard.countries:
        n += len(testboard.countries[country])
    assert n == 42


testboard = risk.Board()
test_counts(testboard)
