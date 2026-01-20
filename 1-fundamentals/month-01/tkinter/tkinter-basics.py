import tkinter as tk
from tkinter import messagebox

def add():
    global entry, listbox
    text = entry.get()
    if not text.strip():
        messagebox.showwarning("Error", "Empty text")
        return
    listbox.insert(tk.END, text)
    entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.title("My first app")

    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)

    btn = tk.Button(root, text="Add text", command=add)
    btn.pack()

    listbox = tk.Listbox(root, width=70)
    listbox.pack(pady=15)
    root.mainloop()
    
if __name__ == "__main__":
    main()
