import pytest
import tree

copac = tree.Tree()

def test_find():
    copac.add(8)
    assert copac.find(8).data == 8

def test_find_not():
    copac.add(8)
    assert copac.find(8).data == 6
