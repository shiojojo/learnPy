my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
my_list_tmp = my_list[:]
    
for i in range(0,len(my_list_tmp)):
    if my_list_tmp[i] in my_list_tmp[(i + 1):]:
        my_list[i] = None

while None in my_list:
    my_list.remove(None)

print("The list with unique elements only:")
print(my_list)


