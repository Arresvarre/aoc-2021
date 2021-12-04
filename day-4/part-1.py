with open("input.txt", "r") as f:
    a = f.read().splitlines()
numbers = a[0].split(",")
a.pop(0)
a.pop(0)
a.append("")
print(a)
arr = ['27 21 17 24  4', '10 27 15  9 19', '21  9 27 16  7', ' 22 11 13  27  5', '  2  0 12  3  27']


def hor_ver(data):
    count = 0
    for i in data:
        for i2 in i:
            if i2 is True:
                count += 1
        if count == 5:
            return True
        count = 0
    arrcount = [0, 0, 0, 0, 0]
    index = 0
    for i in data:
        for i2 in i:
            if i2 is True:
                arrcount[index] += 1
            index += 1
        index = 0
    for i in arrcount:
        if i == 5:
            return True
    return False



class board():
    playingboard = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]]

    def __init__(self, data):
        index = 0
        index2 = 0
        for i in data:
            for i2 in i.split(" "):
                if i2:
                    self.playingboard[index2][index] = i2
                    index += 1
            index = 0
            index2 += 1

    def get_board(self):
        str=""
        for i in self.playingboard:
            for i2 in i:
                str += f"{i2} "
            print(str)
            str = ""



    def check(self, numbers):
        pb = self.playingboard
        index = 0
        index2 = 0
        number_count = 0
        for i in numbers:
            number_count += 1
            for i2 in pb:
                for i3 in i2:
                    if i == i3:
                        pb[index][index2] = True
                    index2 += 1

                    if hor_ver(pb):
                        #print(i, number_count)
                        return number_count
                index2 = 0
                index += 1
            index = 0
        return 26
arrboard = []
bestboard = board(arr)
print(bestboard.check(numbers))
for i in a:
    if i:
        arrboard.append(i)
    else:
        new_b = board(arrboard).check(numbers)
        print(new_b, bestboard.check(numbers))
        if new_b <= bestboard.check(numbers):
            bestboard = board(arrboard)
            arrboard=[]
        else:
            arrboard = []

print(board(arr).check(numbers))