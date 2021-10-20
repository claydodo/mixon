import unittest
from src import mixon

SAMPLE_PATH = "tests/sample.mixon"
EXPECTED = {
    "id": 123,
    "title": "Ipsum Lorem",
    "desc": "Some fake text",
    "abstract": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n",
    "contents": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
}


class TestLoad(unittest.TestCase):
    def test_load(self):
        with open(SAMPLE_PATH) as f:
            result = mixon.load(f)
            self.assertDictEqual(result, EXPECTED)

    def test_loads(self):
        with open(SAMPLE_PATH) as f:
            s = f.read()
            result = mixon.loads(s)
            self.assertDictEqual(result, EXPECTED)

