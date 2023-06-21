from audioop import reverse


def even_num(num):
    if num & 1 == 1:
        return "Нечетное"
    else:
        return "Четное"


print(even_num(1003))


def reverse1(line: str):
    i = len(line) - 1
    line1 = ''
    while i >= 0:
        line1 = line1 + line[i]
        i -= 1
    return line1


print(reverse1("Игорь"))


def fizz_buzz(num, num1):
    line = []
    for i in range(num, num1 + 1):
        # print(i, end=' ')
        if i % 3 == 0 and i % 5 == 0:
            line.append('FizzBuzz')
        if i % 3 == 0:
            line.append("Fizz")
        if i % 5 == 0:
            line.append("Buzz")
        else:
            line.append(str(i))
    return ' '.join(line)


print(fizz_buzz(1, 30))


def first_non_repeating_letter(s):
    slovary = dict()
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s
    for i in s:
        if i in slovary:
            slovary[i] += 1
        else:
            slovary[i] = 1
    sl = list(slovary)
    if len(sl) <= 1:
        return ''
    min1 = min(slovary.values())
    word = []
    for key, value in slovary.items():
        if min1 == value:
            word.append(key)
            if len(word) > 1:
                return ''
        return ''.join(word)

print(first_non_repeating_letter('abba'))