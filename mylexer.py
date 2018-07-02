import  ply.lex as lex

reserved = {
    'List':'LIST',
    'ArrayList': 'ARRAYLIST',
    'Class': 'CLASS',
    'Struct': 'STRUCT',
    'HashMap':'HASHMAP',
    'Dict':'DICTIONARY',
    'bool': 'BOOL',
    'float': 'FLOAT',
    'int': 'INT',
    'double':'DOUBLE',
    'char':'CHAR',
    'String':'STRING',
    'Boolean':'BOOLEAN',
    'Integer':'INTEGER',
    'Float':'Float',
    'Double':'Double'
}

tokens=[
       'PointerChar',
       'Number','EndOfStatement',
      'LPairBracket','RPairBracket',
    'LSQUARE','RSQUARE',
    'LANGLE','RANGLE',
    'Name','OneLineComment',
    'MuliLineComment'
]

tokens += reserved.values()
t_ignore=' ' #to ingnore space
t_PointerChar=r'\#'
t_EndOfStatement='.'
t_LPairBracket = r'\('
t_RPairBracket = r'\)'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_LANGLE = r'\<'
t_RANGLE = r'\>'


def t_Name(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

def t_Number(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_MuliLineComment(t):
    r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'
#t_COMMENT.__doc__ = r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'

def t_OneLineComment(t):
    r'\@.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
t_newline.__doc__ = r'\n+'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#optimize=1, lextab="footab"
lexer = lex.lex()
"""
if __name__ == '__main__':
    lexer.input("Struct y x .int #x./*hhjjkkl999999999999*/@55555555555556")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)
"""