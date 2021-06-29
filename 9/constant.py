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

from typing import Final
def squirrel(n):
    # объявляем переменную как константу, добавляем тип typing.final чтобы анализатор смог обнаружить замену значения
    FACT_SQUARE: Final = 1
    for i in range(1, n + 1):
        FACT_SQUARE *= i
    return int(str(FACT_SQUARE)[0])
print(squirrel(7))


from typing import Final
def str_slice(s):
    # объявляем переменные как константу, добавляем тип typing.final чтобы анализатор смог обнаружить замену значения
    # calc count columns and lines
    NUM_OF_ROWS_AND_COLUMNS: Final = int((len(s) ** 0.5) * 10) / 10
    NUMBER_OF_ROWS: Final = int(NUM_OF_ROWS_AND_COLUMNS // 1) # берём нижнюю границу, количество строк
    NUMBER_OF_COLUMNS: Final= int(NUM_OF_ROWS_AND_COLUMNS % 1 * 10) # берём верхнюю границу, количество столбцов
    if NUMBER_OF_COLUMNS * NUMBER_OF_ROWS < len(s):
        NUMBER_OF_ROWS += 1
        # cut the string into slices and save them to the list
        list_s = [s[i:i + NUMBER_OF_ROWS] for i in range(0, len(s), NUMBER_OF_ROWS)]
        list_s = [iter(it) for it in list_s]
        return list_s
    else:
        list_s = [s[i:i + NUMBER_OF_ROWS] for i in range(0, len(s), NUMBER_OF_ROWS)]
        list_s = [iter(it) for it in list_s]
        return list_s

from typing import Final
def con_to_dec(REVERSE_DATA_LIST, notation):
    res = 0
    # объявляем переменную как константу, добавляем тип typing.final чтобы анализатор смог обнаружить замену значения
    REVERSE_DATA_LIST: Final = str(REVERSE_DATA_LIST)[::-1]
    for i in range(len(REVERSE_DATA_LIST)):
        res += int(REVERSE_DATA_LIST[i]) * notation ** i
    return res
    
    
from typing import Final
def Unmanned(L, N, track):
    total_dist = L
    red_add_time = 0
    for i in range(N):
        travel_time, time_red, time_green = [item for item in track[i]]
        # объявляем переменные как константу, добавляем тип typing.final чтобы анализатор смог обнаружить замену значения
        WAIT_OF_TIME_SUM: Final = travel_time + red_add_time # общее время в пути вместе с простоем на красном свете
        TRAFFIC_LIGHT_SUM: Final = time_red + time_green # общее время работы светофора

        if TRAFFIC_LIGHT_SUM and L > travel_time: # проверяем что время работы светофора не ноль, и что до светофора мы доедем
             cur_time_lights = WAIT_OF_TIME_SUM % TRAFFIC_LIGHT_SUM # проверяем попадаем ли мы под светофор, с учётом пройденных ранее светофоров
             if cur_time_lights < time_red:
                 red_add_time += time_red - cur_time_lights # вычисляем общее время простоя на красном свете светофоров
    total_dist += red_add_time
    return total_dist

from typing import Final
def splitter_to_words(string, len_splitter):
    '''Функция нарезает слова на слайсы элемента  + пробел'''
    # объявляем переменные как константу, добавляем тип typing.final чтобы анализатор смог обнаружить замену значения
    WORD_LIST: Final = string.split()
    lst_words = list()
    for i in WORD_LIST:
        while len(i) > len_splitter:
            lst_words.append(i[0:len_splitter])
            i = i[len_splitter:]
        lst_words.append(i + ' ')
    return lst_words