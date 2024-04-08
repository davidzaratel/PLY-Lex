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

    # def test_wrong_integers(self):
    #     self.lexer.input('1__934')
    #     token = self.lexer.token()
    #     self.assertEqual(token.type, 'INT')
    #     self.assertNotEqual(token.value, 1934)
    #     self.assertRaises(lex.LexError, self.lexer.token)

if __name__ == '__main__':
    unittest.main(TestIntegers())