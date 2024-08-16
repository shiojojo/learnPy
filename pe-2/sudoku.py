def check_sudoku(sudoku_lists):

    for i in range(0,len(sudoku_lists)):
        total_row = 0
        total_colum = 0
        for j in range(0,len(sudoku_lists)):
            total_row += sudoku_lists[i][j]
            total_colum += sudoku_lists[j][i]
        if total_row != 45 or total_colum != 45: 
            return "No"
 
    sub_square = []
    for i in range(0,7,3): 
        total = 0
        for j in range(1,10):
            for value in sudoku_lists[j - 1][i: i + 3]:
                total += value
            if j % 3 == 0:
                if total != 45:
                    return "No"
                total = 0
    return "Yes"

sudoku_lists = []
i = 0
print("input numbers")
while i < 9:
    tmp_list = []
    for ch in input():
        if int(ch) > 0:
            tmp_list.append(int(ch))
    sudoku_lists.append(tmp_list)
    i += 1

print(check_sudoku(sudoku_lists))
