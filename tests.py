import unittest
from nose.tools import assert_equal
from nose.tools import assert_true

from rangedict import RangeDict
from rangedict import Color, node_color


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


def black_height(root):
    if not root:
        return 0

    lbh = black_height(root.left)
    rbh = black_height(root.right)
    if lbh != rbh:
        #not a valid red black tree
        return -1
    if root.color == Color.BLACK:
        return lbh + 1
    else:
        return lbh


def check_color(root):
    if not root:
        return True

    if node_color(root) == Color.RED and \
       (
           node_color(root.left) == Color.RED or
           node_color(root.right) == Color.RED
       ):
        return False

    return check_color(root.left) and check_color(root.right)


def is_red_black_tree(root):
    if not root:
        return True
    if root.color == Color.RED:
        return False

    #if black_height(root) < 0:
    #    return False

    if not check_color(root):
        return False
    return True


def test_insert_red_black_tree():
    rd = RangeDict()
    for i in xrange(1, 2000, 2):
        rd[(i, i + 1)] = i

    assert_true(is_red_black_tree(rd._root))


def test_delete_red_black_tree():
    rd = RangeDict()
    for i in xrange(1, 2000, 2):
        rd[(i, i + 1)] = i

    for i in xrange(1, 2000, 2):
        del rd[(i, i + 1)]
        assert_true(is_red_black_tree(rd._root))
    assert_equal(rd._root, None)

