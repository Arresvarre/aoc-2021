def m(hh):
    with open("input.txt", "r") as f:
        a = f.read().splitlines()
    a2 = []
    for i in a:
        a2.append(list(i))

    def delete1or0(index, ggg):
        count = 0

        for i in a2:
            if i == "0":
                pass
            elif i[index] == "1":
                count += 1
            else:
                count -= 1
        if ggg:
            if count >= 0:
                return "0"
            else:
                return "1"
        else:
            if count == 0:
                return "1"
            elif count > 0:
                return "1"
            else:
                return "0"

    def delete(idx, ggg):
        _ = 0
        jk = delete1or0(idx, ggg)
        for ii in a2:
            if ii == "0":
                _ += 1
            elif ii[idx] == jk:
                a2[_] = "0"
                _ += 1
            else:
                _ += 1


    def new_list(llll):
        a3 = []
        for iii in llll:
            if type(iii) == list:
                a3.append(iii)
        return a3


    for ll in range(len(a[0])):
        delete(ll, hh)
        a2 = new_list(a2)
        if len(a2)==1:
            break

    return "".join(a2[0])

print(int(m(True), 2) * int(m(False), 2))