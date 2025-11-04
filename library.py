import tkinter as tk
from tkinter import messagebox, ttk

# ---------------------------
# Sorting and Binary Search
# ---------------------------

def bubble_sort(book_list):
    n = len(book_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if book_list[j][0].lower() > book_list[j + 1][0].lower():
                book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]
    return book_list


def binary_search(book_list, key):
    low = 0
    high = len(book_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if book_list[mid][0].lower() == key.lower():
            return mid
        elif book_list[mid][0].lower() < key.lower():
            low = mid + 1
        else:
            high = mid - 1
    return -1


# ---------------------------
# GUI FUNCTIONS
# ---------------------------

def sort_books():
    global books
    books = bubble_sort(books)
    update_listbox()
    messagebox.showinfo("Sorted", "Books sorted alphabetically by title.")


def search_book():
    global books
    key = search_entry.get().strip()
    if not key:
        messagebox.showwarning("Warning", "Please enter a book title to search.")
        return
    index = binary_search(books, key)
    if index != -1:
        messagebox.showinfo("Found", f"Book Found!\n\nTitle: {books[index][0]}\nAuthor: {books[index][1]}")
    else:
        messagebox.showerror("Not Found", f"No book titled '{key}' found.")


def add_book():
    title = title_entry.get().strip()
    author = author_entry.get().strip()
    if not title or not author:
        messagebox.showwarning("Warning", "Please enter both title and author.")
        return
    books.append((title, author))
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    update_listbox()


def update_listbox():
    listbox.delete(*listbox.get_children())
    for i, (title, author) in enumerate(books, start=1):
        listbox.insert("", "end", values=(i, title, author))


# ---------------------------
# GUI SETUP
# ---------------------------

root = tk.Tk()
root.title("Library Book Search Optimization")
root.geometry("600x500")
root.config(bg="#f0f5ff")

tk.Label(root, text="📚 Library Book Search Optimization", font=("Arial", 16, "bold"), bg="#f0f5ff").pack(pady=10)

# Frame for adding books
frame_add = tk.Frame(root, bg="#f0f5ff")
frame_add.pack(pady=10)

tk.Label(frame_add, text="Title:", bg="#f0f5ff").grid(row=0, column=0, padx=5)
title_entry = tk.Entry(frame_add, width=25)
title_entry.grid(row=0, column=1, padx=5)

tk.Label(frame_add, text="Author:", bg="#f0f5ff").grid(row=0, column=2, padx=5)
author_entry = tk.Entry(frame_add, width=25)
author_entry.grid(row=0, column=3, padx=5)

tk.Button(frame_add, text="Add Book", command=add_book, bg="#4CAF50", fg="white", width=10).grid(row=0, column=4, padx=5)

# Search section
frame_search = tk.Frame(root, bg="#f0f5ff")
frame_search.pack(pady=10)

tk.Label(frame_search, text="Search Book Title:", bg="#f0f5ff").grid(row=0, column=0, padx=5)
search_entry = tk.Entry(frame_search, width=30)
search_entry.grid(row=0, column=1, padx=5)
tk.Button(frame_search, text="Search", command=search_book, bg="#2196F3", fg="white", width=10).grid(row=0, column=2, padx=5)
tk.Button(frame_search, text="Sort Books", command=sort_books, bg="#FF9800", fg="white", width=10).grid(row=0, column=3, padx=5)

# Book list display
cols = ("S.No", "Title", "Author")
listbox = ttk.Treeview(root, columns=cols, show="headings", height=10)
for col in cols:
    listbox.heading(col, text=col)
    listbox.column(col, width=180)
listbox.pack(pady=10)

# Initial Book Data
books = [
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("1984", "George Orwell"),
    ("Pride and Prejudice", "Jane Austen"),
    ("Moby-Dick", "Herman Melville"),
]

update_listbox()

root.mainloop()