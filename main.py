# Library Management System main.py

from frontend.gui import LibraryGUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()
