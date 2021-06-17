def isSmaller(string_one, string_two):
    len_str_one = len(string_one)
    len_str_two = len(string_two)

    if len_str_one < len_str_two:
        return True

    if len_str_one > len_str_two:
        return False

    for i in range(len_str_one):
        if string_one[i] < string_two[i]:
            return True
        elif string_one[i] > string_two[i]:
            return False

def BigMinus(s1, s2):
    if isSmaller(s1, s2):
        s1, s2 = s2, s1

    s1_bigger_reverse = [int(i) for i in s1][::-1]
    s2_bigger_reverse = [int(i) for i in s2][::-1]

    res_lst_merge_string = []
    len_small = len(s2_bigger_reverse)

    for i in range(len_small):
        if s1_bigger_reverse[i] >= s2_bigger_reverse[i]:
            res_merge_string = s1_bigger_reverse[i] - s2_bigger_reverse[i]
            res_lst_merge_string.append(res_merge_string)
        else:
            res_merge_string = s1_bigger_reverse[i] + 10 - s2_bigger_reverse[i]
            s1_bigger_reverse[i + 1] = s1_bigger_reverse[i + 1] - 1
            res_lst_merge_string.append(res_merge_string)

    for i in range(len(res_lst_merge_string)):
        s1_bigger_reverse[i] = res_lst_merge_string[i]

    s1_bigger_reverse = s1_bigger_reverse[::-1]
    return str(int(''.join([str(i) for i in s1_bigger_reverse])))