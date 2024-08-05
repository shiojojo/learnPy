blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height = 1
while blocks:
    if blocks - height >= 0:
        blocks -= height
        height += 1
    else:
        break

height -= 1

print("The height of the pyramid:", height)
