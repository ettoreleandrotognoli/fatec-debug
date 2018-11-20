import unittest
from fatec.ettore import debug

class TestDebug(unittest.TestCase):
    
    def test_test(self):
        self.assertTrue(True)

    def test_arg_to_string(self):
        expected = '([1, 2, 3],{})'
        result = debug.args_to_string(args=[1,2,3],kwargs={})
        self.assertEqual(result,expected)
