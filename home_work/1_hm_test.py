def test_passing():
    assert ('home', 'work') == ('home', 'work')


def test_failing():
    assert not 'QA' == 'QC'


def test():
    assert not(1, 1, 2, 3, 5) == (2, 3, 5)
