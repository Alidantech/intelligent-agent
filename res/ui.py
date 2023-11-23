import tkinter as tk
import agent.checker as agent
import agent.suggestions as sg
import json


def on_button_click():
    input_text = text.get("1.0", tk.END).strip()
    textview.config(state=tk.NORMAL)
    textview.insert(tk.END, f"Umeandika: {input_text}\n")
    textview.config(state=tk.DISABLED)


def get_current_word(text_widget):
    cursor_position = text_widget.index(tk.INSERT)
    start = text_widget.search(r"\s", cursor_position, backwards=True, regexp=True)
    if start == "":
        start = "1.0"
    else:
        start = text_widget.index(f"{start}+1c")
    end = text_widget.search(r"\s", cursor_position, regexp=True)
    if end == "":
        end = tk.END
    return text_widget.get(start, end).strip()


def highlight_wrong_words(event):
    text.after(500, update_label)


def update_label():
    input_text = text.get("1.0", tk.END).strip()
    wrong_word_indexes = agent.check_sentence_words(input_text)

    # Remove any existing tags
    text.tag_delete("underline")

    # Get suggestions for the current word
    current_word = get_current_word(text)
    suggestions = sg.get_suggestions(current_word)

    # Update the label with suggestions
    label.config(text=f"Suggestions: {', '.join(suggestions)}")

    sentence_word_list = input_text.split(" ")

    # Check if any suggestion starts with the current word
    starts_with_current_word = any(s.startswith(current_word) for s in suggestions)

    # Apply red underline to the incorrect words if no suggestion starts with the current word
    if not starts_with_current_word:
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

    with open("ui_config.json", "r") as config_file:
        ui_config = json.load(config_file)

    window = tk.Tk()
    window.state("zoomed")
    window.title("Swahili Auto Correct")
    window.configure(bg=ui_config["entry"]["bg"])
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    text = tk.Text(window, wrap=tk.WORD)
    apply_styles(text, ui_config["entry"])
    text.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
    text.bind("<KeyRelease>", highlight_wrong_words)

    label = tk.Label(window, text="")
    apply_styles(label, ui_config["label"])
    label.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

    button = tk.Button(window, text="Submit", command=on_button_click)
    apply_styles(button, ui_config["button"])
    button.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

    textview = tk.Text(window, wrap=tk.WORD)
    apply_styles(textview, ui_config["textview"])
    textview.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

    window.mainloop()


start_app()
