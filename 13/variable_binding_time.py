1.
from os import environ
def Keymaker(keys_sum):
    list_of_keys = [0 for _ in range(keys_sum)]
    for i in range(keys_sum):
        for j in range(keys_sum):
            if j % (i + 1) == i:
                    if list_of_keys[j] == 0:
                        list_of_keys[j] = 1
                    else:
                        list_of_keys[j] = 0
    return ''.join(str(i) for i in list_of_keys)

# read value from environments
if os.environ.exists(KEY_SUM):
    key_sum = environ[KEY_SUM]
else:
    print('This is environ doesn't have')

print(Keymaker(key_sum))

2. 
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

# считывам переменные из кофигурационного файла
with open('config_file.txt') as config:
    values_list = filter(str.strip, config) # очищаем строки
    values_list = list(map(int, values_list))
if len(values_list) >= 4:
    matrix, M, N, *T = values_list

print(MatrixTurn(matrix, M, N, T))

3. 
from typing import Final
def PrintingCosts(string_of_chars_to_print):
    # объявляем словарь с символами и стоимостью печати как константу, добавляем тип typing.final чтобы анализатор смог обнаружить замену значения
    DICT_PRINT_COSTS: Final = {' ': 0, '!': 9, '"': 6, '#': 24, '$': 29, '%': 22, '&': 24, '\'': 3, '(': 12, ')': 12, '*': 17, '+': 13, ',': 7, '-': 7, '.': 4, '/': 10, '0': 22, '1': 19, '2': 22, '3': 23, '4': 21, '5': 27, '6': 26, '7': 16, '8': 23, '9': 26, ':': 8, ';': 11, '<': 10, '=': 14, '>': 10, '?': 15, '@': 32, 'A': 24, 'B': 29, 'C': 20, 'D': 26, 'E': 26, 'F': 20, 'G': 25, 'H': 25, 'I': 18, 'J': 18, 'K': 21, 'L': 16, 'M': 28, 'N': 25, 'O': 26, 'P': 23, 'Q': 31, 'R': 28, 'S': 25, 'T': 16, 'U': 23, 'V': 19, 'W': 26, 'X': 18, 'Y': 14, 'Z': 22, '[': 18, '\\': 10, ']': 18, '^': 7, '_': 8, '`': 3, 'a': 23, 'b': 25, 'c': 17, 'd': 25, 'e': 23, 'f': 18, 'g': 30, 'h': 21, 'i': 15, 'j': 20, 'keys_sum': 21, 'l': 16, 'm': 22, 'n': 18, 'o': 20, 'p': 25, 'q': 25, 'r': 13, 's': 21, 't': 17, 'u': 17, 'v': 13, 'w': 19, 'x': 13, 'y': 24, 'z': 19, '{': 18, '|': 12, '}': 18, '~': 9}
    print_costs = 0
    for i in string_of_chars_to_print:
        if i in DICT_PRINT_COSTS:
            print_costs += DICT_PRINT_COSTS[i]
        else:
            print_costs += 23
    return print_costs
