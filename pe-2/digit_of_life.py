def birthday_digit(birthday):
    digit = 0
    for ch in birthday:
        digit += int(ch)
    if digit >= 10:
        digit = birthday_digit(str(digit))
    return digit

birthday = input("Your birthday: ")
print(birthday_digit(birthday))