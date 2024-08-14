def mysplit(strng):
    mysplitlist = []
    tmpch = ""
    for ch in strng:
        if ch != " ":
            tmpch += ch
        else:
            if tmpch != "":
                mysplitlist.append(tmpch)
            tmpch = ""
    else:
        if len(tmpch) != 0:
            mysplitlist.append(tmpch)
    return mysplitlist

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
