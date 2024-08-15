def pos(hidden, finded):
    
    position = 0
    for ch in hidden:
        position = finded.find(ch, position)
        if position == -1:
            return "No"
    return "Yes"

hidden = input("First Character: ").upper()
finded = input("Second Character: ").upper()

print(pos(hidden, finded))