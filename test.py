
arr = [[1, True, True, True, True], [True, 2, True, True, True], [True, True, 3, True, True], [True, True, True, 4, True], [True, True, True, 5, 4]]

def hor_ver(data):
    count = 0
    for i in data:
        for i2 in i:
            if i2 is True:
                count += 1
        if count == 5:
            return True
        count = 0
    arrcount = [0 ,0 ,0 ,0 ,0]
    index =0
    for i in data:
        for i2 in i:
            if i2 is True:
                arrcount[index] += 1
            index +=1
        index = 0
    print(arrcount)
    for i in arrcount:
        if i == 5:
            return True
    return False

print(hor_ver(arr))