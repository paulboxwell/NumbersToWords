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

def test_hun_2():
    assert numberstowords.text_to_numb("Nine Hundred and Eighty four", 'plain') == 984

def test_neg_1():
    assert numberstowords.text_to_numb("Negative One Hundred and Ten", 'plain') == -110

def test_dec_1():
    assert numberstowords.text_to_numb("Zero point Two", 'plain') == 0.2

def test_dec_2():
    assert numberstowords.text_to_numb("Zero point Naught One Two Three Four Five Six Seven Eight Nine", 'plain') == 0.0123456789

def test_dec_3():
    assert numberstowords.text_to_numb("Negative One Hundred and Ten point Naught One Two Three Four Five Six Seven Eight Nine", 'plain') == -110.0123456789

def test_dec_4():
    assert numberstowords.text_to_numb("Zero point Seven One Zero Six One One Seven Nine Eight Two One Three One One Three", 'plain') == 0.710611798213113

def test_dec_5():
    assert numberstowords.text_to_numb("Zero point Seven Nine Eight Two One Three One One Three Two", 'plain') == 0.7982131132

