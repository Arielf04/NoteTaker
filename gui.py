import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename()
    print(f"Selected file: {file_path}")

# Create the main window
root = tk.Tk()
root.title("Note Taker")

# Create and place the labels
tk.Label(root, text="From page:").grid(row=0, column=0, sticky=tk.W)
tk.Label(root, text="To page:").grid(row=1, column=0, sticky=tk.W)

# Create and place the entry fields
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Create and place the drop-down selector (combobox)
options = ["Automatic title", "Write your own title"]
combobox = ttk.Combobox(root, values=options)
combobox.set("Select an option")
combobox.grid(row=2, column=0, columnspan=2)

# Set the default option for the combobox
default_option = "Automatic title"
combobox.set(default_option)

# Create and place the browse file button
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=3, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
