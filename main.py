import tkinter as tk
from tkinter import ttk


# Function to be called when the button is clicked
def on_button_click():
    label.config(text="Hello, " + entry.get())


# Create the main application window
app = tk.Tk()

# Set the window title to "Intelligent Agent"
app.title("Intelligent Agent")

# Set the window size to 400x300 pixels
app.geometry("400x300")

# Create and add widgets (label, entry, button)
label = tk.Label(app, text="Enter your name:")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=10)

# Create a modern-styled button using ttk
button = ttk.Button(app, text="Say Hello", command=on_button_click)
button.pack(pady=10)

# Start the main event loop
app.mainloop()
