from math_series import __version__
from math_series.series import *


def test_version():
    assert __version__ == '0.1.0'

""" 
1. Fabonacci test
-----------------
test cases: 
   -1  => "The value must be positive"
   "2" => "The value must be integer"
    0  => 0
    1  => 1
    9  => 34  

"""
def test_fabonacci_0():
    expected = 0
    actual = fibonacci(0)
    assert expected == actual 

def test_fabonacci_1():
    expected = 1
    actual = fibonacci(1)
    assert expected == actual

def test_fabonacci_9():
    expected = 34
    actual = fibonacci(9)
    assert expected == actual

def test_fabonacci_positive():
    expected = "The value must be positive"
    actual = fibonacci(-1)
    assert expected==actual

def test_fabonacci_integer():
    expected = "The value must be integer"
    actual = fibonacci("2")
    assert expected == actual


""" 
2. Lucas test
-----------------
test cases: 
   -1  => "The value must be positive"
   "2" => "The value must be integer"
    0  => 2
    1  => 1
    9  => 76  

"""
def test_lucas_0():
    expected = 2
    actual = lucas(0)
    assert expected == actual 

def test_lucas_1():
    expected = 1
    actual = lucas(1)
    assert expected == actual

def test_lucas_9():
    expected = 76
    actual = lucas(9)
    assert expected == actual

def test_lucas_positive():
    expected = "The value must be positive"
    actual = lucas(-1)
    assert expected==actual

def test_lucas_integer():
    expected = "The value must be integer"
    actual = lucas("2")
    assert expected == actual
""" 
3. Sum_series test
------------------
test cases: 
    -1 => "The value must be positive"
    "2" => "The value must be intager"
     0 => 0
     1 => 1
     5,1,1 => 2
     9,2,1 => 76
     9,0,1=> 34

"""
def sum_series_0():
    expected = 0
    actual = sum_series(0)
    assert expected == actual 

def sum_series_1():
    expected = 1
    actual = sum_series(1)
    assert expected == actual

def sum_series_positive():
    expected = "The value must be positive"
    actual = sum_series(-1)
    assert expected==actual

def sum_series_integer():
    expected = "The value must be integer"
    actual = sum_series("2")
    assert expected == actual

def sum_series_921():
    expected = 76
    actual = sum_series(9,2,1)
    assert expected == actual
def sum_series_901():
    expected = 34
    actual = sum_series(9,0,1)
    assert expected == actual
def sum_series_511():
    expected = 2
    actual = sum_series(5,1,1)
    assert expected == actual