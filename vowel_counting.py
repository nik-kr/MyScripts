'''
----Программа по подсчета гласных в тексте----
----Program for counting vowels in the text---
'''
# from tkinter import *
# from tkinter import ttk
from tkinter import *

class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry('500x500')
        self.MainFrame = AppFrame(self).pack()

class AppFrame(Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.
        self.TextEntry = Entry().pack()

def main() -> None:
    app = App()
    app.mainloop()
    pass
if __name__ == "__main__":
    main()