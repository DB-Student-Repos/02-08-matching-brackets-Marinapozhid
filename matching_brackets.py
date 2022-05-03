#Dictionaries, Lists, Conditionals
# 1. Create Stack
def is_paired(input_string):
    d = dict(zip(['[', '{', '('], [']','}',')']))
    s = []
    for symb in input_string:
        if symb in d.keys():
           s.append(symb)

        elif symb in d.values():
            if not s:
                return False
                
            current_char = s.pop() #pick and return the last char in the stack
            if current_char == '(':
                if symb != ")":
                    return False
            if current_char == '{':
                if symb != "}":
                    return False
            if current_char == '[':
                if symb != "]":
                    return False


    return len(s) == 0
        


