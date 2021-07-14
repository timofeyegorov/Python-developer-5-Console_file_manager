from myfunctions import separator, long_separator, simple_separator, pow_many, my_filter
from directories import create_dir
from file_save import save_dir_content

def test_separator():
    assert separator('*', 6) == '******'
    assert separator('**', 2) == '****'

def test_long_separator():
    assert long_separator(5) == '*****'

def test_simple_separator():
    assert simple_separator() == '**********'

def test_pow_many():
    assert pow_many(1, 1, 2, 3) == 6
    assert pow_many(2, 1, 2, 3) == 36

def test_my_filter():
    y = my_filter([0, 3, 500], lambda x: x < 10)
    assert y == [i for i in [0, 3, 500] if i < 10]
    assert y[0] == 0
