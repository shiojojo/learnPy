
caesar_plain = ""
shift = 0
caesar_cipher = ""


caesar_plain = input("Your String: ")
while True:
    shift = int(input("Shift String: "))
    if 1 <= shift and shift <= 25:
        break
    else:
        print("you shuold 1 ~ 25")

for ch in caesar_plain:
    cipher_codepoint = 0
    codepoint = ord(ch)
    if ord("a") <= codepoint and codepoint <= ord("z"):
        cipher_codepoint = codepoint + shift
        if cipher_codepoint > ord("z"):
            cipher_codepoint = (cipher_codepoint % ord("z")) + ord("a") -1
        cipher_ch = chr(cipher_codepoint)
    elif ord("A") <= codepoint and codepoint <= ord("Z"):
        cipher_codepoint = codepoint + shift
        if cipher_codepoint > ord("Z"):
            cipher_codepoint = (cipher_codepoint % ord("Z")) + ord("A") - 1
        cipher_ch = chr(cipher_codepoint)
    else:
        cipher_ch = ch
    caesar_cipher += cipher_ch
    
print(caesar_cipher)
