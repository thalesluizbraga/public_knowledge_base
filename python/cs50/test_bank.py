#In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value expects a str as input and returns 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. You can assume that the string passed to the value function will not contain any leading spaces. Only main should call print.

#def main():
    #...
#
#
#def value(greeting):
    #...
#
#
#if __name__ == "__main__":
    #main()
#Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
#
#pytest test_bank.py


import pytest
from bank import value

def test_is_hello():
    assert value('hello') == 0
    assert value('Hello') == 0

def test_starts_with_h():
    assert value('hi') == 20
    assert value('hey') == 20
    assert value('Hi') == 20
    assert value('Hey') == 20

def test_does_not_starts_with_h():
    assert value('oi') == 100
    assert value('ola') == 100
    assert value('Oi') == 100
    assert value('Ola') == 100


