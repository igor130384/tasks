import collections


def sum_of_square_digits(number):
    return sum(int(x) ** 2 for x in str(number))


def is_happy_number(num):
    i = 0
    if num == 0:
        return False
    while i <= 10:
        if num == 1:
            return True
        else:
            num = sum_of_square_digits(num)
            i += 1
            if i >= 10:
                return False


print(is_happy_number(13))
print(sum_of_square_digits(7))


def is_power_of_three(num):
    if num == 1:
        return True
    while num >= 1:
        num = num / 3
        if num == 1:
            return True
    return False


print(is_power_of_three(9))  # True


def get_number_explanation(count):
    match count:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'
        case 7:
            return 'prime number'
        case _:
            return 'just a number'


def letter_multiply(text: str, sim: str, num: int) -> str:
    for i in text:
        if sim in text:
            a = text.replace(sim, sim * num)
            return a


print(letter_multiply('python', 'p', 3))


def is_continuous_sequence(step):
    t = len(step) - 1
    if len(step) == 0 or len(step) == 1:
        return False
    index = 0
    while index < t:
        if step[index] == step[index + 1] - 1:
            index += 1
        else:
            return False
    return True


print(is_continuous_sequence([7]))


def compare_version(line: str, line2: str):
    line = line.split('.')
    line2 = line2.split('.')
    for i in range(len(line)):
        if line[i] == line2[i] and line[i + 1] == line2[i + 1]:
            return 0
        elif line[i] > line2[i]:
            return 1
        elif line[i] < line2[i]:
            return -1




print(compare_version('0.2', '0.12'))


def test_compare():
    assert compare_version('0.1', '0.2') == -1
    assert compare_version('0.2', '0.1') == 1
    assert compare_version('4.2', '4.2') == 0
    assert compare_version('0.2', '0.12') == -1
    assert compare_version('3.2', '4.12') == -1
    assert compare_version('3.2', '2.12') == 1
