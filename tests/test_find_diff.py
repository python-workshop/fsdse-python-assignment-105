from unittest import TestCase


class TestFind_diff(TestCase):
    def test_find_diff(self):
        try:
            from build import find_diff
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, find_diff, None)
        self.assertEqual(find_diff('abcd', 'abcde'), 'e')
        self.assertEqual(find_diff('aaabbcdd', 'abdbacade'), 'e')
