from sympy import symbols, parse_expr, evalf
x = symbols("x")
from .functions import Function, PolynomialFunction, TranscendentalFunction # Using relative import since we are going to be calling this from parent 

def process_result(input):  # processes what is currently on the calculator screen 
    if not input.count('(') == input.count(')'): return "Parenthesis's unmatched."
    while " " in input: input = input.replace(" ", "")  
    while "^" in input: input = input.replace("^", "**")
    #TODO parse logs
    if input[:4] != "f(x)":
        try: 
            expr = parse_expr(input)
            return round(expr.evalf(), 3) 
        except SyntaxError: 
            return "SyntaxError, try again"
    """ 
    We can't (easily implement) use process_implicit_mul if transcendental functions are in the calculations so, for now, we will just
    throw a syntax error if user doesn't explicit the mul's (ex: 5sin(x) should be 5*sin(x))
    """
    # if we pass here, we need to evaluate further since we got a calculus request 
    input = input.replace("f(x);", "") 
    if "x" not in input: return "Didn't input function in function mode"
    if Function.find_type(input) == "Polynomial": fun = PolynomialFunction(input) 
    else: fun = TranscendentalFunction(input) 

    if "d/dx|(" in input:  # Order of checks is important since the lower elifs's are inside the higher checks but not the other way around 
        pass
    elif "∫|(" in input:
        pass 
    elif "∫" in input: 
        pass
    elif "d/dx" in input: 
        pass 
    else:
        pass # handle thing, show error 


