from calculator import sum_nums, subtraction_nums, multiply_nums, divide_nums

def test_sums():
    assert sum_nums(3, 5) == 8

def test_subtraction():
    assert subtraction_nums(9, 6) == 3

def test_multiply():
    assert multiply_nums(4, 3) == 12

def test_divide():
    assert divide_nums(10, 2) == 5
    assert divide_nums(10, 0) == "На ноль делить нельзя!"


test_sums()
test_subtraction()
test_multiply()
test_divide()