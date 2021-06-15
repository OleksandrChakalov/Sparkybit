from main import is_perfect_square as ps
from mock import patch
import unittest
import tempfile


class FibonacciTest(unittest.TestCase):
    def test_is_perfectSquare(self):
        self.assertEqual(ps(4), True)
        self.assertEqual(ps(1), True)
        self.assertEqual(ps(3), False)
        self.assertEqual(ps(7), False)

    def test_is_fibonacci(self):
        self.assertEqual(ps((5 * 4 * 4 + 4) or (5 * 4 * 4 - 4)), False)
        self.assertEqual(ps((5 * 1 * 1 + 4) or (5 * 1 * 1 - 4)), True)
        self.assertEqual(ps((5 * 7 * 7 + 4) or (5 * 7 * 7 - 4)), False)

def myfunc():
    with tempfile.NamedTemporaryFile() as mytmp:
        return mytmp.name

class TestMock(unittest.TestCase):
    @patch('tempfile.NamedTemporaryFile')
    def test_cm(self, mock_tmp):
        mytmpname = 'abcde'
        mock_tmp.return_value.__enter__.return_value.name = mytmpname
        self.assertEqual(myfunc(), mytmpname)

if __name__ == '__main__':
    unittest.main()
