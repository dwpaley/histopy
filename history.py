import readline

def get_history():
    hlen = readline.get_current_history_length()
    h = []
    for i in range(hlen): h.append(readline.get_history_item(i+1))
    return h

def broken_get_history():
    hlen = readline.get_current_history_length()
    history = [readline.get_history_item(i+i) for i in range(hlen)]
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

                



