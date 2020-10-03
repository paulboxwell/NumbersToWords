import numberstowords    # The code to test

def test_subfunc_units_0():
    assert numberstowords.hundreds("0", 0) == "Zero"

def test_subfunc_units_1():
    assert numberstowords.hundreds("3", 0) == "Three"

def test_subfunc_twenty():
    assert numberstowords.hundreds("20", 0) == "Twenty"


def test_units_0():
    assert numberstowords.numb_to_text(0, 'plain') == "Zero"

def test_units_1():
    assert numberstowords.numb_to_text(1, 'plain') == "One"

def test_units_3():
    assert numberstowords.numb_to_text(3, 'plain') == "Three"

def test_units_9():
    assert numberstowords.numb_to_text(9, 'plain') == "Nine"

def test_tens():
    assert numberstowords.numb_to_text(10, 'plain') == "Ten"

def test_teens():
    assert numberstowords.numb_to_text(14, 'plain') == "Fourteen"


def test_twenty():
    assert numberstowords.numb_to_text(20, 'plain') == "Twenty"

def test_fithty():
    assert numberstowords.numb_to_text(50, 'plain') == "Fithty"
  

def test_hun():
    assert numberstowords.numb_to_text(110, 'plain') == "One Hundred and Ten"

def test_hun_2():
    assert numberstowords.numb_to_text(984, 'plain') == "Nine Hundred and Eighty Four"

def test_neg_1():
    assert numberstowords.numb_to_text(-110, 'plain') == "Negative One Hundred and Ten"

def test_dec_1():
    assert numberstowords.numb_to_text(0.2, 'plain') == "Zero point Two"

def test_dec_2():
    assert numberstowords.numb_to_text(0.0123456789, 'plain') ==  "Zero point Zero One Two Three Four Five Six Seven Eight Nine"


def test_pound():
    assert numberstowords.numb_to_text(1, 'pounds') ==  "One Pound"

def test_pounds():
    assert numberstowords.numb_to_text(2, 'pounds') ==  "Two Pounds"

def test_pounds_and_pence():
    assert numberstowords.numb_to_text(3.20, 'pounds') ==  "Three Pounds Twenty Pence"