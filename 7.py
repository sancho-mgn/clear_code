"""было"""
def LineAnalysis(char_line):
    num_of_dots = char_line.count('.')
    num_of_star = char_line.count('*')

    if num_of_dots == 0 or num_of_star == 2:
        return True

    main_dots = 0

    for i in range(1, len(char_line)):
        if char_line[i] == '*':
            break
        main_dots += 1
    return main_dots * (num_of_star - 1) == num_of_dots

"""стало"""
def LineAnalysis(chars_of_line):
    num_of_dots = chars_of_line.count('.')
    num_of_star = chars_of_line.count('*')

    if num_of_dots == 0 or num_of_star == 2:
        return True

    main_dots = 0

    for i in range(1, len(chars_of_line)):
        if chars_of_line[i] == '*':
            break
        main_dots += 1
    return main_dots * (num_of_star - 1) == num_of_dots