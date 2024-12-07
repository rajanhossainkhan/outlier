def count_chars(s):
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

input_string = "Hello World  We are Aliens"
print(count_chars(input_string))