from tkinter import *
import random


# 캔버스 생성이후

# 1. 기본 원그리기
# cx = 1000//2
# cy = 1000//2
# r = 400
# canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=2, outline='red')

# 전역변수
count = 0
wSize = 1000
radius = 400
colors = ['red', 'green', 'blue', 'black', 'orange', 'indigo', 'violet']

# 2. 프랙탈 원그리기 재귀함수 선언
def drawCircle(x,y,r):
    global count
    count += 1
    canvas.create_oval(x-r, y-r, x+r, y+r, width=2, outline=random.choice(colors))

    if r > 5:    
        drawCircle(x-r//2, y, r//2) # 중심의 왼쪽을 계속 그려감(재귀호출)
        drawCircle(x+r//2, y, r//2) # 중심의 오른쪽을 계속 그려감


root = Tk()
root.title('원 모양 프랙탈')
canvas = Canvas(root, width=1000, height=1000, bg=('white'))

drawCircle(wSize//2, wSize//2, radius)

canvas.pack()
root.mainloop()