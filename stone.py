import random

print("로아 돌깍기".center(32, '='))

Stone = [[0 for j in range(10)] for i in range(3)]

for i in range(3) :
        for j in range(10) :
            Stone[i][j] = '□'
            
per = 75
cnt = 30
up1 = 0
up2 = 0
down = 0
count = [0 for i in range(3)]

while (cnt != 0) :
    if per > 75 : per = 75
    elif per < 25 : per = 25
    print("확률 >> ".rjust(32, ' ')+ "%d%%" % per)

    for i in range(3) :
        for j in range(10) :
            print("%s" % Stone[i][j], end = ' ')
        print("+%d" % count[i])
        
    print("".center(32, '='))
    inp = int(input("\n돌을 깎을 위치\n0: 증가1\n1: 증가2\n2: 감소\n>> "))

    ran = random.randint(1, 100)
    if per >= ran : S = 1
    else : S = 0

    if inp == 0 and up1 < 9 :
        cnt -= 1
        while True :
            if Stone[inp][up1] != '□' : up1 += 1
            else : break
        if S == 1 :
            Stone[inp][up1] = ' O'
            count[inp] += 1
            per -= 10
        else :
            Stone[inp][up1] = ' X'
            per += 10
            
    elif inp == 1 and up2 < 9 :
        cnt -= 1
        while True :
            if Stone[inp][up2] != '□' : up2 += 1
            else : break
        if S == 1 :
            Stone[inp][up2] = ' O'
            count[inp] += 1
            per -= 10
        else :
            Stone[inp][up2] = ' X'
            per += 10
            
    elif inp == 2 and down < 9 :
        cnt -= 1
        while True :
            if Stone[inp][down] != '□' : down += 1
            else : break
        if S == 1 :
            Stone[inp][down] = ' O'
            count[inp] += 1
            per -= 10
        else :
            Stone[inp][down] = ' X'
            per += 10

    else : print("잘못된 입력".center(32, '!') + "\n")

print("\n\n최종 결과: %d %d %d 돌맹이 세공 완료" % (count[0], count[1], count[2]))
