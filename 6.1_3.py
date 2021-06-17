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