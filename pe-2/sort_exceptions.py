def print_exception_tree(thisclass, nest = 0):
    lst = []
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        lst.append([subclass.__name__,subclass])
        lst.sort()
    for i in range(len(lst)):    
        print_exception_tree(lst[i][1], nest + 1)


print_exception_tree(BaseException)
