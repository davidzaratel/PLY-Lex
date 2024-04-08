import ply.lex as lex

tokens = [ 'INT' ]

t_ignore  = ' \t'

def t_INT(token):
    r'[0-9]+'
    token.value = int(token.value)
    return token


def getLexer():
    return lex.lex()