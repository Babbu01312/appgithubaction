from src.math_operation import add,sub

def test_add():
    assert add(2,2)==5
    assert add(-1,1)==0

def test_sub():
    assert sub(2,2)==0
    assert sub(5,3)==2
    