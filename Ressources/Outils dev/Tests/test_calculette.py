from calculette import *
import pytest

@pytest.mark.parametrize("input, output", [(1,1), (1.5, 2.25), (2,4), (3,9), (4,16)])
@pytest.mark.square
def test_carre(input, output):
    assert carre(input) == output

@pytest.mark.skip
@pytest.mark.square
def test_carre2():
    assert carre(3) == 4

@pytest.mark.other
def test_racine():
    assert racine(9) == 3