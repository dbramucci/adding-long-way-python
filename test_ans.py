from hypothesis import given, settings
from hypothesis.strategies import integers
from main import *

def all_digits(digits: List[int]) -> bool:
    return all(0 <= digit < 10 for digit in digits)

def test_two_digits_to_digit():
    for a, b in ((x, y) for x in range(10) for y in range(10 - x)):
        a_list = to_digit_list(a)
        b_list = to_digit_list(b)
        c_list = add(a_list, b_list)
        c = from_digit_list(c_list)
        assert a + b == c, 'Can add two digits together that add to' \
                           ' less than 10'
        assert all_digits(c_list), 'the answer is a list of digits' \
                                  f' (a={a}, b={b})'

def test_add_two_digits():
    for a, b in ((x, y) for x in range(10) for y in range(10)):
        a_list = to_digit_list(a)
        b_list = to_digit_list(b)
        c_list = add(a_list, b_list)
        c = from_digit_list(c_list)
        assert a + b == c, f'Can add two digits together'
        assert all_digits(c_list), 'the answer is a list of digits' \
                                  f' (a={a}, b={b})'


@settings(max_examples=1000)
@given(integers(min_value=0, max_value=9))
def test_add_10(a: int):
    a_list = to_digit_list(a)
    c_list = add(a_list, [1, 0])
    c = from_digit_list(c_list)
    assert a + 10 == c, "Can add ten to a digit"
    assert all_digits(c_list), 'the answer is a list of digits (a={a}, b={b})'


@settings(max_examples=1000)
@given(integers(min_value=0), integers(min_value=0))
def test_add(a: int, b: int):
    a_list = to_digit_list(a)
    b_list = to_digit_list(b)
    c_list = add(a_list, b_list)
    c = from_digit_list(c_list)
    assert a + b == c, "Can add two non-negative numbers together"
    assert all_digits(c_list), 'the answer is a list of digits (a={a}, b={b})'