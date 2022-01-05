from numpy import array
from sympy import symbols, lambdify, diff, integrate
from sympy.parsing.sympy_parser import parse_expr
from re import findall, split, sub

class NotFunctionError(Exception): 
    ERR_NOT_FUN_INPUT = """This is not a valid way to input a function.
            Please check that you are using a variable with a single letter (ex: 'x') and that you are only using the following operators: [+,-,/,*,^,(,)] """
    def __init__(self, calling, message):
        self.calling = calling 
        self.message = message 
    """
    calling: expression that caused the error 
    message: outputed explanation message on raise 
    """ 


class Function:
    x = symbols('x')  # The variable we'll use for all the calculations, represented by x in the class by default 

    @staticmethod
    def process_implicit_mul(string:str, var:str)->str: 
        str_list = list(string) 
        for i, char in enumerate(str_list): # Now check to the left and right if there is a digit without operator 
            if char == var:
                if i == 0:  # If it's at the very start, add multiplication to the right of term 
                    if str_list[1].isnumeric(): str_list.insert(1, "*") 
                elif i == len(str_list)-1:  # If it's at the very end, add it to the left of term 
                    if str_list[len(str_list)-2].isnumeric(): str_list.insert(len(str_list)-1, "*")  
                else: # if it's in another place, check right and left and then insert where needed 
                    if str_list[i-1].isnumeric(): str_list.insert(i, "*")
                    if str_list[i+1].isnumeric(): str_list.insert(i, "*")  
        return "".join(str_list)

    @staticmethod 
    def find_type(fun:str)->str: 
        for e in ["sin", "cos", "tan", "log", "ln"]: 
            if e in fun: return "Transcendental"
        return "Polynomial"
    @classmethod 
    def get_symbol(cls)->str:
        return f"The current accepted variable is {cls.x}, use the change_var method to change it" 

    @classmethod
    def change_var(cls, new_var:str)->None:
        cls.x = symbols(str(new_var)) 

    def __init__(self, fun):
        self.fun = parse_expr(fun)
    
    def return_function(self): 
        return self.fun

    def __repr__(self): 
        return f"""Function('{self.fun}', '{type(self)}')"""

    def __add__(self, other): 
        if type(other) is (PolynomialFunction or TranscendentalFunction): self.fun += other.return_function()
        elif type(other) is int: self.fun += other 
        else: pass # TODO: raise an error 

    def __sub__(self, other): 
            if type(other) is (PolynomialFunction or TranscendentalFunction): self.fun -= other.return_function()
            elif type(other) is int: self.fun -= other 
            else: pass # TODO: raise an error 

    def numerical_integration_rectangles(self, lower_bound:int = 0, superior_bound:int =10, rectangle_count=100)->float: 
        base = (superior_bound-lower_bound)/rectangle_count 
        total_area = 0 
        lower_x = lower_bound  
        for _ in range(rectangle_count): 
            x = lower_x + (base/2)
            total_area += self.fun.subs(self.x, x) * base 
            lower_x += base # shifting the lower bound towards the right 
        return total_area 

    def eval_integral(self, numerical=False, lower_bound: int = 0, superior_bound:int = 10):
        if numerical: return integrate(self.fun, (self.x, lower_bound, superior_bound))
        return integrate(self.fun, self.x) 

    def eval_derivative(self, numerical=False, x: float=0, order:int=1)->float: 
        if numerical: 
            return diff(self.fun, self.x, int(order)).subs(self.x, x) 
        return diff(self.fun, self.x, int(order))
    
    def calculate_outputs(self, abs: list = [n for n in range(0, 110, 10)])->dict: # Calculates outputs for the function
        try: 
            abs = array(abs) 
              # returns a dict showing the x's and associated y's 
            return dict(zip(abs, lambdify(self.x, self.fun, "numpy")(abs)))
        except TypeError: 
            return {"Error": """Please input a list of the X values to compute. Ex: "[0, 20, 40]"}"""} 


class PolynomialFunction(Function):
    @staticmethod #TODO: optimize this 
    def transform_into_function(function_string):
        if "=" in function_string: return None # We are assuming y = [x expression] form 
        vars = findall(r"[^\s\+\-\/\*\^1-9]", function_string) 
        if vars == []: return None 
        # Now, checking if another variable is present
        vars = list(set(vars)) # removing excess and reconverting to list to access by index after 
        if len(vars) != 1: return None # Means we have more than one var (ex: ['x', 'y'])
        var = vars[0]
        del vars # we don't need this anymore 
        expr = Function.process_implicit_mul(function_string, var)
        if "xx" in expr: # if the person inputted something like 3xxx+4, it -> 3*xxx+4. I couldn't manage to make it work with the loop, so I'll just brute force it
            equivalences = [("x*"*n)[:-1] for n in range(2,7)]
            for element in split(r"[+-/*\s]", expr): 
                if "xx" in element: 
                    for degree in range(2,7): 
                        if "x"*degree in element: 
                            expr = expr.replace("x"*degree, equivalences[degree-2])
        if "^" in expr: expr = sub("\^", "**", expr)
        return expr                  

    def __init__(self, fun : str):  # Default creation is with 'standard' form, ex: "4x + 45-4x^2"
        f = self.transform_into_function(fun)
        if f is None: raise NotFunctionError(str, NotFunctionError.ERR_NOT_FUN_INPUT)
        self.fun = parse_expr(f)
        

class TranscendentalFunction(Function): 
    def __init__(self, fun):
        self.fun = parse_expr(fun)  # TODO: right now directly parsing but we'll have to add some checks 
    def taylor_approx(self, degree: int)->str: # TODO: return taylor approximation 
        pass 
