from calculette import *
import pytest 

@pytest.mark.other
def test_compare():
    assert compare(2,3) == "2<=3"