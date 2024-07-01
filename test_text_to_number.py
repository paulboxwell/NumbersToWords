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

def test_missing_and():
    assert numberstowords.text_to_numb("One Hundred Ten", 'plain') == 110

def test_random_pad():
    assert numberstowords.text_to_numb("One    Hundred Ten", 'plain') == 110

def test_no_tens():
    assert numberstowords.text_to_numb("One Thousand One Hundred", 'plain') == 1100

def test_no_hundreds():
    assert numberstowords.text_to_numb("One Thousand One", 'plain') == 1001

def test_no_units():
    assert numberstowords.text_to_numb("One Thousand Ten", 'plain') == 1010

def test_millions():
    assert numberstowords.text_to_numb("One Million Three Thousand Ten", 'plain') == 1003010


def test_mix():
    assert numberstowords.text_to_numb("5 hundred", 'plain') == 500

def test_mix_complex():
    assert numberstowords.text_to_numb("5 hundred 13", 'plain') == 513

def test_mix_complex_2():
    assert numberstowords.text_to_numb("5 hundred and 3", 'plain') == 503
