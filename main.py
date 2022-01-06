from tkinter import *
#------------part 1
sum = 0
num = 0
num1 = 0
activate1 = 0

def move(event):
    global hammer_img,num,hammer2
    hammer_img = PhotoImage(file="hammer.png")
    hammer2= canvas.create_image(event.x, event.y, image=hammer_img)
    if event.x >= 600 and event.x <= 650:
        wall.destroy()
        con2_btn.place(x= 450, y=200)
        num = 1
        canvas.unbind("<B1-Motion>")
        canvas.itemconfig(hammer2, image=non_img)
        clear_screen()






def delete_lvl2(sponge,hammer):
    canvas.delete(hammer)
    canvas.delete(sponge)


def delete(sponge, hammer):

    canvas.delete(sponge)
    canvas.delete(hammer)

def clear_screen():
    global sponge
    global hammer
    if num == 0:
        global canvas
        canvas.itemconfig(container, image = lvl2_bg)
        canvas.itemconfig(instr_text, font=("Arial", 25, "bold"),text= "בדרכו הביתה נתקל בובספוג בחומה. עזרו לבובספוג לשבור את החומה")
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btn4.destroy()
        btn5.destroy()
        Con_byn.destroy()
        hammer = canvas.create_image(150, 550, image=hammer_img)
        sponge = canvas.create_image(1000,500, image = character)
        wall.place(x=600, y= 200 )
        canvas.bind("<B1-Motion>",move)
    if num == 1:
        canvas.itemconfig(sponge, image= non_img)



def lvl6_create():
    global activate
    activate = 1
    right_btn.destroy()
    left_btn.destroy()
    same_btn.destroy()
    con6_btn.destroy()
    canvas.itemconfig(right_img, image = non_img)
    canvas.itemconfig(left_img, image=non_img)
    canvas.itemconfig(container, image = flyingbob)
    canvas.itemconfig(instr_text, text= "בובספוג עף למעלה בשמיים ומסתכל למטה,מה בובספוג יראה מהמקום בו הוא נמצא כרגע")
    con7_btn.place(x= 500, y =580)

def final():
    finish_btn.destroy()
    sky_btn.destroy()
    version2_btn.destroy()
    version3_btn.destroy()
    canvas.itemconfig(instr_text, text= "כל הכבוד עזרתם לבובספוג בהצלחה")
    canvas.itemconfig(container, image= final_img)


def to_finish():
    finish_btn.place(x= 475, y = 575)


def lvl_9():
    global activate1
    con9_btn.destroy()
    activate1 = 1
    lvl_8()
    sky_btn.place(x=475, y=200)
    version2_btn.place(x= 25, y= 300)
    version3_btn.place(x= 800, y= 200)



def lvl_8():
    global up_bob
    if activate1 == 0:
        correct_btn.destroy()
        option2_btn.destroy()
        con8_btn.destroy()
        indoor_btn.destroy()
        up_bob = canvas.create_image(575,400, image= upbob)
        canvas.itemconfig(instr_text, text= "עכשיו בובספוג עומד על האדמה ומסתכל ישר למעלה, מה בובספוג יראה משם")
        con9_btn.place(x= 500, y = 500)
    if activate1 == 1:
        canvas.itemconfig(up_bob, image=non_img)
        canvas.itemconfig(instr_text, text=" ")





def lvl7_create():
    con8_btn.place(x= 450, y= 575)


def level_7():
    con7_btn.destroy()
    canvas.itemconfig(container, image= lvl2_bg)
    canvas.itemconfig(instr_text, text=" ")
    correct_btn.place(x=475, y=200)
    indoor_btn.place(x=25, y=300)
    option2_btn.place(x=750, y=300)

def lvl_6():
    con6_btn.place(x=430, y=300)

def lvl5_create():
    con5_btn.destroy()
    canvas.itemconfig(right_img, image= line2)
    right_btn.config(command= lvl_6)
    left_btn.config(command= lvl_6)
    same_btn.config(command= lvl_6)

def level_5():
    con5_btn.place(x=430, y= 300)

def lvl4_create():
    global num1
    con4_btn.destroy()
    num1 = 1
    lvl3()
    right_btn.config(command= level_5)
    left_btn.config(command= level_5)
    same_btn.config(command= level_5)


def lvl4():
    con4_btn.place(x=430, y= 300)

def lvl3():
    global right_img, left_img
    if num1 == 0:
        canvas.itemconfig(container, image=bg3)
        canvas.itemconfig(instr_text, text="עזרו לבובספוג להחליט באיזה צד של המסך יש יותר מדוזות")
        con2_btn.destroy()
        left_img = canvas.create_image(200,350, image = duses6)

        right_img= canvas.create_image(850, 350, image = duses9)
        right_btn.place(x=850, y= 550)
        left_btn.place(x=200, y=550)
        same_btn.place(x=475, y= 550 )
    if num1 == 1:
        canvas.itemconfig(right_img, image = lineduses)




def count1():
    global btn1,sum
    btn1.config(relief=SUNKEN)
    btn1.config(state= DISABLED)
    sum = sum + 1
    if sum == 5:

        Con_byn.place(x=450,y=200)


def count2():
    global btn2,sum
    btn2.config(relief=SUNKEN)
    btn2.config(state=DISABLED)
    sum += 1
    if sum == 5:

        Con_byn.place(x=450,y=200)



def count3():
    global btn3,sum
    btn3.config(relief=SUNKEN)
    btn3.config(state=DISABLED)
    sum += 1
    if sum == 5:

        Con_byn.place(x=450,y=200)


def count4():
    global btn4,sum
    btn4.config(relief=SUNKEN)
    btn4.config(state=DISABLED)
    sum += 1
    if sum == 5:

        Con_byn.place(x=450,y=200)



def count5():
    global btn5,sum
    btn5.config(relief=SUNKEN)
    btn5.config(state=DISABLED)
    sum += 1
    if sum == 5:

        Con_byn.place(x=450,y=200)


def start_game():
    start_btn.destroy()
    canvas.itemconfig(container,image= background_img)
    canvas.itemconfig(instr_text, font=("Arial", 16, "bold") ,text= "בובספוג הגיע לסרטן הפריך וראה 5 קציצות סרטן בגדלים שונים, עזרו לבובספוג לסדר את קציצות הסרטן מהקטן לגדול")
    btn1.place(x=100, y=500)
    btn2.place(x=300, y=500)
    btn3.place(x=500, y=500)
    btn4.place(x=650, y=500)
    btn5.place(x=800, y=480)


window = Tk()
window.title("The Spongebob Game")
window.minsize(1200,675)
canvas = Canvas(width=1200, height=675)
opening = PhotoImage(file="opening.png")
background_img = PhotoImage(file="1200px-Bottle_Burglars_001.png")
container = canvas.create_image(600, 350, image= opening)
instr_text = canvas.create_text(600,80, text=" ",font = ("Arial", 50, "bold"))
canvas.place(x= 0, y=0)
burger_img = PhotoImage(file= "burger2.png")
btn1 = Button(image = burger_img, command = count1)

burger_img2= PhotoImage(file= "burger1.png")
btn2 = Button(image = burger_img2, command = count2)

burger_img3 = PhotoImage(file="burger3.png")
btn3 = Button(image = burger_img3, command = count3)

burger_img4 = PhotoImage(file="burger-4.png")
btn4 = Button(image = burger_img4, command = count4)

burger_img5 = PhotoImage(file="burger5.png")
btn5 = Button(image = burger_img5, command = count5)

Con_byn = Button(text="עבודה טובה, לחץ כדי להמשיך", font=("Arial", 15, "bold"), command=clear_screen)
start_btn = Button(text="ברוך הבא למסע של בובספוג, לחץ כדי להתחיל", font=("Arial", 15, "bold"), command=start_game)
start_btn.place(x=425, y=300)


#------------part 1
#------------part2

lvl2_bg = PhotoImage(file="background2.png")
character = PhotoImage(file= "spongebob.png")
hammer_img = PhotoImage(file = "hammer.png")
wall = Label(background="black", height=600, width=4)
con2_btn =  Button(text="עבודה טובה, לחץ כדי להמשיך", font=("Arial", 15, "bold"), command=lvl3)
#------------part3
bg3 = PhotoImage(file= "background3.png")
duses6 = PhotoImage(file= "duses4.png")
non_img = PhotoImage(file= "transparent.png")
duses9 = PhotoImage(file = "duses9.png")
right_btn = Button(text="ימין", font=("Arial", 15, "bold"), command=lvl4)
left_btn = Button(text="שמאל", font=("Arial", 15, "bold"), command=lvl4)
same_btn = Button(text="שניהם אותו הדבר", font=("Arial", 15, "bold"), command=lvl4)
con4_btn = Button(text="עבודה טובה, לחץ כדי להמשיך", font=("Arial", 15, "bold"),command= lvl4_create)
#--------part4
lineduses = PhotoImage(file= "lineduse.png")
#--------part5
con5_btn = Button(text="עבודה טובה, לחץ כדי להמשיך", font=("Arial", 15, "bold"),command= lvl5_create)
line2 = PhotoImage(file= "line3.png")
#--------part6
con6_btn = Button(text="עבודה טובה, לחץ כדי להמשיך", font=("Arial", 15, "bold"),command= lvl6_create)

#-------part7
flyingbob = PhotoImage(file= "bobsfogfly.png")
con7_btn = Button(text="לחץ כדי להמשיך", font=("Arial", 15, "bold"),command= level_7)
correct = PhotoImage(file= "correct.png")
indoor = PhotoImage(file= "indoor.png")
option2 = PhotoImage(file= "option2.png")
correct_btn = Button(image = correct, command = lvl7_create)
indoor_btn = Button(image = indoor, command = lvl7_create)
option2_btn = Button(image= option2, command= lvl7_create)
con8_btn = Button(text="עבודה טובה, לחץ כדי להמשיך", font=("Arial", 15, "bold"),command= lvl_8)
#-------part8
upbob = PhotoImage(file= "upbob.png")
con9_btn = Button(text="לחץ כדי להמשיך", font=("Arial", 15, "bold"),command= lvl_9)
#------part 9
sky = PhotoImage(file = "sky.png")
sky_btn = Button(image = sky, command = to_finish)
version2 = PhotoImage(file="version2.png")
version2_btn = Button(image = version2, command = to_finish)
version3 = PhotoImage(file= "version3.png")
version3_btn = Button(image = version3, command = to_finish)
#-------finish
finish_btn = Button(text="עבודה טובה, לחץ כדי להמשיך", font=("Arial", 15, "bold"),command= final)
final_img = PhotoImage(file = "patrick.png")






window.mainloop()