import ply.lex as lex

tokens = [ 'INT' ]

t_ignore  = ' \t'

def t_INT(token):
    r'[0-9]+[_0-9]*'
    cleanString = token.value.replace("_", "")
    token.value = int(cleanString)
    return token


def getLexer():
    return lex.lex()