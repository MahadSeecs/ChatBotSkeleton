from sympy import *
import re

def find_variable(exp):
    variable_pattern = r"\b[a-zA-Z]\b"
    variables = re.findall(variable_pattern, exp)
    return variables[0] if variables else "x"


def find_func(exp):
    # Assuming its the last word in the user input
    tok = exp.split()
    return tok[-1]


def result(f, op, sym):
    if op == "d":
        return diff(f, sym)

    elif op == "i":
        return integrate(str(f), symbols(sym))
    

def differentiater(exp):
    var = find_variable(exp)
    func = find_func(exp)
    return result(func,'d',var)

def integrater(exp):
    var = find_variable(exp)
    func = find_func(exp)
    return result(func,'i',var)




