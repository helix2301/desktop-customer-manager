import tkinter as tk
import csv

f = open('results.csv', 'r')
reader = csv.reader(f)

def close_window ():
    master.destroy()

master = tk.Tk()
master.title('Customer List')
master.geometry('450x250')

Listbox = tk.Listbox(master)
Listbox.config(width=300, height=300)

with open('results.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)
  for item in your_list:

    Listbox.insert("end", item)


Listbox.grid(row=0, column=0)


#b1 = tk.Button(text='Submit', command = getInput).grid(row=9, column=1)
b2 = tk.Button(text='Close', command = close_window).grid(row=0, column=0)

master.mainloop()
