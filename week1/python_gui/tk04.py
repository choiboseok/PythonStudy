from tkinter import *
from PIL import Image, ImageTk
#pip install pillow

app = Tk()
canvas = Canvas(app, width=400, height=300)
canvas.pack()
x = 20
y = 20
tk_tiger = None
def create_img(canvas):
    global tk_tiger # 전역변수 사용
    img = Image.open('tiger.png')
    img = img.resize((50, 50)) # 사이즈 조정
    tk_tiger = ImageTk.PhotoImage(img)
    canvas.create_image(100, 250, image=tk_tiger, tag='tiger')

def move_right(event):
    canvas.move('tiger', x, 0)
    canvas.after(10)
    canvas.update()
def move_left(event):
    canvas.move('tiger', -x, 0)
    canvas.after(10)
    canvas.update()
def move_up(event):
    canvas.move('tiger', 0, -y)
    canvas.after(10)
    canvas.update()
def move_down(event):
    canvas.move('tiger', 0, y)
    canvas.after(10)
    canvas.update()
def move_space(event):
    for i in range(5) :
        canvas.move('tiger', 0, -y)
        canvas.after(30)
        canvas.update()
    for i in range(5) :
        canvas.move('tiger', 0, y)
        canvas.after(10)
        canvas.update()

# 100, 150 왼쪽 상단 모서리  150, 200 오른쪽 상단 모서리
# canvas.create_oval(100, 150, 150, 200, fill='red', tag = 'redball') # 50x50 크기 원
create_img(canvas)
canvas.bind('<Right>', move_right)
canvas.bind('<Left>', move_left)
canvas.bind('<Up>', move_up)
canvas.bind('<Down>', move_down)
canvas.bind('<space>', move_space)
canvas.focus_set()
app.mainloop()