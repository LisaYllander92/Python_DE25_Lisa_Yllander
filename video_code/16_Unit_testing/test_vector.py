from vector import Vector # import the Vector
from pytest import raises, approx # raises an error
# approx = ish
import math

"""ALl tests should start with 'test' """

def test_valid_init():
    v = Vector(1,2,3)
    # assert = make sure that... /what we expect
    assert v.numbers == (1,2,3)

# test to see if vector is empty
def test_empty_vector_fail():
    with raises (ValueError):
        Vector()

# test negative values in init
def test_negative_valid_init():
   v = Vector(-1, -5, 3)
   assert v.numbers == (-1, -5, 3)

# test string in the init
def test_string_in_init_fails():
    with raises(TypeError):
        Vector("1")

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

# test for len() function 
def test_different_lengths():
    vectors = (Vector(1,2), Vector(1), Vector(1,2,3), Vector(1,2,3,4))
    excepted_lengths = (2, 1, 3, 4)

    for vector, excepted_length in zip(vectors, excepted_lengths):
        assert len(vector) == excepted_length



def test_length():
    v = Vector(1,2)
    assert len(v) == 2

# test abs() function
def test_vector_norm_valid():
    v = Vector(1,4)
    expeted_norm =  math.sqrt(v[0]**2 + v[1]**2) #import math
    assert abs(v) == approx(expeted_norm)


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