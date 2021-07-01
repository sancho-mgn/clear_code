"""было"""
actual_string = ''
actual_idx = 1
undo_memory = []
len_mem = len(undo_memory)

def BastShoe(char_of_string):

    global actual_string
    global undo_memory
    global actual_idx
    global len_mem

    if char_of_string == '':
        return actual_string

    try:
        count_space_in_string = char_of_string.split(' ', 1)
        ind_fst_of_space_in_str = int(count_space_in_string[0])
    except ValueError:
        return actual_string

    if len(count_space_in_string) > 1:
        chars_of_string = count_space_in_string[1]
    else:
        chars_of_string = ''

    if int(ind_fst_of_space_in_str) == 1:
        if chars_of_string == '':
            return actual_string
        else:
            App_chr(chars_of_string)

    elif int(ind_fst_of_space_in_str) == 2:
        if chars_of_string == '' or actual_string == '':
            return actual_string
        else:
            Del_chr(chars_of_string)

    elif int(ind_fst_of_space_in_str) == 3:
        if chars_of_string == '':
            return ''
        else:
            index = Return_index(chars_of_string)
            return index

    elif int(ind_fst_of_space_in_str) == 4 and chars_of_string == '':
        if len(undo_memory) == 0:
            return actual_string
        else:
            Undo_act()

    elif int(ind_fst_of_space_in_str) == 5 and chars_of_string == '':
        if len(undo_memory) == 0:
            return actual_string
        else:
            Redo_act()
    else:
        return actual_string

    return actual_string


def App_chr(S):
    global actual_string
    global undo_memory
    global actual_idx
    global len_mem

    if actual_idx != 1:
        undo_memory = undo_memory[len_mem - actual_idx:len_mem - actual_idx + 1]
        actual_idx = 1

    if len(undo_memory) == 0:
        actual_string = S
        undo_memory.append(actual_string)
    else:
        actual_string = undo_memory[-1] + S
        undo_memory.append(actual_string)

    return actual_string


def Del_chr(N):
    global actual_string
    global undo_memory
    global actual_idx
    global len_mem

    if actual_idx != 1:
        undo_memory = undo_memory[len_mem - actual_idx:len_mem - actual_idx + 1]
        actual_idx = 1

    str_len = len(actual_string)
    try:
        if int(N) >= str_len:
            actual_string = ''
        else:
            actual_string = actual_string[:str_len - int(N)]
        undo_memory.append(actual_string)

        return actual_string
    except ValueError:
        return actual_string


def Return_index(i):
    global actual_string

    try:

        if int(i) >= len(actual_string) or int(i) < 0:
            return ''
        else:
            index = actual_string[int(i)]
            return str(index)
    except ValueError:
        return ''


def Undo_act():
    global actual_string
    global undo_memory
    global actual_idx

    if actual_idx == len(undo_memory):
        actual_idx = len(undo_memory)
    else:
        actual_idx += 1
    actual_string = undo_memory[len(undo_memory) - actual_idx]

    return actual_string


def Redo_act():
    global actual_string
    global undo_memory
    global actual_idx

    if actual_idx == 1:
        actual_string = undo_memory[len(undo_memory) - actual_idx]
    else:
        actual_idx -= 1
        actual_string = undo_memory[len(undo_memory) - actual_idx]

    return actual_string
"""стало"""
actual_string = ''
actual_idx = 1
undo_memory = []
len_mem = len(undo_memory)

def BastShoe(char_of_string):

    global actual_string
    global undo_memory
    global actual_idx
    global len_mem
    #избежал сравнения
    if not char_of_string:
        return actual_string

    try:
        count_space_in_string = char_of_string.split(' ', 1)
        ind_fst_of_space_in_str = int(count_space_in_string[0])
    except ValueError:
        return actual_string

    if len(count_space_in_string) > 1:
        chars_of_string = count_space_in_string[1]
    else:
        chars_of_string = ''

    # ушёл от преобразования типов
    if ind_fst_of_space_in_str == 1:
        # избежал сравнения
        if not char_of_string:
            return actual_string
        else:
            App_chr(chars_of_string)
    # ушёл от преобразования типов
    elif ind_fst_of_space_in_str == 2:
        # избежал сравнения
        if not chars_of_string or not actual_string:
            return actual_string
        else:
            Del_chr(chars_of_string)
    # ушёл от преобразования типов
    elif ind_fst_of_space_in_str == 3:
        # избежал сравнения
        if not char_of_string:
            return ''
        else:
            index = Return_index(chars_of_string)
            return index
    # ушёл от преобразования типов
    elif ind_fst_of_space_in_str == 4 and chars_of_string == '':
        # избежал сравнения
        # ушёл от повторения операции вычисления длины строки
        if not len_mem:
            return actual_string
        else:
            Undo_act()
    # ушёл от преобразования типов
    elif ind_fst_of_space_in_str == 5 and chars_of_string == '':
        # избежал сравнения
        # ушёл от повторения операции вычисления длины строки
        if not len_mem:
            return actual_string
        else:
            Redo_act()
    else:
        return actual_string

    return actual_string


def App_chr(S):
    global actual_string
    global undo_memory
    global actual_idx
    global len_mem

    if actual_idx != 1:
        undo_memory = undo_memory[len_mem - actual_idx:len_mem - actual_idx + 1]
        actual_idx = 1
    # избежал сравнения
    # ушёл от повторения операции вычисления длины строки
    if not len_mem:
        actual_string = S
        undo_memory.append(actual_string)
    else:
        actual_string = undo_memory[-1] + S
        undo_memory.append(actual_string)

    return actual_string


def Del_chr(N):
    global actual_string
    global undo_memory
    global actual_idx
    global len_mem

    if actual_idx != 1:
        undo_memory = undo_memory[len_mem - actual_idx:len_mem - actual_idx + 1]
        actual_idx = 1

    str_len = len(actual_string)
    try:
        # ушёл от преобразования типов
        if N >= str_len:
            actual_string = ''
        else:
            actual_string = actual_string[:str_len - int(N)]
        undo_memory.append(actual_string)

        return actual_string
    except ValueError:
        return actual_string


def Return_index(i):
    global actual_string

    try:

        if int(i) >= len(actual_string) or int(i) < 0:
            return ''
        else:
            index = actual_string[int(i)]
            return str(index)
    except ValueError:
        return ''


def Undo_act():
    global actual_string
    global undo_memory
    global actual_idx
    # ушёл от повторения операции вычисления длины строки
    if actual_idx == len_mem:
        actual_idx = len_mem
    else:
        actual_idx += 1
    actual_string = undo_memory[len(undo_memory) - actual_idx]

    return actual_string


def Redo_act():
    global actual_string
    global undo_memory
    global actual_idx
    # избежал сравнения
    if actual_idx:
        # ушёл от повторения операции вычисления длины строки
        actual_string = undo_memory[len_mem - actual_idx]
    else:
        actual_idx -= 1
        # ушёл от повторения операции вычисления длины строки
        actual_string = undo_memory[len_mem - actual_idx]

    return actual_string