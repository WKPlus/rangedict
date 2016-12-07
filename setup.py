try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '0.1.6'

LONG_DESCRIPTION = '''
rangedict is a dict whose key is a range.

Usage
-----

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

Implemented based on red black tree provides an O(logn) complexity for
inserting, deleting and finding.
'''

setup(
    name='rangedict',
    description='range dict is a dict whose key is a range',
    long_description=LONG_DESCRIPTION,
    author='WKPlus',
    url='https://github.com/WKPlus/rangedict.git',
    license='MIT',
    author_email='qifa.zhao@gmail.com',
    version=VERSION,
    py_modules=['rangedict'],
    install_requires=[],
    test_requires=['nose'],
    zip_safe=False,
)
