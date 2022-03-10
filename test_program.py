import unittest
from program import *

def test_same():
        ret = freq("apple")
        assert ret ==  {"a": 1, "p": 2, "l": 1, "e": 1}

def test_multiple():
    ret = freq("aaabbccc")
    assert ret == {"a" : 3, "b" : 2, "c": 3}     


def testcase():
        ret =  panagram("the quick brown fox jumps over a lazy dog")
        assert ret == True

def testcase1():
    ret = panagram("the quick brown fox jumped over a lazy dog")
    assert ret == False

def test_average_positive():
        ret = Average([10,20, 30])
        assert ret == 20

def test_average_negetive():
        ret = Average([-10, -20, -30])
        assert ret == -20
        
def test_average_none():
        ret = Average([])
        assert ret == None 