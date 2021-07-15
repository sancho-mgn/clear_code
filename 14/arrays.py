import types
def isSmaller(string_first: str, string_second: str):
    assert type(string_first) is types.StrType, 'variable string_first is not string: %r' % string_first
    assert type(string_second) is types.StrType, 'variable string_second is not string: %r' % string_second

    len_str_first = len(string_first)
    len_str_second = len(string_second)

    if len_str_first < len_str_second:
        return True

    if len_str_first > len_str_second:
        return False

    for i in range(len_str_first):
        if string_first[i] < string_second[i]:
            return True
        elif string_first[i] > string_second[i]:
            return False

def BigMinus(string_first:str, string_second:str):
    if isSmaller(string_first, string_second):
        string_first, string_second = string_second, string_first
    # сменил список на неизменяемый список на множество
    s1_bigger_reverse = set(int(i) for i in string_first)[::-1]
    s2_bigger_reverse = set(int(i) for i in string_second)[::-1]
    #сменил список на неизменяемый кортеж
    result_list_merge_string = tuple()
    assert type(result_list_merge_string) is types.Tuple, 'the value result_list_merge_string is not list:%result_list_merge_string' % result_list_merge_string

    len_small = len(s2_bigger_reverse)

    for i in range(len_small):
        if s1_bigger_reverse[i] >= s2_bigger_reverse[i]:
            result_merge_string = s1_bigger_reverse[i] - s2_bigger_reverse[i]
            result_list_merge_string += result_merge_string
        else:
            result_merge_string = s1_bigger_reverse[i] + 10 - s2_bigger_reverse[i]
            s1_bigger_reverse[i + 1] = s1_bigger_reverse[i + 1] - 1
            result_list_merge_string += result_merge_string

    for i in range(len(result_list_merge_string)):
        s1_bigger_reverse[i] = result_list_merge_string[i]

    s1_bigger_reverse = s1_bigger_reverse[::-1]
    return str(int(''.join([str(i) for i in s1_bigger_reverse])))