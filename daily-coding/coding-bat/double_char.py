# Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
    my_list = list(str)
    dbl_char = ''
    for char in my_list:
        dbl_char += char
        dbl_char += char

    return dbl_char

