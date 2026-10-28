# Python Keyboard Event Logger — Learning Project

## Overview

This project is a simple Python application built with **Tkinter** to demonstrate keyboard event handling in a graphical user interface (GUI).

The application detects key presses while its window is active, displays the last pressed key and its timestamp, and saves a test event to a local text file when the Enter key is pressed.

This project was created for educational purposes as part of my cybersecurity learning journey.

## Features

- **Keyboard event handling:** Detects key presses inside the application's window.
- **Timestamping:** Records the time when a key is pressed.
- **GUI interface:** Displays the most recent keyboard event.
- **Local file handling:** Saves the Enter key event and its timestamp to `sensinfo.txt`.
- **Clear display:** Provides a button to reset the displayed message.

## Technologies Used

- Python 3
- Tkinter
- `datetime`
- `pathlib`
- `logging`

## Requirements

- Python 3 installed on your computer.
- Tkinter available in your Python installation.

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the Python file:

   ```bash
   python keyboard_logger.py
   ```

   Replace `keyboard_logger.py` with your actual Python filename if it is different.

4. Click inside the application window and press some keys.
5. Press Enter to trigger the test event and save it to `sensinfo.txt`.

## Security Warning and Ethical Use

**This project is intended strictly for educational purposes and authorized testing.**

- The application captures keyboard events only while its own window is active.
- It is not designed to monitor keyboard activity across the operating system.
- Do not use keyboard-monitoring techniques to collect passwords, personal information, or other sensitive data.
- Never deploy monitoring software on another person's device without their informed consent and proper authorization.
- Do not modify or distribute this project for covert surveillance, credential theft, or unauthorized data collection.

The purpose of this project is to understand Python event handling, GUI programming, file operations, and basic cybersecurity concepts in a controlled environment.

## Learning Objectives

- Understand how keyboard events work in Tkinter.
- Learn how to use event handlers and callback functions.
- Work with timestamps and file paths.
- Practice writing data to local files.
- Understand the importance of consent, privacy, and ethical security testing.

## Disclaimer

The author is not responsible for misuse of this project. Users are responsible for ensuring that their activities comply with applicable laws, privacy requirements, and ethical standards.
