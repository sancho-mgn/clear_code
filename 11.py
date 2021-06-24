"""было"""
def MisterRobot(N, data):
    chk = []
    while True:
        if data != sorted(data):
            for i in range(N - 3):
                chunk = data[i:i + 3]
                if chunk != sorted(chunk):
                    for j in range(len(chunk)):
                        chunk_sort = [chunk[j - 2], chunk[j - 1], chunk[j]]
                        if chunk_sort == sorted(chunk):
                            data[i:i + 3] = chunk_sort
                            break
            if data in chk and data != sorted(data):
                return False
            chk.append(data)
        else:
            return True

"""стало"""			
def MisterRobot(N, unsorted_data):
    sorted_data = []
    while True:
        if unsorted_data != sorted(unsorted_data):
            for i in range(N - 3):
                chunk = unsorted_data[i:i + 3]
                if chunk != sorted(chunk):
                    for j in range(len(chunk)):
                        chunk_sort = [chunk[j - 2], chunk[j - 1], chunk[j]]
                        if chunk_sort == sorted(chunk):
                            unsorted_data[i:i + 3] = chunk_sort
                            break
            if unsorted_data in sorted_data and unsorted_data != sorted(unsorted_data):
                return False
            sorted_data.append(unsorted_data)
        else:
            return True