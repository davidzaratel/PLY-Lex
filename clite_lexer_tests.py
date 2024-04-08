import unittest
import ply.lex as lex
import clite

class TestIntegers(unittest.TestCase):
    def setUp(self):
        self.lexer = clite.getLexer()

    def test_basic_integers(self):
        self.lexer.input('1934')
        token = self.lexer.token()
        self.assertEqual(token.type, 'INT')
        self.assertEqual(token.value, 1934)

    def test_underscored_integers(self):
        self.lexer.input('1_9_3_4')
        token = self.lexer.token()
        self.assertEqual(token.type, 'INT')
        self.assertEqual(token.value, 1934)

    def test_wrong_integers(self):
        self.lexer.input('1__934')
        token = self.lexer.token()
        self.assertEqual(token.type, 'INT')
        self.assertNotEqual(token.value, 1934)
        self.assertRaises(lex.LexError, self.lexer.token)

class TestFloats(unittest.TestCase):
    def setUp(self):
        self.lexer = clite.getLexer()

    def test_basic_decimal_floats(self):
        self.lexer.input('0. 72.40 072.30 2.71828 .25')
        for value in [0.0, 72.4, 72.3, 2.71828, .25]:
            token = self.lexer.token()
            self.assertAlmostEqual(token.value, value)
            self.assertEqual(token.type, 'FLOAT')

    def test_basic_decimal_floats_sci_notation(self):
        self.lexer.input('1.e+0 6.67428e-11 1E6 .12345E+5')
        for value in [1.0, 6.67428e-11, 1e6, 0.12345E+5]:
            token = self.lexer.token()
            self.assertAlmostEqual(token.value, value)
            self.assertEqual(token.type, 'FLOAT')
    
    # def test_decimal_underscored_floats(self):
    #     self.lexer.input('1_5. 0.15e+0_2')
    #     for value in [15.0, 15.0]:
    #         token = self.lexer.token()
    #         self.assertAlmostEqual(token.value, value)
    #         self.assertEqual(token.type, 'FLOAT')

    # def test_wrong_floats_1(self):
    #     self.lexer.input('1_.5')
    #     self.lexer.token()  # consumes "1"
    #     self.assertRaises(lex.LexError, self.lexer.token)

    # def test_wrong_floats_2(self):
    #     self.lexer.input('1._5')
    #     self.lexer.token()  # consumes "1."
    #     self.assertRaises(lex.LexError, self.lexer.token)

    # def test_wrong_floats_3(self):
    #     self.lexer.input('1.5_e1')
    #     self.lexer.token()  # consumes "1.5"
    #     self.assertRaises(lex.LexError, self.lexer.token)

    # def test_wrong_floats_4(self):
    #     self.lexer.input('1.5e_1')
    #     self.lexer.token()
    #     self.assertRaises(lex.LexError, self.lexer.token)

if __name__ == '__main__':
    # unittest.main(TestIntegers())
    unittest.main(TestFloats())