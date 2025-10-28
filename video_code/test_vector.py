from vector import Vector
from pytest import raises

def test_valid_init():
    v = Vector(1,2,3)
    # assert = make sure that... 
    assert v.numbers == (1,2,3)


def test_invalid_init():
    with raises(TypeError):
        Vector(1,2,"3")

    with raises(ValueError):
        Vector()

def test_addition():
    v1 = Vector(1,2,3)
    v2 = Vector(4,5,6)
    result = v1 + v2
    assert result.numbers == (5,7,9)

    with raises(TypeError):
        v1 + "not a vector"

    with raises(TypeError):
        v1 +5

def test_subtraction():
    v1 = Vector(1,2,3)
    v2 = Vector(4,5,6)
    result = v1 - v2
    assert result.numbers == (-3,-3,-3)

    with raises(TypeError):
        v1 - "not a vector"

    with raises(TypeError):
        v1 - 5

def test_length():
    v = Vector(1,2)
    assert len(v) == 2

def test_abs():
    v = Vector(4,3)
    assert abs(v )== 5
    
def test_validate_vectors():
    v1 = Vector(1,2)
    v2 = Vector(3,4)
    assert v1.validate_vectors(v2) is True

    v3 = Vector(1,2,3)
    with raises(TypeError):
        v1.validate_vectors(v3)

    with raises(TypeError):
        v1.validate_vectors("not a vector")

def test_getitem():
    v = Vector(12,3,4)
    assert v[0] == 12
    assert v[1] == 3
    assert v[-1] == 4

def test_plot():
    v1 = Vector(1,2)
    v2 = Vector(2,2)
    v3 = Vector(3,4)

    v1.plot(v2,v3)

    assert True