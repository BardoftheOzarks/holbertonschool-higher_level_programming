def remove_char_at(str, n):
    new_str = ''
    i = 0
    while i < len(str):
        if i == n:
            i++
        else:
            new_str += str[i]
            i++
    return new_str
