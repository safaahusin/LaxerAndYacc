result="{expr"
i=0

def ConvertTuple(t):
    for i in range (0,len(t)):
        global result
        result+=str(check(t[i]))
    return result+"}"

def check(value):
    if(isinstance(value,tuple)):
        data1=check(value[0])
        data2=check(value[1])
        return data1+data2
    else:
        return ","+str(value)+",#,#"


from nltk.tree import Tree
from nltk.draw.tree import TreeView
t = Tree.fromstring('(S (NP this tree) (VP (V is) (AdjP pretty)))')
print (t)
TreeView(t)._cframe.print_to_file('output.ps')
import os
os.system('convert output.ps output.png')
