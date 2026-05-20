import tkinter as tk
from tkinter import messagebox

notes = []

def add_note():
    note = text_area.get("1.0", tk.END).strip()

    if note:
        notes.append(note)
        listbox.insert(tk.END, note)
        text_area.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Warning", "Please write something!")

def delete_note():
    selected = listbox.curselection()

    if selected:
        index = selected[0]
        listbox.delete(index)
        notes.pop(index)
    else:
        messagebox.showwarning("Warning", "Select a note first!")

root = tk.Tk()
root.title("Notes App")
root.geometry("500x500")

title = tk.Label(root, text="📝 Notes App", font=("Arial", 20))
title.pack(pady=10)

text_area = tk.Text(root, height=5, width=40)
text_area.pack(pady=10)

add_btn = tk.Button(root, text="Add Note", command=add_note)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Selected", command=delete_note)
delete_btn.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

root.mainloop()