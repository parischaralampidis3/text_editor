from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.title("Text editor")
        self.geometry("600x500")
        self.navigation_menu()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Main text area
        self.text_window = tk.Text(self, height=8)
        self.text_window.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    def text_editor_input(self):
        text_input = self.text_window.get("1.0", "end-1c")
        print("Text input:", text_input)

    def navigation_menu(self):  
        self.menu = Menu(
            self,
            background="#ffffff",
            foreground="black",
            activebackground="white",
            activeforeground="black"
        )
        self.config(menu=self.menu)

        file = Menu(
            self.menu,
            tearoff=0,
            background="#ffffff",
            foreground="black"
        )
        file.add_command(label="New", command=self.new_file)
        file.add_command(label="Save",command=self.save_file)
        file.add_command(label="Exit", command=self.exit_app)
        self.menu.add_cascade(label="File", menu=file)

    def new_file(self):
        """Clear the text editor."""
        self.text_window.delete("1.0", END)
        print("New file created (text area cleared).")

    def save_file(self):
        """Save the text editor"""
        file_path = filedialog.asksaveasfilename(
            defaultextension= ".txt",
            filetypes=[("Text Files","*.txt"),("All Files","*.*")]
        )
        if file_path:
            try:
                content = self.text_window.get("1.0","end-1c")
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(content)
                messagebox.showinfo("Success",f"file saved at{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:{e}")

    def exit_app(self):
        """Exit the application."""
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
