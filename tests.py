import unittest
from nose.tools import assert_equal
from nose.tools import assert_true

from rangedict import RangeDict


def test_insert():
    rd = RangeDict()
    rd[(1, 2)] = 1.5
    rd[(3, 5)] = 4

    assert_true(4 in rd)
    assert_equal(rd[4], 4)


def test_delete():
    rd = RangeDict()
    rd[(1, 2)] = 1.5
    rd[(3, 5)] = 4

    del rd[(1, 2)]
    assert_true(1 not in rd)
    assert_equal(rd[4], 4)
