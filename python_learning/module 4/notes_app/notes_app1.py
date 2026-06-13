import tkinter as tk
from tkinter import messagebox
from datetime import datetime

notes = []

# ---------------- ADD NOTE ---------------- #

def add_note():
    text = note_text.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Write something first!")
        return

    current_time = datetime.now().strftime("%d %b %Y | %I:%M %p")

    note = f"{current_time}\n{text}"

    notes.append(note)

    listbox.insert(tk.END, note)
    note_text.delete("1.0", tk.END)

# ---------------- DELETE NOTE ---------------- #

def delete_note():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a note first!")
        return

    index = selected[0]

    listbox.delete(index)
    notes.pop(index)

# ---------------- SEARCH NOTE ---------------- #

def search_note():

    query = search_entry.get().lower()

    listbox.delete(0, tk.END)

    for note in notes:
        if query in note.lower():
            listbox.insert(tk.END, note)

# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()

root.title("Advanced Notes App")
root.geometry("700x700")
root.configure(bg="#1e1e1e")

# ---------------- TITLE ---------------- #

title = tk.Label(
    root,
    text="📝 Advanced Notes App",
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=20)

# ---------------- SEARCH ---------------- #

search_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=40,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)
search_entry.pack(pady=10)

search_btn = tk.Button(
    root,
    text="Search",
    font=("Arial", 12, "bold"),
    bg="#0078ff",
    fg="white",
    command=search_note
)
search_btn.pack(pady=5)

# ---------------- TEXT AREA ---------------- #

note_text = tk.Text(
    root,
    height=8,
    width=60,
    font=("Arial", 14),
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)
note_text.pack(pady=20)

# ---------------- BUTTONS ---------------- #

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack()

add_btn = tk.Button(
    btn_frame,
    text="Add Note",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    width=15,
    command=add_note
)
add_btn.grid(row=0, column=0, padx=10)

delete_btn = tk.Button(
    btn_frame,
    text="Delete Note",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    width=15,
    command=delete_note
)
delete_btn.grid(row=0, column=1, padx=10)

# ---------------- NOTES LIST ---------------- #

listbox = tk.Listbox(
    root,
    width=80,
    height=18,
    font=("Arial", 12),
    bg="#2d2d2d",
    fg="white",
    selectbackground="#0078ff"
)
listbox.pack(pady=25)

# ---------------- START APP ---------------- #

root.mainloop()