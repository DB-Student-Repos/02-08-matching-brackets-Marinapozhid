#Dictionaries, Lists, Conditionals

def is_paired(input_string):
    d = dict(zip('[{(', ']})'))
    s = []
    for symb in input_string:
        if symb in d.keys():
           s.append(symb)
        if symb in d.values():
            if not s:
                return False

        if s[-1] == d(symb):
            s.pop()
        else:
            return False

    return not s
        


