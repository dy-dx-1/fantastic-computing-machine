import tkinter as tk
from typing import Collection 
root = tk.Tk()

def create_base():
    # First let's create the base 
    root.title("Calculator") 
    root.geometry("400x600") 
    # Placing the output label 
    root.grid_columnconfigure(2, weight=1)
    output_label = tk.Label(root, text = "THIS IS OUTPUT")
    output_label.grid(row=0, column=0, columnspan=4)

def main():
    create_base() 
    root.mainloop()
if __name__ == "__main__": 
    main() 