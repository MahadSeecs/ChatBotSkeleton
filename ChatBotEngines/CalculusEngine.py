from sympy import *
from re import findall
from chat import definer

processed_user = definer()
user = processed_user[0] # gives the statement
op = processed_user[1] # gives the operation

def find_variable(exp):
    variable_pattern = r'\b[a-zA-Z]\b'
    variables = findall(variable_pattern, exp)
    return variables[0] if variables else None


def find_func(exp):
    #Assuming its the last word in the user input
    tok = exp.split()
    return tok[-1]
    

def result(f,op,sym):
    if op == 'd':
        return diff(f,sym)
    
    elif op == 'i':
        return integrate(f,sym)
    

answer = (result(find_func(user),op,find_variable(user)))
print(answer)


