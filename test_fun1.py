from nose.tools import assert_equal
from fun1 import fun1

def test_fun1 ():
    exp = 1
    obs = fun1(0)
    assert_equal(exp,obs)