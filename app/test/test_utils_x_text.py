from utils.x_text import *

def test_capitalize():
    assert capitalize('hello woRLD') == 'Hello world'

def test_slice_from_start():
    assert slice_from_start('hello world', 3) == 'hel'

def test_slice_from_end():
    assert slice_from_end('hello world', 3) == 'lo world'
    assert slice_from_end('hello world', 99) == ''

def test_title():
    assert title('hello world') == 'Hello World'