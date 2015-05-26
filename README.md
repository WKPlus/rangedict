#rangedict: a dict maps a range to a value

rangedict is a dict whose key can be a range.

##Usage
----

```
    >>> from rangdict import RangeDict
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
```

Implemented based on red black tree provides an O(logn) complexity for
inserting, deleting and finding.

##Installation
Installation with `pip` is recommended:
```
pip install rangedict
```