from sympy import symbols, parse_expr, evalf
x = symbols("x")
from functions import Function
def process_result(input):  # processes what is currently on the calculator screen 
    if not input.count('(') == input.count(')'): return "Parenthesis's unmatched."
    while " " in input: input = input.replace(" ", "")  
    while "^" in input: input = input.replace("^", "**")
    try: 
        expr = parse_expr(input)
    except SyntaxError: 
        return "SyntaxError"
    if input[:3] != "f(x)": return expr.evalf()  ########################################ONLY USING EVAL SINCE THIS IS A SMALL NON PRODUCTION PROJECT

    # if we pass here, we need to evaluate further 
    # input = Function.process_implicit_mul(input, x)
