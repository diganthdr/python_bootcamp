import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_int_int(self):
        calc.calc(7,8)
        #self.assertEqual( calc.calc(7, 3), 10 )#integer test

    def test_int_word(self):
        self.assertEqual(calc.calc("5", "Four" ), "Invalid inputs. Only integers supported" ) #int, word test

    def some_func(self):
        pass

if __name__ == '__main__':
    unittest.main()
