#!/usr/bin/env python
__author__ = 'marcsantiago'
try:
    from future_builtins import *
except ImportError:
    pass

try:
    input = raw_input
    range = xrange
except NameError:
    pass