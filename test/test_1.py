import pytest
import src.func1 as f1


def test_func1():
    val = f1.get_name("con", "ga")
    assert val == "Con Ga"
