def remove_char_at(str, n):
    new_str = ''
    i = 0
    while i < len(str):
        if i == n:
            i = i + 1
        else:
            new_str += str[i]
            i = i + 1
    return new_str
