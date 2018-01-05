from typing import List


def add(a: List[int], b: List[int]) -> List[int]:
    """Adds two lists of digits"""
    # TODO: Rewrite me so I don't rely on converting to ints
    a_num = int(''.join(str(x) for x in a))
    b_num = int(''.join(str(x) for x in b))
    return to_digit_list(a_num + b_num)


def to_digit_list(x: int) -> List[int]:
    """Converts a number into a list of digits"""
    return [int(d) for d in str(x)]


def from_digit_list(x: List[int]) -> int:
    """Converts a list of digits into a number"""
    return int(''.join(str(d) for d in x))


if __name__ == '__main__':
    a = to_digit_list(int(input("First number: ")))
    b = to_digit_list(int(input("Second number: ")))
    c_list = add(a, b)
    c = int(''.join(str(x) for x in c_list))
    print(c)
