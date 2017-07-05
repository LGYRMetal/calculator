#-*- coding: utf-8 -*-

import tkinter

class Calculator:
    """
    一个用python3实现的计算器
    """
    def __init__(self, parent):
        parent.title("计算器")
        parent.resizable(width=tkinter.NO, height=tkinter.NO)
        parent.config(bd=2, padx=5, pady=5)
        self.showFrame = tkinter.Frame(master=parent, bd=1)
       #self.showFrame.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        self.showFrame.grid(row=0, column=0, rowspan=5, columnspan=6)
        self.showLab = tkinter.Label(master=self.showFrame)
        self.showLab.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        self.showEntry = tkinter.Entry(master=self.showFrame)
        self.showEntry.pack(expand=tkinter.YES, fill=tkinter.BOTH)

        tkinter.Button(parent, text='7', command=None).grid(row=6, column=0)

def start():
    Calculator(tkinter.Tk())
    tkinter.mainloop()

if __name__ == "__main__":
    start()

