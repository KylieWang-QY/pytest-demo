import pytest

@pytest.mark.g1
def test_func1():
    pass

@pytest.mark.g2
def test_func2():
    pass

@pytest.mark.g1
def test_func3():
    pass

@pytest.mark.g2
def test_func4():
    pass

@pytest.mark.g1
def test_func5():
    pass