from ast import parse  

def process_result(input):  # This will be called if the other buttons for functions or systems, etc have not been called 
    while " " in input: input = input.replace(" ", "") 
    while "^" in input: input = input.replace("^", "**") 
    return eval(input, {"__builtins__":None})  ########################################ONLY USING EVAL SINCE THIS IS A SMALL NON PRODUCTION PROJECT 

print(process_result("4 - + 45^2 - 23")) 
