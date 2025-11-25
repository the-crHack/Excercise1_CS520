def spec1_bell_number(n, res):
    """Negative input returns 0"""
    if n < 0:
        assert res == 0

def spec2_bell_number(n, res):
    """B(0) = 1"""
    if n == 0:
        assert res == 1

def spec3_bell_number(n, res):
    """B(1) = 1"""
    if n == 1:
        assert res == 1

def spec4_bell_number(n, res):
    """B(2) = 2"""
    if n == 2:
        assert res == 2

def spec5_bell_number(n, res):
    """B(3) = 5"""
    if n == 3:
        assert res == 5

def spec6_bell_number(n, res):
    """B(4) = 15"""
    if n == 4:
        assert res == 15

def spec7_bell_number(n, res):
    """Result is positive for non-negative n"""
    if n >= 0:
        assert res > 0

def spec8_bell_number(n, res):
    """Result is an integer"""
    assert isinstance(res, int)
