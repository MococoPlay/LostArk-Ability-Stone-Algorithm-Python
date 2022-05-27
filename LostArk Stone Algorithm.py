from random import randint as rint
from tkinter import *

global Per # 확률 변수
Per = 75
global Cnt # 총 몇 번의 세공을 했는지를 세는 변수
Cnt = 0
global Up1 # 첫번째 증가 옵션 변수
Up1 = 0
global Up2 # 두번째 증가 옵션 변수
Up2 = 0
global Down # 감소 옵션 변수
Down = 0

# [3][10]의 2차원 배열을 생성하여 세공의 상태를 저장
Stone = [[0 for j in range(10)] for i in range(3)]
for i in range(3) :
        for j in range(10) :
                Stone[i][j] = '□'

# 몇 번 성공 했는지 확인 하는 배열
Count = [0 for i in range(3)]

# 처음은 0으로 초기화
for i in range(3) :
        Count[i] = 0

# 첫번째 증가 옵션을 세공하는 버튼
def bt1_click(event):
        global Ran
        global Per
        global Up1
        global Cnt

        if Up1 < 9 : # 아직 세공이 덜 완료 됐을 경우
                Cnt += 1
                Ran = rint(1, 100)
                if Per >= Ran : S = 1 # Ran 함수가 Per 함수보다 높으면 성공
                else : S = 0 # 낮으면 실패
                        
                if Stone[0][Up1] != '□' : Up1 += 1 # 이전 단계가 세공을 완료 했으면 다음으로 넘어감
                if S == 1 :
                        Stone[0][Up1] = ' O'
                        Count[0] += 1
                        Per -= 10
                        if Per < 25 : Per = 25 # 확률이 25% 미만으로 떨어지지 않게 설정
                else :
                        Stone[0][Up1] = ' X'
                        Per += 10
                        if Per > 75 : Per = 75 # 확률이 75% 초과하지 않도록 설정
        for i in range(3) : # 돌의 세공 정보를 화면에 출력
                for j in range(10) :
                        stoneUI = Label(win, text=Stone[i][j])
                        stoneUI.grid(row=i+2, column=j)
                        
        Per_screen = Label(win, text=Per) # 확률 정보를 화면에 출력
        Per_screen.grid(row=1, column=11, columnspan=11)
        
        One = Label(win, text=Count[0]) # 얼마나 성공했는지 화면에 출력
        One.grid(row=2, column=11)

def bt2_click(event):
        global Ran
        global Per
        global Up2
        global Cnt

        if Up2 < 9 :
                Cnt += 1
                Ran = rint(1, 100)
                if Per >= Ran : S = 1
                else : S = 0
                        
                if Stone[1][Up2] != '□' : Up2 += 1
                if S == 1 :
                        Stone[1][Up2] = ' O'
                        Count[1] += 1
                        Per -= 10
                        if Per < 25 : Per = 25
                else :
                        Stone[1][Up2] = ' X'
                        Per += 10
                        if Per > 75 : Per = 75
        for i in range(3) :
                for j in range(10) :
                        stoneUI = Label(win, text=Stone[i][j])
                        stoneUI.grid(row=i+2, column=j)
                        
        Per_screen = Label(win, text=Per)       
        Per_screen.grid(row=1, column=11, columnspan=11)
        
        One = Label(win, text=Count[1])
        One.grid(row=3, column=11)

def bt3_click(event):
        global Ran
        global Per
        global Down
        global Cnt

        if Down < 9 :
                Cnt += 1
                Ran = rint(1, 100)
                if Per >= Ran : S = 1
                else : S = 0
                        
                if Stone[2][Down] != '□' : Down += 1
                if S == 1 :
                        Stone[2][Down] = ' O'
                        Count[2] += 1
                        Per -= 10
                        if Per < 25 : Per = 25
                else :
                        Stone[2][Down] = ' X'
                        Per += 10
                        if Per > 75 : Per = 75
        for i in range(3) :
                for j in range(10) :
                        stoneUI = Label(win, text=Stone[i][j])
                        stoneUI.grid(row=i+2, column=j)
                        
        Per_screen = Label(win, text=Per)       
        Per_screen.grid(row=1, column=11, columnspan=11)
        
        One = Label(win, text=Count[2])
        One.grid(row=4, column=11)
        
win = Tk()

# 메인 글귀를 화면에 출력
Main = Label(win, text="LostArk Ability Stone Algorithm".center(32, '　'))
Main.grid(row=0, column=0, columnspan=12)

# 초기 확률 정보를 화면에 출력
Per_screen = Label(win, text=Per)
Per_mark = Label(win, text="%")
Per_screen.grid(row=1, column=11, columnspan=11)
Per_mark.grid(row=1, column=12)

# 밑에 여백을 화면에 출력
Foot = Label(win, text="".center(34, '　'))
Foot.grid(row=5, column=0, columnspan=12)

# 첫번째 증가 옵션의 성공 횟수와 '+'기호를 화면에 출력
One_mark = Label(win, text='+')
One = Label(win, text=Count[0])

# 두번째 증가 옵션의 성공 횟수와 '+'기호를 화면에 출력
Two_mark = Label(win, text='+')
Two = Label(win, text=Count[1])

# 감소 옵션의 성공 횟수와 '+'기호를 화면에 출력
Three_mark = Label(win, text='+')
Three = Label(win, text=Count[2])

# 첫번째 증가 옵션을 세공하는 버튼을 화면에 출력
Bt1 = Button(win, text="세공")
One_mark.grid(row=2, column=9, columnspan=9)
One.grid(row=2, column=11)
Bt1.grid(row=2, column=12)
Bt1.bind("<Button-1>", bt1_click)

# 두번째 증가 옵션을 세공하는 버튼을 화면에 출력
Bt2 = Button(win, text="세공")
Two_mark.grid(row=3, column=9, columnspan=9)
Two.grid(row=3, column=11)
Bt2.grid(row=3, column=12)
Bt2.bind("<Button-1>", bt2_click)

# 감소 옵션을 세공하는 버튼을 화면에 출력
Bt3 = Button(win, text="세공")
Three_mark.grid(row=4, column=9, columnspan=9)
Three.grid(row=4, column=11)
Bt3.grid(row=4, column=12)
Bt3.bind("<Button-1>", bt3_click)

# 초기 돌의 세공 정보를 화면에 출력
for i in range(3) :
        for j in range(10) :
                stoneUI = Label(win, text=Stone[i][j])
                stoneUI.grid(row=i+2, column=j)
                
win.mainloop()
