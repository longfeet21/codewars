'''
4 kyu

In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them
'''

int_lib_a = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fifteen": 15,
    "eighteen": 18,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
}

int_lib_b = {
    "thousand": 1000,
    "million": 1000000
}


def parse_int(string):
    num = 0
    group = 0
    for w in string.replace(' and ', ' ').replace('-', ' ').split():
        if w == "hundred":
            group *= int_lib_a[w]
        elif w in int_lib_a:
            group += int_lib_a[w]
        elif "teen" in w:
            group += 10 + int_lib_a[w[:-4]]
        else:
            num += group * int_lib_b[w]
            group = 0
    return num + group


def define_check(x, y):
    if parse_int(x) == y:
        return True
    return False


print(define_check('one', 1))
print(define_check('seven hundred eighty-three thousand nine hundred and nineteen', 783919))
print(define_check('two hundred forty-six', 246))
