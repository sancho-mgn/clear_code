"""было"""
def Sort_One_Pemutation(lst, len_lst):
    sort_command_lst = sorted(lst)
    for i in range(len_lst):
        for j in range(i + 1, len_lst):
            lst[i], lst[j] = lst[j], lst[i]
            if lst == sort_command_lst:
                return True
            else:
                lst[i], lst[j] = lst[j], lst[i]
    return False

def Sort_Reverse(lst, len_lst):
    sort_command_lst = sorted(lst)
    sort_reverse_com_lst = lst[::-1]
    for i in range(1, len_lst):
        for j in range(2 + i, len_lst + 1):
            batch = lst[:i] + lst[i:j][::-1] + lst[j:len_lst]
            sort_reverse_com_lst.append(batch)

    return sort_command_lst == sort_reverse_com_lst

def Football(F, N):
    return Sort_One_Pemutation(F, N) or Sort_Reverse(F, N)

"""стало"""
def Sort_One_Pemutation(list_of_player, len_list_of_player):
    sort_command_lst = sorted(list_of_player)
    for i in range(len_list_of_player):
        for j in range(i + 1, len_list_of_player):
            list_of_player[i], list_of_player[j] = list_of_player[j], list_of_player[i]
            if list_of_player == sort_command_lst:
                return True
            else:
                list_of_player[i], list_of_player[j] = list_of_player[j], list_of_player[i]
    return False

def Sort_Reverse(list_of_player, len_list_of_player):
    sort_command_lst = sorted(list_of_player)
    sort_reverse_com_lst = list_of_player[::-1]
    for i in range(1, len_list_of_player):
        for j in range(2 + i, len_list_of_player + 1):
            batch_of_player = list_of_player[:i] + list_of_player[i:j][::-1] + list_of_player[j:len_list_of_player]
            sort_reverse_com_lst.append(batch_of_player)

    return sort_command_lst == sort_reverse_com_lst

def Football(F, N):
    return Sort_One_Pemutation(F, N) or Sort_Reverse(F, N)