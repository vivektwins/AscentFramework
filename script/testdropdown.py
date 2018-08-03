import unittest
import pytest


class TestUM(unittest.TestCase):

    def inc(x):
        return x + 1

    def test_answer(self):
        assert self.inc(3) == 5

