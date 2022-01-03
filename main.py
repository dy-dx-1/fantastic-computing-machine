import tkinter as tk
from tkinter.constants import NSEW

root = tk.Tk()
root.title("Calculator") 
root.geometry("400x600") 
root.rowconfigure(6)
root.columnconfigure(3) 
output_label = tk.Label(root, text = "")
def set_up_grid():
    for n in range(6): 
        tk.Grid.rowconfigure(root, index = n, weight=1) 
        if n<=3: tk.Grid.columnconfigure(root, index=n, weight = 1) 
    # Placing the output label 
    output_label.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    create_buttons() 

def update_screen(new_text): 
        old_text = output_label.cget("text") 
        output_label.configure(text= f"{old_text}{new_text}")

def create_buttons(): #TODO: use symbols instead of text for the text 
    m_der = tk.Button(root, text="d/dxE") 
    m_inter = tk.Button(root, text = "intE") 
    der = tk.Button(root, text = "d/dx") 
    inter = tk.Button(root, text = "inte") 
    fun = tk.Button(root, text = "f(x)") 
    system = tk.Button(root, text = "{}") 
    var = tk.Button(root, text = "x", command=lambda: update_screen("x")) 

    sum_ = tk.Button(root, text ="+", command=lambda: update_screen("+")) 
    subs = tk.Button(root, text = "-", command=lambda: update_screen("-")) 
    div = tk.Button(root, text = "/", command=lambda: update_screen("/")) 
    mul = tk.Button(root, text = "*", command=lambda: update_screen("*")) 
    clear = tk.Button(root, text = "CS") 
    equals = tk.Button(root, text="=") 
    dot = tk.Button(root, text= ".", command=lambda: update_screen(".")) 

    one = tk.Button(root, text = "1", command=lambda: update_screen("1")) 
    two = tk.Button(root, text = "2", command=lambda: update_screen("2")) 
    three = tk.Button(root, text = "3", command=lambda: update_screen("3")) 
    four = tk.Button(root, text = "4", command=lambda: update_screen("4")) 
    five = tk.Button(root, text="5", command=lambda: update_screen("5")) 
    six = tk.Button(root, text= "6", command=lambda: update_screen("6")) 
    seven = tk.Button(root, text = "7", command=lambda: update_screen("7")) 
    eight = tk.Button(root, text="8", command=lambda: update_screen("8")) 
    nine = tk.Button(root, text="9", command=lambda: update_screen("9")) 
    o = tk.Button(root, text="0", command=lambda: update_screen("0")) 
    
    button_list = [system, inter, m_inter, var, fun, der, m_der, div, one, two, three, mul, four, five, six, subs,seven, eight, nine, sum_, o, dot, clear, equals]
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
        


def main():
    set_up_grid() 
    root.mainloop()
if __name__ == "__main__": 
    main() 