from tkinter import *
from tkinter import messagebox as mb
from random import randrange as rnd, choice

root = Tk()
width = 1200
height = 700
root.geometry(str(width)+'x'+str(height))
main_menu = Menu(root)
root.config(menu=main_menu)
menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Меню', menu=menu)
mode = Menu(menu, tearoff=0)
canv = Canvas(root, bg='White')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']
scoreLabel = Label(text="Счет: 0, Текущий рекорд: 0", font=("Arial", 12))
scoreLabel.config(bd=0, bg='white')
scoreLabel.pack()
score = 0
life = 0
objects = []
obj_count = 0
difficulty = IntVar()
difficulty.set(0)

def new_ball():
    global obj_count
    r = rnd(30, 50)
    x = rnd(100, width - 100)
    y = rnd(100, height - 100)
    f = 0
    while f == 0 & obj_count < 10:
        f = 1
        for t in objects:
            x1 = (canv.coords(t[0])[0] + canv.coords(t[0])[2]) / 2
            y1 = (canv.coords(t[0])[1] + canv.coords(t[0])[3]) / 2
            r1 = (canv.coords(t[0])[2] - canv.coords(t[0])[0]) / 2
            if (x - x1) ** 2 + (y - y1) ** 2 < (r + r1) ** 2:
                r = rnd(30, 50)
                x = rnd(100, width - 100)
                y = rnd(100, height - 100)
                f = 0
    vx = rnd(0, 7 + 2 * score // 20) - 3 - score // 20  
    vy = rnd(0, 7 + 2 * score // 20) - 3 - score // 20
    if vx**2 + vy**2 == 0:
        vx = 1
    obj_count += 1
  
    objects.append([canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0), 0, [vx, vy]])


def click(event):
    global score, life, obj_count, high1, high2, high3
    for target in objects:
        x = (canv.coords(target[0])[0] + canv.coords(target[0])[2]) / 2 
        y = (canv.coords(target[0])[1] + canv.coords(target[0])[3]) / 2
        r = (canv.coords(target[0])[2] - canv.coords(target[0])[0]) / 2
        if (x - event.x)**2 + (y - event.y)**2 <= r*r:  
            score += 1
            if difficulty.get() == 1:
                life += obj_count
                if score > high2:
                    high2 = score
                    save = open("save.dat", 'w')
                    save.write(str(high1)+'\n')
                    save.write(str(high2)+'\n')
                    save.write(str(high3)+'\n')
                    save.close()
                scoreLabel['text'] = "Текущий счет: " + str(score) + ", Рекорд: " + str(high2)
            else:
                if score > high1:
                    high1 = score
                    save = open("save.dat", 'w')
                    save.write(str(high1)+'\n')
                    save.write(str(high2)+'\n')
                    save.write(str(high3)+'\n')
                    save.close()
                scoreLabel['text'] = "Текущий счет: " + str(score) + ", Рекорд: " + str(high1)
            canv.delete(target[0])  # then delete it
            objects.remove(target)
            obj_count -= 1

# updater
def update():
    # difficulty depends on score
    global obj_count, life
    for target in objects:
        target[1] += 1      # counting lifetime
        if target[1] > 210 - 30 * (score + 1) ** (1/3):  # this is formula for decreasing of ball's lifetime
            canv.delete(target[0])      # the ball is dead, we remove corpse
            objects.remove(target)
            obj_count -= 1
            if difficulty.get() == 1:
                life -= 1
                scoreLabel['text'] = "Текущий счет: " + str(score) + ", Рекорд: " + str(high2)
                if life <= 0:
                    mb.showinfo("Loser", "Вы проиграли\nСчет: " + str(score))
                    new_game()
        else:
            x = (canv.coords(target[0])[0] + canv.coords(target[0])[2]) / 2     # we're getting target's coords
            y = (canv.coords(target[0])[1] + canv.coords(target[0])[3]) / 2
            r = (canv.coords(target[0])[2] - canv.coords(target[0])[0]) / 2
            if (x < r) | (x > width - r):
                target[2][0] *= -1
            if (y < r) | (y > height - r):
                target[2][1] *= -1
            for second in objects:
                if second != target:
                    x1 = (canv.coords(second[0])[0] + canv.coords(second[0])[2]) / 2    # something difficult to calc
                    y1 = (canv.coords(second[0])[1] + canv.coords(second[0])[3]) / 2    # it's bouncing
                    r1 = (canv.coords(second[0])[2] - canv.coords(second[0])[0]) / 2
                    if (x1 - x)**2 + (y1 - y)**2 < (r1 + r)**2:
                        xn = (x1 + x) / 2 - x
                        yn = (y1 + y) / 2 - y
                        xv = target[2][0]
                        yv = target[2][1]
                        x_proj = xn / (xn**2 + yn**2) * (xv * xn + yv * yn)
                        y_proj = yn / (xn**2 + yn**2) * (xv * xn + yv * yn)
                        target[2][0] -= 2 * x_proj
                        target[2][1] -= 2 * y_proj
            canv.move(target[0], target[2][0], target[2][1])

    needed_num = (score // 10) + 1    
    if obj_count < needed_num:
        for i in range(needed_num - obj_count):
            new_ball()
    root.after(10, update)

def new_game():    
    global obj_count, score, life
    obj_count = 0
    canv.delete(ALL)
    objects.clear()
    score = 0
    life = 0
    if difficulty.get() == 0:
        scoreLabel['text'] = "Счет: 0, Рекорд: " + str(high1)
    elif difficulty.get() == 1:
        scoreLabel['text'] = "Счет: 0, Рекорд: " + str(high2)
        life = 10
    else:
        scoreLabel['text'] = "Счет: 0, Рекорд: " + str(high2)
        life = 30

new_ball()
canv.bind('<Button-1>', click)
menu.add_command(label='Новая игра', command=new_game)
saved = open("save.dat")
arr = saved.readlines()
saved.close()
high1 = 0
high2 = 0
high3 = 0
if len(arr) == 0:
    saved = open("save.dat", 'w')
    saved.writelines({"0", "0", "0"})
    saved.close()
else:
    if int(arr[0]) > high1:
        high1 = int(arr[0])
        scoreLabel['text'] = "счет: 0, Рекорд: " + str(high1)
    if int(arr[1]) > high2:
        high2 = int(arr[1])
    if int(arr[2]) > high3:
        high3 = int(arr[2])
root.after(10, update)
mainloop()
