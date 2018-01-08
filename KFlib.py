from tkinter import *
from tkinter.ttk import *
import win32gui


def gui_finder():

    arr = []

    def start_parsing(event):
        arr.append(comboboxValues.get().split(' ', maxsplit=1))
        wProcessWin.quit()

    def window_callback(hwnd, n):
        title = win32gui.GetWindowText(hwnd)
        if title != '' and win32gui.IsWindowVisible(hwnd):
            processList.append(str(hwnd) + ' ' + title)

    wProcessWin = Tk()
    wProcessWin.geometry('234x78')
    wProcessWin.resizable(width='false', height='false')
    wProcessWin.title('finderGui')
    Label(text='Select windows:').place(x=6, y=0)
    processList = []
    comboboxValues = StringVar()
    win32gui.EnumWindows(window_callback, 0)
    Combobox(wProcessWin, textvariable=comboboxValues, value=processList, width=33).place(x=6, y=20)
    wButton = Button(wProcessWin, text='Start', width=14)
    wButton.bind("<Button-1>", start_parsing)
    wButton.place(x=134, y=47)
    wProcessWin.mainloop()
    return arr












