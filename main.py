from tkinter import *
import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        
        
        self.title( "Text editor" )
        self.geometry( "600x500" )
        self.navigation_menu()
        self.columnconfigure( 0, weight = 1)
        self.rowconfigure( 1, weight = 1 )

       
      
        
        self.text_window = tk.Text( self, height = 8 )
        self.text_window.grid(row = 1, column = 0, padx = 10, pady = 10,  sticky = "nsew" )

    def text_editor_iput(self):
        text_input = self.text_window.get("1.0", "end-1c")
        print("Text input", text_input)
    
    def navigation_menu(self):  
        self.menu = Menu(self, background= "#ffffff", foreground= "black", activebackground = "white", activeforeground= "black")
        self.config(menu=self.menu)

       
        file = Menu(self.menu , tearoff = 0, background= '#ffffff', foreground = "black",  )
        file.add_command(label="New")
        file.add_command(label = "Exit")
        self.menu.add_cascade(label="File", menu=file)
    
    
    def new_file(self):
        pass
    
    
    def exit(self):
        pass

    
    


if __name__ == "__main__":
    app = App()
    app.mainloop()