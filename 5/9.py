"""было"""
def MatrixTurn(matrix, M, N, T):
    global Matrix
    for shift_its_axis in range(len(matrix)):
        matrix[shift_its_axis] = list(matrix[shift_its_axis])

    if M <= N:
        num_circle = M // 2
    else:
        num_circle = N // 2

    for step in range(T): # количество сдвигов
        tmp = []
        for shift_its_axis in range(num_circle): # количество кругов во круг своей оси
            tmp.append(matrix[shift_its_axis + 1][shift_its_axis])
        for shift_its_axis in range(num_circle):
            horizont_iter = N - shift_its_axis * 2 - 1
            vertic_iter = M - shift_its_axis * 2 - 1
            horizont_iter_circle = N - shift_its_axis - 1
            vertic_iter_circle = M - shift_its_axis - 1

            for a in range(shift_its_axis, horizont_iter + shift_its_axis):
                matrix[shift_its_axis][a], tmp[shift_its_axis] = tmp[shift_its_axis], matrix[shift_its_axis][a]
            for b in range(shift_its_axis, vertic_iter + shift_its_axis):
                matrix[b][horizont_iter_circle], tmp[shift_its_axis] = tmp[shift_its_axis], matrix[b][horizont_iter_circle]
            for c in range(shift_its_axis, horizont_iter + shift_its_axis)[::-1]:
                matrix[vertic_iter_circle][c + 1], tmp[shift_its_axis] = tmp[shift_its_axis], matrix[vertic_iter_circle][c + 1]
            for d in range(shift_its_axis, vertic_iter + shift_its_axis)[::-1]:
                matrix[d + 1][shift_its_axis], tmp[shift_its_axis] = tmp[shift_its_axis], matrix[d + 1][shift_its_axis]

    for j in range(len(matrix)):
        matrix[j] = ''.join(matrix[j])

    Matrix = matrix
    return Matrix

x = MatrixTurn(['123456','234567','345678','456789'], 4,6,1)
print(x)
y = MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 3)
print(y)



"""стало"""
def MatrixTurn(matrix, M, N, T):
    global Matrix
    for shift_its_axis in range(len(matrix)):
        matrix[shift_its_axis] = list(matrix[shift_its_axis])

    if M <= N:
        circle_sum = M // 2
    else:
        circle_sum = N // 2

    for step in range(T): # количество сдвигов
        matrix_cnt_circle = []
        for shift_its_axis in range(circle_sum): # количество кругов во круг своей оси
            matrix_cnt_circle.append(matrix[shift_its_axis + 1][shift_its_axis])
        for shift_its_axis in range(circle_sum):
            horizont_iter = N - shift_its_axis * 2 - 1
            vertic_iter = M - shift_its_axis * 2 - 1
            horizont_iter_circle = N - shift_its_axis - 1
            vertic_iter_circle = M - shift_its_axis - 1

            for a in range(shift_its_axis, horizont_iter + shift_its_axis):
                matrix[shift_its_axis][a], matrix_cnt_circle[shift_its_axis] = matrix_cnt_circle[shift_its_axis], matrix[shift_its_axis][a]
            for b in range(shift_its_axis, vertic_iter + shift_its_axis):
                matrix[b][horizont_iter_circle], matrix_cnt_circle[shift_its_axis] = matrix_cnt_circle[shift_its_axis], matrix[b][horizont_iter_circle]
            for c in range(shift_its_axis, horizont_iter + shift_its_axis)[::-1]:
                matrix[vertic_iter_circle][c + 1], matrix_cnt_circle[shift_its_axis] = matrix_cnt_circle[shift_its_axis], matrix[vertic_iter_circle][c + 1]
            for d in range(shift_its_axis, vertic_iter + shift_its_axis)[::-1]:
                matrix[d + 1][shift_its_axis], matrix_cnt_circle[shift_its_axis] = matrix_cnt_circle[shift_its_axis], matrix[d + 1][shift_its_axis]

    for j in range(len(matrix)):
        matrix[j] = ''.join(matrix[j])

    Matrix = matrix
    return Matrix

x = MatrixTurn(['123456','234567','345678','456789'], 4,6,1)
print(x)
y = MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 3)
print(y)

