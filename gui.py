import tkinter as tk
from tkinter.constants import NSEW
from basic_operations import process_result

root = tk.Tk()
root.title("Calculator") 
root.geometry("400x600") 
root.rowconfigure(6)
root.columnconfigure(3) 
output_label = tk.Label(root, text = "")

def set_up_grid():
    for n in range(9): 
        tk.Grid.rowconfigure(root, index = n, weight=1) 
        if n<=3: tk.Grid.columnconfigure(root, index=n, weight = 1) 
    # Placing the output label 
    output_label.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    create_buttons() 

def create_buttons(): #TODO: use symbols instead of text for the text 
    m_der = tk.Button(root, text="d/dx(f|eval)", command=lambda: append_screen("d/dx|("), state="disabled") 
    m_inter = tk.Button(root, text = "∫|x=eval", command= lambda: append_screen("∫|("), state="disabled") 
    der = tk.Button(root, text = "d/dx", command = lambda: append_screen("d/dx("), state="disabled") 
    inter = tk.Button(root, text = "∫", command=lambda: append_screen("∫"), state = "disabled")   
    fun = tk.Button(root, text = "f(x)", command=lambda: function_mode()) 
    system = tk.Button(root, text = "{eq|eq}", command=lambda:update_screen("{")) 
    var = tk.Button(root, text = "x", command=lambda: append_screen("x"), state="disabled") 
    
    sin = tk.Button(root, text="sin()", command = lambda:append_screen("sin(")) 
    cos = tk.Button(root, text="cos()", command=lambda: append_screen("cos(")) 
    tan = tk.Button(root, text="tan()", command=lambda: append_screen("tan("))  
    log = tk.Button(root, text="log(eval;base)", command=lambda: append_screen("log(")) 
    sep = tk.Button(root, text="|", command=lambda: append_screen("|")) 
    pi  = tk.Button(root, text="π", command=lambda: append_screen("π")) 
    lpar = tk.Button(root, text = "(", command = lambda: append_screen("("))  
    rpar = tk.Button(root, text = ")", command = lambda: append_screen(")")) 
    
    sum_ = tk.Button(root, text ="+", command=lambda: append_screen("+")) 
    subs = tk.Button(root, text = "-", command=lambda: append_screen("-")) 
    div = tk.Button(root, text = "/", command=lambda: append_screen("/")) 
    mul = tk.Button(root, text = "*", command=lambda: append_screen("*")) 
    clear = tk.Button(root, text = "CS", command= lambda: update_screen("")) 
    equals = tk.Button(root, text="=", command=lambda: update_screen(process_result(output_label.cget("text"))))  ## This is just temp for now well have to include support for other adavanced ops 
    dot = tk.Button(root, text= ".", command=lambda: append_screen(".")) 

    one = tk.Button(root, text = "1", command=lambda: append_screen("1")) 
    two = tk.Button(root, text = "2", command=lambda: append_screen("2")) 
    three = tk.Button(root, text = "3", command=lambda: append_screen("3")) 
    four = tk.Button(root, text = "4", command=lambda: append_screen("4")) 
    five = tk.Button(root, text="5", command=lambda: append_screen("5")) 
    six = tk.Button(root, text= "6", command=lambda: append_screen("6")) 
    seven = tk.Button(root, text = "7", command=lambda: append_screen("7")) 
    eight = tk.Button(root, text="8", command=lambda: append_screen("8")) 
    nine = tk.Button(root, text="9", command=lambda: append_screen("9")) 
    o = tk.Button(root, text="0", command=lambda: append_screen("0")) 
    
    def append_screen(new_text): 
            old_text = output_label.cget("text") 
            output_label.configure(text= f"{old_text}{new_text}")

    def update_screen(new_text): 
        output_label.configure(text = new_text)
        for button in [m_der, m_inter, inter, der, var]: button["state"] = "disabled"

    def function_mode():
        output_label.configure(text= "f(x); ") 
        for button in [m_der, m_inter, inter, der, var]: button["state"] = "normal"

    button_list = [system, inter, m_inter, var, fun, der, m_der, div, one, two, three, mul, four, five, six, subs,seven, eight, nine, sum_, o, dot, clear, equals, sin, cos, tan, log, sep, pi, lpar, rpar ]
    row = 0 
    for index, button in enumerate(button_list):
        if index % 4==0: 
            column = 0
        elif index % 2==0: 
            column = 2 
        elif (index+3)%4==0:
            column = 1 
        else: 
            column=3
            button.grid(row= row+1, column= column, sticky=NSEW) 
            row+=1 
            continue
        button.grid(row= row+1, column= column, sticky=NSEW) 
        #### All of these if/elses and the use of guide are based on patterns I saw in the 'index matrix' -> serve to avoid an O(n^2) solution 
        # (even though it doesnt really matter with such small data count) 