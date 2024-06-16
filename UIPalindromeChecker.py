#IMPORTING FILES
import tkinter as tk
from tkinter import ttk
import os.path
import csv
from tkinter import messagebox

#window diamensions
window = tk.Tk()
window.geometry("640x400")
window.title("PALINDROME CHECKER")
window.resizable(0, 0)
window['bg'] = "#CAA8F5"

#file naming
txt_file = 'Palindrome.txt'
csv_file = 'Reverse.csv'

# create the text file
if not os.path.exists(txt_file):
    with open(txt_file, 'w', newline='') as fp:
        fp.write('PALINDROME LIST' + '\n' + '=======================' + '\n')

# create the csv file
if not os.path.exists(csv_file):
    with open(csv_file, 'w', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(['Given', 'Reverse'])

#to check the user input and clear if its not alnum
def verify_user_entry(event):
    reverse_label.config(text="")
    if not event.char.isalnum():
        g_input_val.delete(0, tk.END)
        g_input_val.insert(0, g_input_val.get()[::-1])


#to clear all text in the textbox while toggling between admin and user
def clear_all():
    g_input_val.delete(0, tk.END)
    reverse_label.config(text="")

# the reverse function with popups
def show_reverse():
    g_string = g_input_val.get()
    # result_string = ""
    if (len(g_string.strip()) > 0):
        result_string = g_string[::-1]
        reverse_label.config(text=result_string)
        record_data(privilege.get())
    else:
        messagebox.showwarning("Empty", "Input is mandatory")
    if (g_string == result_string):
        messagebox.showinfo(result_string, "PALINDROME")
    else:
        messagebox.showinfo(result_string, "NOT A PALINDROME  ")

# to record file into the text and csv files
def record_data(user_type):
    if (user_type == 1):
        g_string = g_input_val.get()
        reversed_str = g_string[::-1]
        if (g_string == reversed_str):
            with open(txt_file, 'a', newline='') as fp:
                fp.write(g_string + '\n')
        else:
            with open(csv_file,'a',newline='') as fp:
                writer = csv.writer(fp)
                writer.writerow([g_string,reversed_str])

#privilege is used for button to be selected
privilege = tk.IntVar()
window_label = ttk.Label(window, text="Palindrome Check")
window_label.grid(row=0, column=0, sticky=tk.W, padx=20, pady=20,)

#admin radiobutton
admin_rdo_button = ttk.Radiobutton(window, text="Administrator", variable=privilege, value=0, command=clear_all)
#button with value=0 will be selected
admin_rdo_button.grid(row=1, column=0, sticky=tk.W, padx=20, pady=20)

#user radiobutton
user_rdo_button = ttk.Radiobutton(window, text="User", variable=privilege, value=1, command=clear_all)
user_rdo_button.grid(row=1, column=1, sticky=tk.W, padx=20, pady=20)

#enter the string label
g_input = ttk.Label(window, text="Enter the string")
g_input.grid(row=2, column=0, sticky=tk.W, padx=20, pady=20)

#input area
g_input_val = ttk.Entry(window)
g_input_val.grid(row=2, column=1, sticky=tk.W, padx=20, pady=20)
g_input_val.bind('<KeyRelease>', verify_user_entry)

#reverse button
r_button = ttk.Button(window, text='Reverse', command=show_reverse)
r_button.grid(row=2, column=3, sticky=tk.W, padx=20, pady=20)

#reversed string label
g_output = ttk.Label(window, text="Reversed string: ")
g_output.grid(row=3, column=0, sticky=tk.W, padx=20, pady=20)

#output area
reverse_label = ttk.Label(window, text="")
reverse_label.grid(row=3, column=1, sticky=tk.W, padx=20, pady=20)

window.mainloop()