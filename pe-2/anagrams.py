anagrams_check = True
anagrams_first = sorted(input("first: ").upper().replace(" ",""))
anagrams_secound = sorted(input("secound: ").upper().replace(" ",""))

if len(anagrams_first) != len(anagrams_secound) or len(anagrams_first) == 0:
    anagrams_check = False
else:
    for i in range(0,len(anagrams_first) - 1):
        if anagrams_first[i] != anagrams_secound[i]:
            anagrams_check = False
            break

if anagrams_check == True:
    print("Anagrams")
else:
    print("Not anagrams")


