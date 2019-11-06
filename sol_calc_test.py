from sol_calc import*
import pytest
import math

def test_find_sqrt():
    assert find_sqrt(100)==10.0
def test_find_ceil():
    assert find_ceil(12.7)==13

if __name__=='__main__':
    pytest.main()