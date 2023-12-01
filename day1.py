fp = open("day1.txt")

result = 0
count = 0
for input in fp.readlines():
    input = (
        input.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )
    if count <= 5:
        count += 1
        print(input)
    digits = []
    for num in input:
        if num.isdigit():
            digits.append(int(num))
    if len(digits) == 1:
        digits.append(digits[0])
    number = digits[0] * 10 + digits[-1]
    result += number
print(result)
