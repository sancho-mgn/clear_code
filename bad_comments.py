1. было
from os import environ
def Keymaker(keys_sum):
    # создаём список размером параметра функции заполненный
    list_of_keys = [0 for _ in range(keys_sum)]
    for i in range(keys_sum):
       for j in range(keys_sum):
            if j % (i + 1) == i:
                    if list_of_keys[j] == 0:
                        list_of_keys[j] = 1
#                    else:
#                       list_of_keys[j] = 0
    return ''.join(str(i) for i in list_of_keys)

# read value from environments
if os.environ.exists(KEY_SUM):
    # calc sum keys
    key_sum = environ[KEY_SUM]
else:
    # print result
    print('This is environ doesn't have')

print(Keymaker(key_sum))

1. стало
from os import environ
def Keymaker(keys_sum):
    # создаём список размером параметра функции заполненный
    list_of_keys = [0 for _ in range(keys_sum)]
    for i in range(keys_sum):
       for j in range(keys_sum):
            if j % (i + 1) == i:
                    if list_of_keys[j] == 0:
                        list_of_keys[j] = 1
		    # Удалил излишние комментарии, удалив не нужный код
    return ''.join(str(i) for i in list_of_keys)

# Удалил излишние комментарии
if os.environ.exists(KEY_SUM):
    # Удалил излишние комментарии
    key_sum = environ[KEY_SUM]
else:
    # Удалил излишние комментарии
    print('This is environ doesn't have')

print(Keymaker(key_sum)

2. было
def MatrixTurn(matrix, M, N, T):
    global Matrix # глобальная переменная для всей области видимости
    #GOTO в дальнешем нужно будет переделать
    for shift_its_axis in range(len(matrix)):
	# назначаем элементу списка другой список
        matrix[shift_its_axis] = list(matrix[shift_its_axis])
	
    if M <= N: # проверяем какая переменная больше
        circle_sum = M // 2
    else:
        circle_sum = N // 2

    # вычисляем количество сдвигов
    for step in range(T): 
        matrix_cnt_circle = []
 	# вычисляем количество кругов во круг своей оси
        for shift_its_axis in range(circle_sum):
            matrix_cnt_circle.append(matrix[shift_its_axis + 1][shift_its_axis])
	# закончился первый цикл, далее начнется цикл по диагоналям и горизонталям
        for shift_its_axis in range(circle_sum):
            horizont_iter = N - shift_its_axis * 2 - 1
            vertic_iter = M - shift_its_axis * 2 - 1
            horizont_iter_circle = N - shift_its_axis - 1
            vertic_iter_circle = M - shift_its_axis - 1
	    # вычисляем шаги по горизонтали справа
            for a in range(shift_its_axis, horizont_iter + shift_its_axis):
                matrix[shift_its_axis][a], matrix_cnt_circle[shift_its_axis] = matrix_cnt_circle[shift_its_axis], matrix[shift_its_axis][a] # закончился цикл по горизонтали
	    # вычисляем шаги по вертикали справа
            for b in range(shift_its_axis, vertic_iter + shift_its_axis):
                matrix[b][horizont_iter_circle], matrix_cnt_circle[shift_its_axis] = matrix_cnt_circle[shift_its_axis], matrix[b][horizont_iter_circle] # закончился цикл по вертикали
	    # вычисляем шаги по горизонтали слева
            for c in range(shift_its_axis, horizont_iter + shift_its_axis)[::-1]:
                matrix[vertic_iter_circle][c + 1], matrix_cnt_circle[shift_its_axis] = matrix_cnt_circle[shift_its_axis], matrix[vertic_iter_circle][c + 1] # закончился цикл по горизонтали в обратном порядке
	    # вычисляем шаги по вертикали слева
            for d in range(shift_its_axis, vertic_iter + shift_its_axis)[::-1]:
                matrix[d + 1][shift_its_axis], matrix_cnt_circle[shift_its_axis] = matrix_cnt_circle[shift_its_axis], matrix[d + 1][shift_its_axis] # закончился цил по вертикали в обратном порядке

    for j in range(len(matrix)):
        matrix[j] = ''.join(matrix[j])
    
    Matrix = matrix # переназначаем переменную локальную для глобальной
    return Matrix

# считывам переменные из кофигурационного файла
with open('config_file.txt') as config:
    values_list = filter(str.strip, config) # очищаем строки
    values_list = list(map(int, values_list))
if len(values_list) >= 4:
    matrix, M, N, *T = values_list

print(MatrixTurn(matrix, M, N, T))

2. стало 
def MatrixTurn(matrix, M, N, T):
    global Matrix
    #GOTO в дальнешем нужно будет переделать
    for shift_its_axis in range(len(matrix)):
        matrix[shift_its_axis] = list(matrix[shift_its_axis])

    if M <= N:
        circle_sum = M // 2
    else:
        circle_sum = N // 2

    # вычисляем количество сдвигов
    for step in range(T): 
        matrix_cnt_circle = []
 	# вычисляем количество кругов во круг своей оси
        for shift_its_axis in range(circle_sum):
            matrix_cnt_circle.append(matrix[shift_its_axis + 1][shift_its_axis])
        for shift_its_axis in range(circle_sum):
            horizont_iter = N - shift_its_axis * 2 - 1
            vertic_iter = M - shift_its_axis * 2 - 1
            horizont_iter_circle = N - shift_its_axis - 1
            vertic_iter_circle = M - shift_its_axis - 1
	    # вычисляем шаги по горизонтали справа
            for a in range(shift_its_axis, horizont_iter + shift_its_axis):
                matrix[shift_its_axis][a], matrix_cnt_circle[shift_its_axis] = matrix_cnt_circle[shift_its_axis], matrix[shift_its_axis][a]
	    # вычисляем шаги по вертикали справа
            for b in range(shift_its_axis, vertic_iter + shift_its_axis):
                matrix[b][horizont_iter_circle], matrix_cnt_circle[shift_its_axis] = matrix_cnt_circle[shift_its_axis], matrix[b][horizont_iter_circle]
	    # вычисляем шаги по горизонтали слева
            for c in range(shift_its_axis, horizont_iter + shift_its_axis)[::-1]:
                matrix[vertic_iter_circle][c + 1], matrix_cnt_circle[shift_its_axis] = matrix_cnt_circle[shift_its_axis], matrix[vertic_iter_circle][c + 1]
	    # вычисляем шаги по вертикали слева
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


3. было
from typing import Final
def PrintingCosts(string_of_chars_to_print):
    # объявляем словарь с символами и стоимостью печати как константу, добавляем тип typing.final чтобы анализатор смог обнаружить замену значения
    DICT_PRINT_COSTS: Final = {' ': 0, '!': 9, '"': 6, '#': 24, '$': 29, '%': 22, '&': 24, '\'': 3, '(': 12, ')': 12, '*': 17, '+': 13, ',': 7, '-': 7, '.': 4, '/': 10, '0': 22, '1': 19, '2': 22, '3': 23, '4': 21, '5': 27, '6': 26, '7': 16, '8': 23, '9': 26, ':': 8, ';': 11, '<': 10, '=': 14, '>': 10, '?': 15, '@': 32, 'A': 24, 'B': 29, 'C': 20, 'D': 26, 'E': 26, 'F': 20, 'G': 25, 'H': 25, 'I': 18, 'J': 18, 'K': 21, 'L': 16, 'M': 28, 'N': 25, 'O': 26, 'P': 23, 'Q': 31, 'R': 28, 'S': 25, 'T': 16, 'U': 23, 'V': 19, 'W': 26, 'X': 18, 'Y': 14, 'Z': 22, '[': 18, '\\': 10, ']': 18, '^': 7, '_': 8, '`': 3, 'a': 23, 'b': 25, 'c': 17, 'd': 25, 'e': 23, 'f': 18, 'g': 30, 'h': 21, 'i': 15, 'j': 20, 'keys_sum': 21, 'l': 16, 'm': 22, 'n': 18, 'o': 20, 'p': 25, 'q': 25, 'r': 13, 's': 21, 't': 17, 'u': 17, 'v': 13, 'w': 19, 'x': 13, 'y': 24, 'z': 19, '{': 18, '|': 12, '}': 18, '~': 9}
    print_costs = 0 # назначаем начальную стоимость печати
    for i in string_of_chars_to_print:
        if i in DICT_PRINT_COSTS:
            print_costs += DICT_PRINT_COSTS[i] # суммируем значение печати
        else:
            print_costs += 23
    return print_costs # возвращаем вычеленное значение



3. стало 
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

4. было
from typing import Final
def splitter_to_words(string, len_splitter):
    '''Функция нарезает слова на слайсы элемента  + пробел'''
    WORD_LIST: Final = string.split()
    lst_words = list() # назначаем переменной пустой список
    for i in WORD_LIST:
        while len(i) > len_splitter: # входим во вложенный цикл while
            lst_words.append(i[0:len_splitter])
            i = i[len_splitter:]
        lst_words.append(i + ' ') # добавляем результирующий i
    return lst_words


def align_lines(splitter_to_words, len_splitter):
    '''Функция выравнивает элементы согласно уканному срезу'''
    result = []
    # сохраняем первый элемент слайса строки
    line = splitter_to_words[0]
    # проверяем переменной splitter_to_words и последнего элемента line
    if len(splitter_to_words) == 1 and len(line[:-1]) <= len_splitter:
        result.append(line[:-1]) # формируем result
        return result
    lst = splitter_to_words[1:]
    for i in range(len(lst)):
        # проверяем что предыдущий эл + текущий эл были не длинее заданного отрезка
        if len(line + lst[i][
                      :-1]) <= len_splitter:  
            line += lst[i]
            continue
        else:
            # проверяем что посл. эл. пробел иначе отходим
            if line[-1] == ' ':  
                line = line[:-1]
            result.append(line)
            line = lst[i]
            if i == len(lst) - 1:
                if line[-1] == ' ':
                    line = line[:-1]
                result.append(line)
    return result

def WordSearch(lenn, s, subs):
    # сначала нарезаем на слайсы а далее выравниваем элементы согласно указанному срезу
    text = align_lines(splitter_to_words(s, lenn), lenn)
    result = [0]*len(text) # заполняем result нулями нужно размера
    for i in range(len(text)):
        if subs in text[i].split():
            result[i] = 1
    return result




4. стало
from typing import Final
def splitter_to_words(string, len_splitter):
    '''Функция нарезает слова на слайсы элемента  + пробел'''
    WORD_LIST: Final = string.split()
    lst_words = list()
    for i in WORD_LIST:
        while len(i) > len_splitter:
            lst_words.append(i[0:len_splitter])
            i = i[len_splitter:]
        lst_words.append(i + ' ')
    return lst_words


def align_lines(splitter_to_words, len_splitter):
    '''Функция выравнивает элементы согласно уканному срезу'''
    result = []
    # сохраняем первый элемент слайса строки
    line = splitter_to_words[0]
    if len(splitter_to_words) == 1 and len(line[:-1]) <= len_splitter:
        result.append(line[:-1])
        return result
    lst = splitter_to_words[1:]
    for i in range(len(lst)):
        # проверяем что предыдущий эл + текущий эл были не длинее заданного отрезка
        if len(line + lst[i][
                      :-1]) <= len_splitter:  
            line += lst[i]
            continue
        else:
            # проверяем что посл. эл. пробел иначе отходим
            if line[-1] == ' ':  
                line = line[:-1]
            result.append(line)
            line = lst[i]
            if i == len(lst) - 1:
                if line[-1] == ' ':
                    line = line[:-1]
                result.append(line)
    return result

def WordSearch(lenn, s, subs):
    # сначала нарезаем на слайсы а далее выравниваем элементы согласно указанному срезу
    text = align_lines(splitter_to_words(s, lenn), lenn)
    result = [0]*len(text)
    for i in range(len(text)):
        if subs in text[i].split():
            result[i] = 1
    return result