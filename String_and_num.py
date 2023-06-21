def duplicate_count(text):
    dict = {}
    for i in text.lower():
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    num = 0
    for key, value in dict.items():
        if dict[key] > 1:
            num += 1
    return num


print(duplicate_count("abcdeaB"))
