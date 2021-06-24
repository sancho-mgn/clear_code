'''было'''
def generate_parentheses(out, open_parenthes, close_parenthes, N, result):
    if open_parenthes == N and close_parenthes == N:
        result.append(out)
    else:
        if open_parenthes < N:
            generate_parentheses(out + '(', open_parenthes + 1, close_parenthes, N, result)
        if close_parenthes < open_parenthes:
            generate_parentheses(out + ')', open_parenthes, close_parenthes + 1, N, result)
    return result

def BalancedParentheses(N):
    return ' '.join(generate_parentheses('', 0, 0, N, []))


'''стало'''
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