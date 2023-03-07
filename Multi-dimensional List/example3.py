mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

N = len(mat)

M = len(mat[0])

bag = ""
for i in range(N):
    for j in range(M):
        bag += str(mat[i][j]) + " "
print(bag)
