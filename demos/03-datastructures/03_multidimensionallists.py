grid = [
    [1, 2, 3],
    [4, 5, 6],
]
print(grid[0])  # [1, 2, 3], the first row
print(grid[1][2])  # 6, row 1, column 2
print(len(grid), len(grid[0]))  # 2 3, rows and columns

grid[0][0] = 10
print(grid)  # [[10, 2, 3], [4, 5, 6]]
grid.append([7, 8, 9])
print(grid)  # [[10, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(grid[0][3])  # IndexError: list index out of range

shared = [[0] * 3] * 2
shared[0][0] = 1
print(shared)  # [[1, 0, 0], [1, 0, 0]], both rows are one list

rows = [[0] * 3, [0] * 3]
rows[0][0] = 1
print(rows)  # [[1, 0, 0], [0, 0, 0]], two separate lists
