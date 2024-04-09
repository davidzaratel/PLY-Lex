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
single_quote = r'(\'.*\')'
double_quote = r'(\".*\")'
str_regex = r'(' + single_quote +  r'|' + double_quote  + r')'

# declaring str states
states = (
   ('strSingle','exclusive'),
)

# enters the single quote string state
def t_begin_strSingle(token):
    r'\''
    token.lexer.begin('strSingle')
    token.lexer.str_buf = ''

# reads the escaping characters
def t_strSingle_escape(token):
    r'(\\\')'
    token.lexer.str_buf += '\''

# reads the 'normal' characters inside the string
def t_strSingle_content(token):
    r'[^\']'
    token.lexer.str_buf += token.value

# ends the strSingle state
def t_strSingle_end(token):
    r'\''
    token.lexer.begin('INITIAL')  # Return to the initial state
    token.value = token.lexer.str_buf
    token.type = "STR"
    return token

def t_strSingle_error(token):
    print("Illegal character", token.value)
    token.lexer.skip(1)

t_strSingle_ignore = ''

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