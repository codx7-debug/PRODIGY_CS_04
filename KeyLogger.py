
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

def on_key_press(event):
    timestamp = datetime.now().strftime("%H:%M:%S")
    key = event.keysym

    event_label.config(
        text=f"Last key pressed: {key} | Time: {timestamp}"
    )

    info = f"{key} | {timestamp}\n"

    if key.lower() == "return":
        sendinfo(info)
    else:
        sendinfo(info)    


def sendinfo(info):
    file_path = Path("./sensinfo.txt")

    try:
        with file_path.open("a", encoding="utf-8") as sensinfo:
            sensinfo.write(info)

        logging.info("Test event saved successfully.")

    except OSError as error:
        logging.error("Could not write the test file: %s", error)


def clear_display():
    event_label.config(
        text="Press a key inside this window to test."
    )


root = tk.Tk()
root.title("Keyboard Event Test")
root.geometry("500x300")
root.resizable(False, False)

title_label = ttk.Label(
    root,
    text="Keyboard Event Logger — Test Mode",
    font=("Arial", 14, "bold")
)
title_label.pack(pady=20)

instructions = ttk.Label(
    root,
    text="Click inside this window, then press a key."
)
instructions.pack(pady=5)

event_label = ttk.Label(
    root,
    text="Press a key inside this window to test.",
    wraplength=450
)
event_label.pack(pady=20)

clear_button = ttk.Button(
    root,
    text="Clear Display",
    command=clear_display
)
clear_button.pack(pady=10)

root.bind("<KeyPress>", on_key_press)

root.mainloop()
