'''было'''
def str_slice(s):
    # calc count columns and lines
    num_of_lin_and_col = int((len(s) ** 0.5) * 10) / 10
    num_of_lin = int(num_of_lin_and_col // 1) # берём нижнюю границу, количество строк
    num_of_col = int(num_of_lin_and_col % 1 * 10) # берём верхнюю границу, количество столбцов
    if num_of_col * num_of_lin < len(s):
        num_of_lin += 1
        # cut the string into slices and save them to the list
        list_s = [s[i:i + num_of_lin] for i in range(0, len(s), num_of_lin)]
        list_s = [iter(it) for it in list_s]
        return list_s
    else:
        list_s = [s[i:i + num_of_lin] for i in range(0, len(s), num_of_lin)]
        list_s = [iter(it) for it in list_s]
        return list_s

def trans_list_of_lists(list_s):
    len_s = len(list_s)
    list_enc = []
    while len_s:
        tmp = []
        for i, v in enumerate(list_s):
            try:
                values = next(v)
            except StopIteration:
                break
            tmp.append(values)
        list_enc.append(''.join(tmp))
        len_s -= 1
    return list_enc

def TheRabbitsFoot(s, encode):
    if encode:
        # del spaces in string
        s = s.split()
        s = ''.join(s)
        list_s = str_slice(s)
        list_enc = trans_list_of_lists(list_s)
        return ' '.join(list_enc)
    else:
        s = s.split()
        res = ''
        for i in range(len(s)):
            for j in range(len(s)):
                if i < len(s[j]):
                    res += s[j][i]
        return res
'''стало'''
def str_slice(s):
    # calc count columns and lines
    num_of_lin_and_col = int((len(s) ** 0.5) * 10) / 10
    num_of_lin = int(num_of_lin_and_col // 1) # берём нижнюю границу, количество строк
    num_of_col = int(num_of_lin_and_col % 1 * 10) # берём верхнюю границу, количество столбцов
    if num_of_col * num_of_lin < len(s):
        num_of_lin += 1
        # cut the string into slices and save them to the list
        list_s = [s[i:i + num_of_lin] for i in range(0, len(s), num_of_lin)]
        list_s = [iter(it) for it in list_s]
        return list_s
    else:
        list_s = [s[i:i + num_of_lin] for i in range(0, len(s), num_of_lin)]
        list_s = [iter(it) for it in list_s]
        return list_s

def trans_list_of_lists(list_s):
    len_s = len(list_s)
    list_enc = []
    while len_s:
        values_of_string = []
        for i, v in enumerate(list_s):
            try:
                values = next(v)
            except StopIteration:
                break
            values_of_string.append(values)
        list_enc.append(''.join(values_of_string))
        len_s -= 1
    return list_enc

def TheRabbitsFoot(s, encode):
    if encode:
        # del spaces in string
        s = s.split()
        s = ''.join(s)
        list_s = str_slice(s)
        list_enc = trans_list_of_lists(list_s)
        return ' '.join(list_enc)
    else:
        s = s.split()
        res = ''
        for i in range(len(s)):
            for j in range(len(s)):
                if i < len(s[j]):
                    res += s[j][i]
        return res