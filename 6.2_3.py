def Keymaker(number_keys):
    list_of_keys = [0 for _ in range(number_keys)]
    for i in range(number_keys):
        for j in range(number_keys):
            if j % (i + 1) == i:
                    if list_of_keys[j] == 0:
                        list_of_keys[j] = 1
                    else:
                        list_of_keys[j] = 0
    return ''.join(str(i) for i in list_of_keys)

print(Keymaker(100))