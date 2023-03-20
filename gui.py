import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedTk

import gui

custom_font = ('Helvetica', 14)

def browse_file():
    gui.pdf_path = filedialog.askopenfilename()

# Create the main window
root = ThemedTk(theme="Clearlooks")
root.title("Note Taker")
root.resizable(False, False)

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack(expand=True)

# Create and place the labels
tk.Label(frame, text="Pages:", font=custom_font).grid(row=0, column=0, sticky=tk.W)

# Create and place the entry fields
entry1 = tk.Entry(frame, font=custom_font)
entry1.grid(row=0, column=1, padx=5, pady=10)

def on_combobox_selected(event):
    selected_option = combobox.get()
    if selected_option == "Write your own title":
        entry_title.config(state='normal')  # Enable the text entry
    else:
        entry_title.config(state='disabled')  # Disable the text entry

# Create and place the drop-down selector (combobox)
options = ["Automatic title", "Write your own title"]
combobox = ttk.Combobox(frame, values=options, state='readonly', font = custom_font)
combobox.set("Select an option")
combobox.grid(row=2, column=0, columnspan=2, padx=5, pady=2)
combobox.bind("<<ComboboxSelected>>", on_combobox_selected)  # Add a callback function to the combobox

# Set the default option for the combobox
default_option = "Automatic title"
combobox.set(default_option)

# Create and place the text entry field
entry_title = ttk.Entry(frame, font=custom_font)
entry_title.grid(row=3, column=0, columnspan=2)
entry_title.config(state='disabled')  # Initially disable the text entry

# Create and place the browse file button
browse_button = tk.Button(frame, text="Browse", command=browse_file, font=custom_font)
browse_button.grid(row=4, column=0, columnspan=1, padx=10, pady=10, sticky='nsew')

# Create and place the browse file button
take_notes_button = tk.Button(frame, text="Take notes", font=custom_font)
take_notes_button.grid(row=4, column=1, columnspan=1, padx=10, pady=10, sticky='nsew')

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(4, weight=1)

# Start the main event loop
root.mainloop()
