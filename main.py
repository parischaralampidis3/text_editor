import tkinter as tk

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title( "Text editor" )
        self.geometry( "600x500" )

        self.columnconfigure( 0, weight = 1)
        self.rowconfigure( 1, weight = 1 )
        
        self.text_window = tk.Text( self, height = 8 )
        self.text_window.grid(row = 1, column = 0, padx = 10, pady = 10,  sticky = "nsew" )

    def text_editor_iput(self):
        text_input = self.text_window.get("1.0", "end-1c")
        print("Text input", text_input)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()