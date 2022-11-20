def test_equals():
    assert 1 == 1

def test_greater_than():
    assert 2 > 1
    
def test_less_than():
    assert 1 < 2

def test_not_equal_to():
    assert 1 != 2

def test_greater_than_or_equal_to():
    assert 2 >= 1
    
def test_less_than_or_equal_to():
    assert 1 <= 2
    
def test_tuple_equals_tuple():
    assert (1,2) == (1,2)
    
def test_element_exist_in_list():
    assert 1 in [1,2]
    
def test_string_equals_string():
    assert "abc" == "abc"