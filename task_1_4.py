def palindrom(strr):
    for i in range(len(strr)//2):
        j = -i - 1
        if strr[i] == strr[j]:
            if abs(i - j) == 1 or i == j:
                print('Это палиндром!')
            else:
                pass
        else:
            print('Это не палиндром!')
            break
