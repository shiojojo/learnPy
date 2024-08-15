check_palindrome = input("palindrome: ").upper().replace(' ', '')
flag_palindrome = True

for i in range(0,len(check_palindrome) // 2 ):
    if check_palindrome[i] != check_palindrome[len(check_palindrome) - 1 - i]:
        flag_palindrome = False
        break
else:
    if len(check_palindrome) == 0:
        flag_palindrome = False

if flag_palindrome == True:
    print("It's a palindrome")
else:
    print("It's not a palindrome")