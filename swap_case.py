def swap_case(s):
    new_string = ''
    for c in s:
        if c.isupper() == True:
            new_string = new_string + c.lower()
        else:
            new_string = new_string + c.upper()

    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    