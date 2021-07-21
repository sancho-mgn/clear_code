1. Example
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
            # проверяем что сл. эл. пробел иначе отходим
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

2. Example
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