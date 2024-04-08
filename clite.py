import ply.lex as lex

tokens = [ 'INT', 
            'FLOAT'
         ]

t_ignore  = ' \t'


def t_FLOAT(token):
    r'[0-9]*(\.[0-9]*)'
    token.value = float(token.value)
    return token

def t_INT(token):
    r'[0-9]+([_][0-9]+)*'
    cleanString = token.value.replace("_", "")
    token.value = int(cleanString)
    return token

def getLexer():
    return lex.lex()