# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
    split = list(str)
    length = len(str)
    middle = length/2
    half = ''
    half = half.join(split[0:middle])
    return half

