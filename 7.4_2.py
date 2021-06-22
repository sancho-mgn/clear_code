'''было'''
def TreeOfLife(H, W, N, tree):
    age = 0
    tree_num = []
    # преобразуем входящий список строк в список списков и заменяем . и + на 0 и 1
    for br in tree:
        tmp = []
        br = br.replace('.', '0')
        br = br.replace('+', '1')
        for el in br:
            tmp.append(int(el))
        tree_num.append(tmp)

    # заходим в цикл для старения или уничтожения дерева
    while age != N:
        age += 1

        # старение
        for br in tree_num:
            for el in range(len(br)):
                br[el] += 1

        # kill
        if age % 2 == 0:
            for i in range(H):
                brunch = tree_num[i]
                for j in range(W):
                    elem = brunch[j]
                    if elem >= 3:
                        try:
                            brunch[j] = 0
                            el_1 = brunch[j - 1]
                            el_2 = brunch[j + 1]
                            el_3 = tree_num[i - 1][j]
                            el_4 = tree_num[i + 1][j]
                            if j - 1 >= 0 and el_1 < 3:
                                el_1 = 0
                            if j + 1 <= W and el_2 < 3:
                                el_2 = 0
                            if j - 1 >= 0 and el_3 < 3:
                                el_3 = 0
                            if j + 1 <= H and el_4 < 3:
                                el_4 = 0
                        except IndexError:
                            pass
    tr = []
    for i in tree_num:
        brunch = ''
        for j in i:
            if j == 0:
                brunch += '.'
            else:
                brunch += '+'
        tr.append(brunch)
    return tr
'''стало'''
def TreeOfLife(H, W, N, tree):
    age = 0
    tree_num = []
    # преобразуем входящий список строк в список списков и заменяем . и + на 0 и 1
    for br in tree:
        new_tree_num = []
        br = br.replace('.', '0')
        br = br.replace('+', '1')
        for el in br:
            new_tree_num.append(int(el))
        tree_num.append(new_tree_num)

    # заходим в цикл для старения или уничтожения дерева
    while age != N:
        age += 1

        # старение
        for br in tree_num:
            for el in range(len(br)):
                br[el] += 1

        # kill
        if age % 2 == 0:
            for i in range(H):
                brunch = tree_num[i]
                for j in range(W):
                    elem = brunch[j]
                    if elem >= 3:
                        try:
                            brunch[j] = 0
                            left_el = brunch[j - 1]
                            right_el = brunch[j + 1]
                            up_el = tree_num[i - 1][j]
                            down_el = tree_num[i + 1][j]
                            if j - 1 >= 0 and left_el < 3:
                                left_el = 0
                            if j + 1 <= W and right_el < 3:
                                right_el = 0
                            if j - 1 >= 0 and up_el < 3:
                                up_el = 0
                            if j + 1 <= H and down_el < 3:
                                down_el = 0
                        except IndexError:
                            pass
    result_tree = []
    for i in tree_num:
        brunch = ''
        for j in i:
            if j == 0:
                brunch += '.'
            else:
                brunch += '+'
        result_tree.append(brunch)
    return result_tree
