#rangedict [![Build Status](https://travis-ci.org/WKPlus/rangedict.svg?branch=master)](https://travis-ci.org/WKPlus/rangedict) [![Coverage Status](https://coveralls.io/repos/WKPlus/rangedict/badge.svg)](https://coveralls.io/r/WKPlus/rangedict)

rangedict is a dict whose key can be a range.

##Usage
----

```
    >>> from rangedict import RangeDict
    >>> rd = RangeDict()
    >>> rd[(1, 2)] = 1
    >>> rd[(3, 3)] = 3
    >>> rd[(5, 7)] = 5
    >>> print rd[6]
    5
    >>> 3 in rd
    True
    >>> del rd[(3, 3)]
    >>> 3 in rd
    False
```

Implemented based on red black tree provides an O(logn) complexity for
inserting, deleting and finding.

##Installation
Installation with `pip` is recommended:
```
pip install rangedict
```
