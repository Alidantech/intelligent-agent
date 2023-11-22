import tkinter as tk
import agent.checker as agent
import json


def on_button_click():
    input_text = text.get(
        "1.0", tk.END
    ).strip()  # Get the entire content of the Text widget
    textview.config(state=tk.NORMAL)
    textview.insert(tk.END, f"Umeandika: {input_text}\n")
    textview.config(state=tk.DISABLED)


def update_label(event):
    input_text = text.get("1.0", tk.END).strip()
    wrong_word_indexes = agent.check_sentence_words(input_text)
    
    # Remove any existing tags
    text.tag_delete("underline")

    sentence_word_list = input_text.split(' ')
    # Apply red underline to the incorrect words
    for index in wrong_word_indexes:
        start = f"1.{index}"
        end = f"{start} wordend"
        text.tag_add("underline", start, end)
        text.tag_configure("underline", underline=True, foreground="red")


def apply_styles(widget, styles):
    for key, value in styles.items():
        widget[key] = value


def start_app():
    global textview
    global label
    global text

    # Read UI configuration from JSON file
    with open("ui_config.json", "r") as config_file:
        ui_config = json.load(config_file)

    # Create the main window
    window = tk.Tk()

    # Maximize the window
    window.state("zoomed")
    window.title("Swahili Auto Correct")

    # Set dark background color
    window.configure(bg=ui_config["entry"]["bg"])

    # Center the window elements
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    # Create text input box
    text = tk.Text(window, wrap=tk.WORD)
    apply_styles(text, ui_config["entry"])
    text.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
    text.bind("<KeyRelease>", update_label)

    # Create show text box (label)
    label = tk.Label(window, text="")
    apply_styles(label, ui_config["label"])
    label.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

    # Create a button
    button = tk.Button(window, text="Submit", command=on_button_click)
    apply_styles(button, ui_config["button"])
    button.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

    # Create a textview box
    textview = tk.Text(window, wrap=tk.WORD)
    apply_styles(textview, ui_config["textview"])
    textview.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

    # Run the Tkinter event loop
    window.mainloop()


# Call the function to create the maximized window
start_app()
