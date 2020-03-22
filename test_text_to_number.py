import numberstowords    # The code to test

def test_units_0():
    assert numberstowords.text_to_numb("Zero", 'plain') == 0

def test_units_1():
    assert numberstowords.text_to_numb("One", 'plain') == 1

def test_units_3():
    assert numberstowords.text_to_numb("Three", 'plain') == 3

def test_units_9():
    assert numberstowords.text_to_numb("Nine", 'plain') == 9

def test_tens():
    assert numberstowords.text_to_numb("Ten", 'plain') == 10

def test_hun():
    assert numberstowords.text_to_numb("One Hundred and Ten", 'plain') == 110

def test_neg_1():
    assert numberstowords.text_to_numb("Negative One Hundred and Ten", 'plain') == -110

def test_dec_1():
    assert numberstowords.text_to_numb("Zero point Two", 'plain') == 0.2

