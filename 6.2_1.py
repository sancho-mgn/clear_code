def BiggerGreater(string):
    for i in range(len(string)-1,0,-1):
        if string[i] > string[i-1]:
            temp_list_chars = list(string[i - 1:])
            list_chars_max_of_volume = sorted(temp_list_chars)
            char_max_of_volume = list_chars_max_of_volume[list_chars_max_of_volume.index(temp_list_chars[0]) + 1]
            ind_chr_max_of_volume = temp_list_chars.index(char_max_of_volume)
            temp_list_chars[0], temp_list_chars[ind_chr_max_of_volume] = temp_list_chars[ind_chr_max_of_volume], temp_list_chars[0]
            sorted_string = string[:i-1] + ''.join(temp_list_chars[0]) + ''.join(sorted(temp_list_chars[1:]))
            return sorted_string
    sorted_string = ''
    return sorted_string