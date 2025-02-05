import unittest
import sys
from io import StringIO
from unittest.mock import patch
from main import split_message


class TestSplitMessage(unittest.TestCase):

    def test_edge_case_empty_html(self):
        html = ""
        max_len = 100

        result = list(split_message(html, max_len))
        self.assertEqual(result, [])

    def test_max_length_restriction(self):
        html = "<html><body><p>Test message</p></body></html>"
        max_len = 50

        result = list(split_message(html, max_len))
        self.assertTrue(all(len(fragment) <= max_len for fragment in result))


if __name__ == '__main__':
    unittest.main()

