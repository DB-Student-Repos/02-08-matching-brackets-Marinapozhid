#Dictionaries, Lists, Conditionals

def is_paired(input_string):
    d = dict(zip('[{(', ']})'))
    s = []

    for bracket in input_string:
        if bracket in d.keys():
           s.append(bracket)

        elif bracket in d.values():
            if not s:
                return False

            current_bracket = s.pop()
            if d[current_bracket] != bracket:
                return False

    return not s
        


