👁️ Basic Keylogger Program (Task 04)
Project Overview
This project is a foundational programming task for SkillCraft Technology focused on low-level system interaction. It implements a simple Keylogger using Python's pynput library to monitor and record keystrokes.

The program's core function is to log every key press, including special keys (like [enter] and [space]), along with a timestamp, and save the data to a local file.

Core Skill
System monitoring, input handling, and foundational knowledge of potential malware techniques (for defensive analysis).

🚨 Ethical Warning (Read Carefully)
This tool is for educational purposes ONLY.

DO NOT use this program on any computer you do not own or have explicit permission to monitor.

Unauthorized use of a keylogger is illegal, unethical, and a serious violation of privacy.

The developer of this code disclaims all responsibility for any misuse.

🚀 Getting Started
Prerequisites
You need a standard installation of Python 3. This program requires the pynput library to interface with the keyboard listener.

Installation
Install pynput: Open your terminal or command prompt and run the following command:

Bash

pip install pynput
Save the Code: Save the Python code as basic_keylogger.py.

🛠️ Usage
Running the Program
Execute the script directly from your terminal:

Bash

python basic_keylogger.py
Program Flow
Start-up: The program initializes the keyboard listener and prints a message indicating that logging has started.

Logging: As long as the script is running, all physical key presses on the system are captured.

File Output: Keystrokes are immediately written to the keystrokes_log.txt file in the same directory, timestamped for chronological record-keeping.

Stopping: To stop the logger, press the Esc (Escape) key while the program's terminal window is active.

Log File Example (keystrokes_log.txt)
The log file includes timestamps for every key event:

Plaintext

2025-09-28 18:35:01: T
2025-09-28 18:35:01: h
2025-09-28 18:35:02: i
2025-09-28 18:35:03: [space]
2025-09-28 18:35:05: a
2025-09-28 18:35:05: [enter]
⚙️ How It Works
The program operates using the pynput.keyboard.Listener thread:

Event-Driven: The listener thread runs continuously in the background, waiting for keyboard events.

on_press Function: When a key is pressed:

It attempts to get the standard character (key.char) for regular letters, numbers, and symbols.

If the key is special (like Shift, Ctrl, or Enter), it catches the AttributeError and logs the key's name (e.g., [enter]).

Logging: The log_key helper function prepends a timestamp and writes the captured key to the designated text file in append mode ("a").

on_release Function: This function is configured to stop the listener thread when the user presses the Esc key, safely terminating the logging process.
