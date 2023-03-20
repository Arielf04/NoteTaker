import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def browse_file():
    pdf_path = filedialog.askopenfilename()

# Create the main window
root = tk.Tk()
root.title("Note Taker")
root.resizable(False, False)

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack(expand=True)

# Create and place the labels
tk.Label(frame, text="Pages:").grid(row=0, column=0, sticky=tk.W)


# Create and place the entry fields
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1)

def on_combobox_selected(event):
    selected_option = combobox.get()
    if selected_option == "Write your own title":
        entry_title.config(state='normal')  # Enable the text entry
    else:
        entry_title.config(state='disabled')  # Disable the text entry

# Create and place the drop-down selector (combobox)
options = ["Automatic title", "Write your own title"]
combobox = ttk.Combobox(frame, values=options, state='readonly')
combobox.set("Select an option")
combobox.grid(row=2, column=0, columnspan=2)
combobox.bind("<<ComboboxSelected>>", on_combobox_selected)  # Add a callback function to the combobox

# Set the default option for the combobox
default_option = "Automatic title"
combobox.set(default_option)

# Create and place the text entry field
entry_title = ttk.Entry(frame)
entry_title.grid(row=3, column=0, columnspan=2)
entry_title.config(state='disabled')  # Initially disable the text entry

# Create and place the browse file button
browse_button = tk.Button(frame, text="Browse", command=browse_file)
browse_button.grid(row=4, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
