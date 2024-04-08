import ply.lex as lex
from ply.lex import TOKEN

tokens = [ 'INT', 
            'FLOAT',
            'STR'
         ]


t_ignore  = ' \t'
int_regex = r'([0-9]+(\_[0-9]+)*)'
sci_regex = r'(e|E)(\-|\+)?' + int_regex 
float_regex = r'((' + int_regex + r'?\.' + int_regex + r'?' +  sci_regex + r')|(' + int_regex + sci_regex + r')|(' + int_regex + r'?\.' + int_regex + r'?))'
str_regex = r'(\'.*\')'

@TOKEN(str_regex)
def t_STR(token):
    return token

@TOKEN(float_regex)
def t_FLOAT(token):
    token.value = float(token.value)
    return token

@TOKEN(int_regex)
def t_INT(token):
    cleanString = token.value.replace("_", "")
    token.value = int(cleanString)
    return token

def t_error(t):
    print(t)

def getLexer():
    return lex.lex()