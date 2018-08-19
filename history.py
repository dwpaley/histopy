import readline

def get_history():
    history = [
            readline.get_history_item(i+i) 
            for i in range(readline.get_current_history_length())
            ]
    print(readline.get_current_history_length())
    return history

def history():
    h = []
    hfull = get_history()
    for i, line in enumerate(hfull):
        if (line.lower().startswith('quit()') or 
                line.lower().startswith('exit()')):
            h = []
        else:
            h.append((i, line))
    for i, line in h:
        print('{}\t{}'.format(i, line))

                



