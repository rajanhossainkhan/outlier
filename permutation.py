def permute(str, step = 0):
    if step == len(str):
        print("".join(str))
    for i in range(step, len(str)):
        #swap current index with a step
        str_copy = [c for c in str]
        str_copy[step], str_copy[i] = str_copy[i], str_copy[step]

        #recurse the function
        permute(str_copy, step + 1)

string = "lkdjkdk"
permute(list(string))
