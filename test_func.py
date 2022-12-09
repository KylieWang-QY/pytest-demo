def add(x, y):
        return x+y

def test1():
    assert 2 == add(1, 1)

def test2():
    assert 1 != add(1, 1)

import pytest

def func(x):
    if x == 0:
        raise ValueError("value error!")
    else:
        pass

# func(0)
# func(1)

def test3():
    with pytest.raises(ValueError):
        func(0)

def test4():
    assert func(1) == None