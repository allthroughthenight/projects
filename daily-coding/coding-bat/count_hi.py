# Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
    my_list = list(str)
    hi_count = 0
    for num in range(len(my_list) -1):
        if my_list[num] == 'h' and my_list[num+1] == 'i':
            hi_count += 1

    return hi_count
