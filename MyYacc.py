import ply.yacc as yacc
from mylexer import tokens


def p_ExpressionStatement(p):#done
    """
    ExpressionStatement : statement EndOfStatement
    | statement EndOfStatement ExpressionStatement
    """
    if(len(p)==3):
        p[0]=(p[1],p[2])
    else:
        p[0]=(p[1],p[2],p[3])
    #p[0]=ast.OpNode(p[1],p[2])

def p_statment (p):
    """
    statement : DataType NameVar
    | Array
    | ArrayList
    | DataStructure
    | Pointer
    """
    if(len(p)==3):
        p[0]=('statment',p[1],p[2])
    else:
        p[0]=('statement',p[1])

def p_NameVar(p):
    'NameVar : Name'
    p[0]=('Name',p[1])

def p_DataType(p):
    """
    DataType : Primitive
    | NonPrimitive
    """
    p[0]=('DataType',p[1])

def p_Primitive(p):
    """
     Primitive  : INT
    | FLOAT
    | DOUBLE
    | BOOL
    | CHAR
    """
    p[0]=('primitive',p[1])

def p_NonPrimitive(p):
    """
    NonPrimitive :  INTEGER
    | Double
    | STRING
    | BOOLEAN
    | Float
    |  Oop
    """
    p[0]=('NonPrimitive',p[1])

def p_Oop(p):
    ' Oop : OopType NameVar'
    p[0]=('Oop',p[1],p[2])

def p_OopType(p):
    """
    OopType : STRUCT
    | CLASS
    """
    p[0]=('Ooptype',p[1])

def p_const(p):
    'const : Number'
    p[0]=('Const',p[1])

def p_Array(p):
    """
    Array : DataType NameVar LSQUARE const RSQUARE
    """
    p[0]=('Array',p[1],p[2],p[3],p[4],p[5])


def p_ArrayList(p):
    """
    ArrayList : ArrayListType LANGLE NonPrimitive RANGLE  NameVar
    """
    p[0]=('ArrayList',p[1],p[2],p[3],p[4],p[5])

def p_ArrayListType(p):
    """
    ArrayListType : ARRAYLIST
    | LIST
    """
    p[0]=('ArrayListType',p[1])



def p_DataStructure(p):
    """
DataStructure : DataStructureType NameVar  LPairBracket const RPairBracket
    """
    p[0]=('DataStructure',p[1],p[2],p[3],p[4],p[5])

def p_DataStructureType(p):
    """
    DataStructureType : HASHMAP
    | DICTIONARY
    """
    p[0]=('DataStructureType',p[1])

def p_Pointer(p):
    """
    Pointer : DataType PointerChars  NameVar
    """
    p[0]=('Pointer',p[1],p[2],p[3])

def p_PointerChars(p):
    """
    PointerChars : PointerChar
    | PointerChar PointerChars
    """
    if(len(p)==2):
        p[0]=('PointerChars',p[1])
    else:
        p[0]=('PointerChars',p[1],p[2])

check=True
def p_error(p):
    if p:
        print ("you have error before",p.value)
        check=False
    if not p:
        print("You missed . in the last statement")
        return

parser = yacc.yacc()
t=yacc.parse("int x.")
"""
@primitive DataType
int x.
float x.
char x.
bool x.
double x.

@NonPrimitive DataType
Integer x.
Float x.
Double x.
Boolean x.
String x.

@OOP NonPrimitive DataType
Struct x x.
Class x x.

@Pointer
char ##x.
Class x ##x.
Integer #x.

@Array
bool x[10].
Boolean x[10].
Struct x x[10].

@ArrayList / list must be with NonPrimitive DataType
ArrayList <Integer> x.
List <Struct x> x.

@HashMap or Dictionary
HashMap x(5).
Dict x(7).

/* Multiline
 Comment */

@One Line Comment
"""

if(not check or t!=None):
    print (t)
    import drawTree
    drawTree.MainFrame()





"""
while True:
    try:
        s = raw_input()   # use input() on Python 3
    except EOFError:
        break
    t=yacc.parse(s)
    if(t!=None):
        print (t)

"""

