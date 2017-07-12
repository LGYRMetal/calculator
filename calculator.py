#-*- coding: utf-8 -*-

import tkinter

class Calculator:
    """
    一个用python3实现的计算器
    """

    # buttons的键的含义(行，列，跨行数，跨列数)
    buttons = {
            (2, 0, 1, 1): '7', 
            (2, 1, 1, 1): '8',
            (2, 2, 1, 1): '9',
            (2, 3, 1, 1): '除',
            (2, 4, 1, 1): '返回',
            (2, 5, 1, 1): '退格',
            (3, 0, 1, 1): '4',
            (3, 1, 1, 1): '5',
            (3, 2, 1, 1): '6',
            (3, 3, 1, 1): 'x',
            (3, 4, 1, 1): '(',
            (3, 5, 1, 1): ')',
            (4, 0, 1, 1): '1',
            (4, 1, 1, 1): '2',
            (4, 2, 1, 1): '3',
            (4, 3, 1, 1): '-',
            (4, 4, 1, 1): '平方',
            (4, 5, 1, 1): '开平方',
            (5, 0, 1, 1): '0',
            (5, 1, 1, 1): '.',
            (5, 2, 1, 1): '%',
            (5, 3, 1, 1): '+',
            (5, 4, 2, 1): '=',
            }
    def __init__(self, parent):
        self.mainWindow = parent

        parent.title("计算器")
        parent.resizable(width=tkinter.NO, height=tkinter.NO)
       #parent.config(bd=2, padx=5, pady=5)
        self.showFrame = tkinter.Frame(parent)
       #self.showFrame.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        self.showFrame.grid(row=0, column=0, columnspan=6)
        self.showLab = tkinter.Label(self.showFrame)
        self.showLab.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        self.showEntry = tkinter.Entry(self.showFrame, justify=tkinter.RIGHT)
        self.showEntry.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        self.__addButton(parent, self.buttons)
        
    def __compute(expression):
        if expression:
            
        return ''

    def __addButton(self, parent, buttons):
        """
        向计算器主窗口添加按键
        parent: 父窗口
        buttons: 按键字典
        """
        def equalClick():
            result = Calculator.__compute(self.showEntry.get())
            self.showLab.config(text=self.showEntry.get() + ' = ' + result)
            self.showEntry.delete(0, tkinter.END)
            self.showEntry.insert(tkinter.END, result)

        for row, col, rowspan, colspan in buttons:
            bt = buttons[(row, col, rowspan, colspan)] # button text

            def click(bt=bt):
                if bt == '=':
                    equalClick()
                else:
                    self.showEntry.insert(tkinter.END, bt)

            tkinter.Button(parent, text=bt, command=click).grid(
                    row=row,
                    column=col,
                    rowspan=rowspan,
                    columnspan=colspan)

def start():
    Calculator(tkinter.Tk())
    tkinter.mainloop()

if __name__ == "__main__":
    start()

