def parentheses(text):
    open = 0
    close = 0
    for i in text:
        if i == '(':
            open += 1
        elif i == ')':
            close += 1
        if close>open:
            return -1
    if open == close:
        return 0
    return 1