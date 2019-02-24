#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pytest
from scapreporterd.skeleton import fib

__author__ = "David Strauss"
__copyright__ = "David Strauss"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
