# Problem
Write a function `add` that, given two lists of digits that represent a pair of
numbers returns a list of digits representing the sum of those two numbers.
You should not convert the input into a pair of ints to perform the addition
like the placeholder does. The goal is to implement the same algorithm for
adding as you would do by hand.

Recall that a digit is an integer d such that 0 <= d <= 9. 

# Examples
```python
add([1], [1]) == [2]
add([5], [5]) == [1, 0]
add([5], [7]) == [1, 2]
add([5, 6, 3], [8, 5, 4]) == [1, 4, 1, 7]
```

# Testing

To test your code, open a terminal in the folder you are working in and run
`pytest`.

If you wish to test a specific case, you may run the program with
`python main.py` and you will be prompted to enter the numbers you wish to add.

# Dependencies
You will need pytest and Hypothesis installed to run the testing code.
You can install these with
`pip install pytest hypothesis`

# Typechecking
If you wish to make sure that you are returning the correct type of output,
there are provided type annotations so all you have to do is run
`mypy main.py` to test the type correctness of your program.
If you don't have mypy installed, you may have to use `pip install mypy` first.