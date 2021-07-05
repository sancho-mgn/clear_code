# было
def generate_parentheses(out, open_parenthes, close_parenthes, N, count_pairs_parenthes):
    if open_parenthes == N and close_parenthes == N:
        count_pairs_parenthes.append(out)
    else:
        if open_parenthes < N:
            generate_parentheses(out + '(', open_parenthes + 1, close_parenthes, N, count_pairs_parenthes)
        if close_parenthes < open_parenthes:
            generate_parentheses(out + ')', open_parenthes, close_parenthes + 1, N, count_pairs_parenthes)
    return count_pairs_parenthes

def BalancedParentheses(N):
    return ' '.join(generate_parentheses('', 0, 0, N, []))

#стало
import types
def generate_parentheses(out: str, open_parenthes: int, close_parenthes: int, N: int, count_pairs_parenthes: list):
    """
    :param out: List
    :type N: Integer, out: String, open_parenthes: Integer, close_parenthes: Integer, count_pairs_parenthes: List
    """
    assert type(open_parenthes) is types.IntType, 'the variable open_parenthes: %r must be of integer type' % open_parenthes
    assert type(close_parenthes) is types.IntType, 'the variable close_parenthes: %r must be of integer type' % close_parenthes
    assert type(N) is types.IntType, 'the variable N: %r must be of integer type' % N
    if open_parenthes == N and close_parenthes == N:
        assert type(out) is types.StringType, 'the variable out: %r must be of string type' % out
        count_pairs_parenthes.append(out)
    else:
        if open_parenthes < N:
            generate_parentheses(out + '(', open_parenthes + 1, close_parenthes, N, count_pairs_parenthes)
        if close_parenthes < open_parenthes:
            generate_parentheses(out + ')', open_parenthes, close_parenthes + 1, N, count_pairs_parenthes)
    return count_pairs_parenthes

def BalancedParentheses(N):
    return ' '.join(generate_parentheses('', 0, 0, N, []))
    
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

    s1_bigger_reverse = [int(i) for i in string_first][::-1]
    s2_bigger_reverse = [int(i) for i in string_second][::-1]

    result_list_merge_string = []
    assert type(result_list_merge_string) is types.List, 'the value result_list_merge_string is not list:%result_list_merge_string' % result_list_merge_string

    len_small = len(s2_bigger_reverse)

    for i in range(len_small):
        if s1_bigger_reverse[i] >= s2_bigger_reverse[i]:
            result_merge_string = s1_bigger_reverse[i] - s2_bigger_reverse[i]
            result_list_merge_string.append(result_merge_string)
        else:
            result_merge_string = s1_bigger_reverse[i] + 10 - s2_bigger_reverse[i]
            s1_bigger_reverse[i + 1] = s1_bigger_reverse[i + 1] - 1
            result_list_merge_string.append(result_merge_string)

    for i in range(len(result_list_merge_string)):
        s1_bigger_reverse[i] = result_list_merge_string[i]

    s1_bigger_reverse = s1_bigger_reverse[::-1]
    return str(int(''.join([str(i) for i in s1_bigger_reverse])))

import types
def Sort_One_Pemutation(list_of_player: list, len_list_of_player: int):
    assert type(list_of_player) is types.List, 'The value list_of_player is not list: %list_of_player'
    assert type(len_list_of_player) is types.IntType, 'The value len_list_of_player is not integer: %len_list_of_player'
    sort_command_lst = sorted(list_of_player)
    for i in range(len_list_of_player):
        for j in range(i + 1, len_list_of_player):
            list_of_player[i], list_of_player[j] = list_of_player[j], list_of_player[i]
            if list_of_player == sort_command_lst:
                return True
            else:
                list_of_player[i], list_of_player[j] = list_of_player[j], list_of_player[i]
    return False

def Sort_Reverse(list_of_player:list, len_list_of_player:int):
    sort_command_lst = sorted(list_of_player)
    sort_reverse_com_lst = list_of_player[::-1]
    for i in range(1, len_list_of_player):
        for j in range(2 + i, len_list_of_player + 1):
            batch_of_player = list_of_player[:i] + list_of_player[i:j][::-1] + list_of_player[j:len_list_of_player]
            sort_reverse_com_lst.append(batch_of_player)

    return sort_command_lst == sort_reverse_com_lst

def Football(F:list, N:int):
    return Sort_One_Pemutation(F, N) or Sort_Reverse(F, N)
