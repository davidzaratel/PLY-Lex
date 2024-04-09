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
   ('strDouble', 'exclusive')
)

# ------------------- enters the single quote string state -----------------
def t_begin_strSingle(token):
    r'\''
    token.lexer.begin('strSingle')
    token.lexer.str_buf = "'"

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
    token.value = token.lexer.str_buf + token.value
    token.type = "STR"
    return token

def t_strSingle_error(token):
    print("Illegal character", token.value)
    token.lexer.skip(1)

t_strSingle_ignore = ''


# ------------------- enters the double quote string state -----------------
def t_begin_strDouble(token):
    r'\"'
    token.lexer.begin('strDouble')
    token.lexer.str_buf = '"'

# reads the escaping characters
def t_strDouble_escape(token):
    r'(\\\")'
    print("escape")
    token.lexer.str_buf += token.value

# reads the 'normal' characters inside the string
def t_strDouble_content(token):
    r'[^\"]'
    token.lexer.str_buf += token.value

# ends the strDouble state
def t_strDouble_end(token):
    r'\"'
    token.lexer.begin('INITIAL')  # Return to the initial state
    token.value = token.lexer.str_buf + token.value
    token.type = "STR"
    return token

def t_strDouble_error(token):
    print("Illegal character", token.value)
    token.lexer.skip(1)

t_strDouble_ignore = ''


# ------------------- floats -----------------
@TOKEN(float_regex)
def t_FLOAT(token):
    token.value = float(token.value)
    return token


# ------------------- ints -----------------

@TOKEN(int_regex)
def t_INT(token):
    cleanString = token.value.replace("_", "")
    token.value = int(cleanString)
    return token

def t_error(t):
    print(t)

def getLexer():
    return lex.lex()