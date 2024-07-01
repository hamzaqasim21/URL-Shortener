import pyshorteners
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

win = tk.Tk()
win.title("URL Shorteners")
def short():
    url = entry_url.get()
    shorted_url = pyshorteners.Shortener()
    showinfo("Shorted URL",f"{shorted_url.tinyurl.short(url)}")
    print(f'{shorted_url.tinyurl.short(url)}')

url_label = tk.Label(win,
text='Enter URL Here :',)
url_label.grid(row=0,column=0)


entry_url = tk.Entry(win,
width=90,
bg='#69BEF6',
bd=8)
entry_url.grid(row=0,column=1,padx=40,pady=40)

button = ttk.Button(win,
text='Short',
command=short)
button.grid(row=1,column=1,columnspan=5)

win.mainloop()