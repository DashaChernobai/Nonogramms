import time
import pygame
import sys
import pyrebase

firebaseConfig = {'apiKey': "AIzaSyCHA9Z0syFJpGD-KJev_KwLBbKd6F7orAc",
                  'authDomain': "fir-course-3ef7c.firebaseapp.com",
                  'databaseURL': "https://fir-course-3ef7c-default-rtdb.firebaseio.com/",
                  'projectId': "fir-course-3ef7c",
                  'storageBucket': "fir-course-3ef7c.appspot.com",
                  'messagingSenderId': "444395592265",
                  'appId': "1:444395592265:web:a41144b7d4b2e49ba33d98",
                  'measurementId': "G-XJM8N51TZ7"}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()



pygame.init()

width = height = 350

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("main")

#black = (0, 0, 0)
#red = (255, 0, 0)
green = (0, 255, 0)
#white = (255, 255, 255)

#light_blue=(156,209,224)
#light_black=(54,52,52)
#light_grey = (176, 176, 176)

black = (39, 45, 45)
light_black = (40, 94, 82)
light_blue = (103, 199, 166)
red = (165, 255, 214)
light_grey = (210, 255, 235)
white = (255, 255, 255)

h1 = 70
w1 = 200
ots_up = 70
margin = 25
size_block = (width - 4 * margin) / 3
state = "main"

levels = db.child("Levels").child().get()
number_of_levels = len(levels.val())
print("number_of_levels")
print(number_of_levels)
my_list = []
for i in range(1, number_of_levels + 1):
    my_list.append(i)


print("my_list")
print(my_list)
def chanching_levels_names():
    print("levels")
    i=0
    number_of_levels_two=0
    while i < 15:
        lvlname="level "+str(i)
        data=db.child("Levels").child(lvlname).get().val()
        print(data)
        if data != None:
            number_of_levels_two+=1
            lvlname2 = "level "  + str(number_of_levels_two)
            print(lvlname2)
            print(lvlname2)
            db.child("Levels").child(lvlname).remove()
            db.child("Levels").child(lvlname2).set(data)

        i = i + 1
    print(number_of_levels_two)
chanching_levels_names()
def transform_to_mass(mas, maxUp):
    qwe = [[0] * maxUp for i in range(len(mas))]
    print("qwe   " + str(qwe))
    print("maxUp   " + str(maxUp))
    print("[0] * maxUp   " + str([0] * maxUp))
    print("len(mas)   " + str(len(mas)))
    for col in range(len(mas)):
        string = mas[col]
        while 2 * maxUp - 1 != len(string):
            if 2 * maxUp - 1 > len(string):
                string = "0 " + string
        result = string.split(" ")
        qwe[col] = result
    print("transform_to_mass   "+str(qwe))
    return qwe
def transform_str_to_up_left(mas,up,left):
    print("3333333333333333333")
    print(len(mas))
    print(len(mas[0]))
    for row in range(len(mas)):
        s = 0
        string = ''
        pause = False
        for col in range(len(mas[0])):
            if mas[row][col] == '1':
                s += 1
            elif mas[row][col] == '0':
                if s == 0:
                    if string != '':
                        string += ' '
                        pause = True
                else:
                    if pause == False:
                        string += ' ' + str(s)
                    else:
                        string += str(s)
                    s = 0
                    pause = False
        if mas[row][col] == '1':
            if s == 0:
                string += '1'
            else:
                if pause == True:
                    string += str(s)
                else:
                    string += ' ' + str(s)
        print("1 string.strip()")
        print(string.strip())
        up.append(string.strip())
    # print("up")
    # print(up)



    for row in range(len(mas[0])):
        s = 0
        string = ''
        pause = False
        for col in range(len(mas)):
            if mas[col][row] == '1':
                s += 1
            elif mas[col][row] == '0':
                if s == 0:
                    if string != '':
                        string += ' '
                        pause = True
                else:
                    if pause == False:
                        string += ' ' + str(s)
                    else:
                        string += str(s)
                    s = 0
                    pause = False
        if mas[col][row] == '1':
            if s == 0:
                string += '1'
            else:
                if pause == True:
                    string += str(s)
                else:
                    string += ' ' + str(s)
        print("2 string.strip()")
        print(string.strip())
        left.append(string.strip())
    #     left+=string.strip()+" "
    # print("left")
    print("left")
    print(left)
    print("up")
    print(up)


def check(mas, numbers_up, numbers_left):

    print("mas = "+ str(mas))
    check1 = True

    for row in range(len(mas)):
        s = 0
        string = ''
        pause = False
        for col in range(len(mas[0])):
            if mas[row][col] == '1':
                s += 1
            elif mas[row][col] == '0':
                if s == 0:
                    if string != '':
                        string += ' '
                        pause = True
                else:
                    if pause == False:
                        string += ' ' + str(s)
                    else:
                        string += str(s)
                    s = 0
                    pause = False
        if mas[row][col] == '1':
            if s == 0:
                string += '1'
            else:
                if pause == True:
                    string += str(s)
                else:
                    string += ' ' + str(s)
        print(string.strip())
        print(numbers_up[row])
        if string.strip() != numbers_up[row]:
            check1 = False

    print('      1 ' + str(check1))

    check2 = True

    for row in range(len(mas)):
        s = 0
        string = ''
        pause = False
        for col in range(len(mas[0])):
            if mas[row][col] == '1':
                s += 1
            elif mas[row][col] == '0':
                if s == 0:
                    if string != '':
                        string += ' '
                        pause = True
                else:
                    if pause == False:
                        string += ' ' + str(s)
                    else:
                        string += str(s)
                    s = 0
                    pause = False
        if mas[row][col] == '1':
            if s == 0:
                string += '1'
            else:
                if pause == True:
                    string += str(s)
                else:
                    string += ' ' + str(s)
        print(string.strip())
        print(numbers_up[row])
        if string.strip() != numbers_left[row]:
            check2 = False

    print('      2 ' + str(check2))

    if check1 and check2:
        print("Е бои!!! Мои поздравения!!!")


def draw_main():
    width = height = 350
    pygame.display.set_caption("main")
    size_window = (width, height)
    screen = pygame.display.set_mode(size_window)
    screen.fill(white)
    pygame.draw.rect(screen, black, ((width - w1) // 2, ots_up, w1, h1))
    pygame.draw.rect(screen, black, ((width - w1) // 2, ots_up * 2 + h1, w1, h1))

    font = pygame.font.SysFont('stxingkai', 50)
    text1 = font.render("Играть", True, white)
    text_rect = text1.get_rect()
    text_x = width / 2 - text_rect.width / 2
    text_y = ots_up + h1 / 2 - text_rect.height / 2
    screen.blit(text1, [text_x, text_y])

    font = pygame.font.SysFont('stxingkai', 50)
    text2 = font.render("Изменить", True, white)
    text_rect = text2.get_rect()
    text_x = width / 2 - text_rect.width / 2
    text_y = ots_up + h1 / 2 + h1 + ots_up - text_rect.height / 2
    screen.blit(text2, [text_x, text_y])


btn_back_w = 170
btn_back_h = 50
btn_margin = 20


def draw_changing():
    size_window = (width + btn_back_w-70, height+ots_up+h1)
    screen = pygame.display.set_mode(size_window)
    screen.fill(black)

    pygame.draw.rect(screen, light_blue, ((width - w1) // 2+250, ots_up, btn_back_w-70, btn_back_h))

    font = pygame.font.SysFont('stxingkai', 20)
    text1 = font.render("Вернуться", True, black)
    text_rect = text1.get_rect()
    text_x = (width - w1) // 2+250 + (btn_back_w-70) / 2 - text_rect.width / 2
    text_y = ots_up + btn_back_h / 2 - text_rect.height / 2
    screen.blit(text1, [text_x, text_y])


    pygame.draw.rect(screen, white, ((width - w1) // 2, ots_up, w1, h1))
    pygame.draw.rect(screen, white, ((width - w1) // 2, ots_up * 2 + h1, w1, h1))
    pygame.draw.rect(screen, white, ((width - w1) // 2, ots_up * 3 + 2*h1, w1, h1))

    font = pygame.font.SysFont('stxingkai', 35)
    text1 = font.render("Создать", True, black)
    text_rect = text1.get_rect()
    text_x = width / 2 - text_rect.width / 2
    text_y = ots_up + h1 / 2 - text_rect.height / 2
    screen.blit(text1, [text_x, text_y])

    font = pygame.font.SysFont('stxingkai', 35)
    text2 = font.render("Редактировать", True, black)
    text_rect = text2.get_rect()
    text_x = width / 2 - text_rect.width / 2
    text_y = ots_up + h1 / 2 + h1 + ots_up - text_rect.height / 2
    screen.blit(text2, [text_x, text_y])

    font = pygame.font.SysFont('stxingkai', 40)
    text2 = font.render("Удалить", True, black)
    text_rect = text2.get_rect()
    text_x = width / 2 - text_rect.width / 2
    text_y = ots_up + h1 / 2 + h1 + ots_up - text_rect.height / 2 + h1 + ots_up
    screen.blit(text2, [text_x, text_y])



def draw_levels():
    marginUp = 30
    marginLeft = 30
    margin = 5

    size_num = 60
    bloc_size = 100


    size_window = (width+btn_back_w, height)
    screen = pygame.display.set_mode(size_window)
    screen.fill(black)
    pygame.draw.rect(screen, light_blue, (width-btn_margin, height-btn_back_h-btn_margin, btn_back_w, btn_back_h))

    font = pygame.font.SysFont('stxingkai', 40)
    text1 = font.render("Вернуться", True, black)
    text_rect = text1.get_rect()
    text_x = width-btn_margin+(btn_back_w)/2 - text_rect.width / 2
    text_y = height-btn_margin -btn_back_h / 2 - text_rect.height / 2
    screen.blit(text1, [text_x, text_y])

    for row in range(3):
        for col in range(3):
            x = col * size_block + (col + 1) * margin
            y = row * size_block + (row + 1) * margin


            font = pygame.font.SysFont('stxingkai', 40)
            # print(row*3+col)
            if (row * 3 + col + 1 <= len(my_list)):
                text1 = font.render(str(my_list[row * 3 + col]), True, black)

                pygame.draw.rect(screen, white, (x, y, size_block, size_block))
            else:
                text1 = font.render("?", True, red)
            text_rect = text1.get_rect()
            text_x = x + size_block / 2 - text_rect.width / 2
            text_y = y + size_block / 2 - text_rect.height / 2
            screen.blit(text1, [text_x, text_y])
            if (X > x) and (X < x + size_block) and (Y > y) and (Y < y + size_block):
                if (row * 3 + col + 1 <= len(my_list)):
                    print(len(my_list))
                    # print(my_list[row * 3 + col])
                    draw_lvl(my_list[row * 3 + col])
                    level = my_list[row * 3 + col]
                    print("level : " + str(level))
                    state = "level"  # + my_list[row * 3 + col]
                    print("Состояное Уровень")
                    screen.fill(black)
def UpdateMas(mas,level_name):

    # db.child("Users").child("user 3").set(data)
    # new_lvl = db.child("Levels").child().get()
    name= level_name
    print("name")
    print(name)


    my_list.append(len(my_list)+1)
    m = len(mas)
    n = len(mas[0])
    print(str(n)+" "+str(m))
    up=[]
    print(up)
    left=[]
    print(left)
    # 1 2 3 4 ... n/m ->

    if n==1:
        d_left={1:""}
    if m==1:
        d_up={1:""}

    if n==2:
        d_left={1:"",2:""}
    if m==2:
        d_up={1:"",2:""}

    if n==3:
        d_left={1:"",2:"",3:""}
    if m==3:
        d_up={1:"",2:"",3:""}

    if n==4:
        d_left={1:"",2:"",3:"",4:""}
    if m==4:
        d_up={1:"",2:"",3:"",4:""}

    if n==5:
        d_left={1:"",2:"",3:"",4:"",5:""}
    if m==5:
        d_up={1:"",2:"",3:"",4:"",5:""}

    if n==6:
        d_left={1:"",2:"",3:"",4:"",5:"",6:""}
    if m==6:
        d_up={1:"",2:"",3:"",4:"",5:"",6:""}

    if n==7:
        d_left={1:"",2:"",3:"",4:"",5:"",6:"",7:""}
    if m==7:
        d_up={1:"",2:"",3:"",4:"",5:"",6:"",7:""}

    if n==8:
        d_left={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:""}
    if m==8:
        d_up={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:""}


    db.child("Levels").child(name).child("up").set(d_up)
    db.child("Levels").child(name).child("left").set(d_left)
    transform_str_to_up_left(mas,up,left)
    # print("222 up")
    # print(up)
    #
    # print("222 left")
    # print(left)
    for row in range(n):
        str0=""
        for col in range(m):
            print(col)
            str0+=mas[col][row]
            print("up[col]")
            print(str(up[col]))

        db.child("Levels").child(name).child("sol").update({row+1:str0})
        # print()
        # print(str(row + 1) + " " + str(left[col]))
        db.child("Levels").child(name).child("left").update({row+1:str(left[row])})

    for row1 in range(m):
        db.child("Levels").child(name).child("up").update({row1 + 1: str(up[row1])})
        # print(str(row+1)+" "+str(left[col]))
        # db.child("Levels").child(name).child("up").update({row + 1: up[col]})
    print("data was seted")
def SaveMas(mas,my_list):

    # db.child("Users").child("user 3").set(data)
    # new_lvl = db.child("Levels").child().get()
    name= "level "+str(len(my_list)+1)
    print("name")
    print(name)


    my_list.append(len(my_list)+1)
    m = len(mas)
    n = len(mas[0])
    print(str(n)+" "+str(m))
    up=[]
    print(up)
    left=[]
    print(left)
    # 1 2 3 4 ... n/m ->

    if n==1:
        d_left={1:""}
    if m==1:
        d_up={1:""}

    if n==2:
        d_left={1:"",2:""}
    if m==2:
        d_up={1:"",2:""}

    if n==3:
        d_left={1:"",2:"",3:""}
    if m==3:
        d_up={1:"",2:"",3:""}

    if n==4:
        d_left={1:"",2:"",3:"",4:""}
    if m==4:
        d_up={1:"",2:"",3:"",4:""}

    if n==5:
        d_left={1:"",2:"",3:"",4:"",5:""}
    if m==5:
        d_up={1:"",2:"",3:"",4:"",5:""}

    if n==6:
        d_left={1:"",2:"",3:"",4:"",5:"",6:""}
    if m==6:
        d_up={1:"",2:"",3:"",4:"",5:"",6:""}

    if n==7:
        d_left={1:"",2:"",3:"",4:"",5:"",6:"",7:""}
    if m==7:
        d_up={1:"",2:"",3:"",4:"",5:"",6:"",7:""}

    if n==8:
        d_left={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:""}
    if m==8:
        d_up={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:""}


    db.child("Levels").child(name).child("up").set(d_up)
    db.child("Levels").child(name).child("left").set(d_left)
    transform_str_to_up_left(mas,up,left)
    # print("222 up")
    # print(up)
    #
    # print("222 left")
    # print(left)
    for row in range(n):
        str0=""
        for col in range(m):
            print(col)
            str0+=mas[col][row]
            print("up[col]")
            print(str(up[col]))

        db.child("Levels").child(name).child("sol").update({row+1:str0})
        # print()
        # print(str(row + 1) + " " + str(left[col]))
        db.child("Levels").child(name).child("left").update({row+1:str(left[row])})

    for row1 in range(m):
        db.child("Levels").child(name).child("up").update({row1 + 1: str(up[row1])})
        # print(str(row+1)+" "+str(left[col]))
        # db.child("Levels").child(name).child("up").update({row + 1: up[col]})
    print("data was seted")

def UpdateMas(mas,level_name):

    # db.child("Users").child("user 3").set(data)
    # new_lvl = db.child("Levels").child().get()
    name= level_name
    print("name")
    print(name)


    #my_list.append(len(my_list)+1)
    m = len(mas)
    n = len(mas[0])
    print(str(n)+" "+str(m))
    up=[]
    print(up)
    left=[]
    print(left)
    # 1 2 3 4 ... n/m ->

    # if n==1:
    #     d_left={1:""}
    # if m==1:
    #     d_up={1:""}
    #
    # if n==2:
    #     d_left={1:"",2:""}
    # if m==2:
    #     d_up={1:"",2:""}
    #
    # if n==3:
    #     d_left={1:"",2:"",3:""}
    # if m==3:
    #     d_up={1:"",2:"",3:""}
    #
    # if n==4:
    #     d_left={1:"",2:"",3:"",4:""}
    # if m==4:
    #     d_up={1:"",2:"",3:"",4:""}
    #
    # if n==5:
    #     d_left={1:"",2:"",3:"",4:"",5:""}
    # if m==5:
    #     d_up={1:"",2:"",3:"",4:"",5:""}
    #
    # if n==6:
    #     d_left={1:"",2:"",3:"",4:"",5:"",6:""}
    # if m==6:
    #     d_up={1:"",2:"",3:"",4:"",5:"",6:""}
    #
    # if n==7:
    #     d_left={1:"",2:"",3:"",4:"",5:"",6:"",7:""}
    # if m==7:
    #     d_up={1:"",2:"",3:"",4:"",5:"",6:"",7:""}
    #
    # if n==8:
    #     d_left={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:""}
    # if m==8:
    #     d_up={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:""}


    # db.child("Levels").child(name).child("up").set(d_up)
    # db.child("Levels").child(name).child("left").set(d_left)
    transform_str_to_up_left(mas,up,left)
    # print("222 up")
    # print(up)
    #
    # print("222 left")
    # print(left)
    for row in range(n):
        str0=""
        for col in range(m):
            print(col)
            str0+=mas[col][row]
            print("up[col]")
            print(str(up[col]))

        db.child("Levels").child(name).child("sol").update({row+1:str0})
        # print()
        # print(str(row + 1) + " " + str(left[col]))
        db.child("Levels").child(name).child("left").update({row+1:str(left[row])})

    for row1 in range(m):
        db.child("Levels").child(name).child("up").update({row1 + 1: str(up[row1])})
        # print(str(row+1)+" "+str(left[col]))
        # db.child("Levels").child(name).child("up").update({row + 1: up[col]})
    print("data was updated")


while True:
    for event in pygame.event.get():  # пока идет игра

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:  # если нажата кнопка мыши

            x_mouse, y_mouse = pygame.mouse.get_pos()
            X = x_mouse
            Y = y_mouse



            # пока находимся в меню можем клацнуть на кнопку играть
            if state == "main" and (X > (width - w1) // 2) and (X < (width - w1) // 2 + w1) and (Y > ots_up) and (
                    Y < ots_up + h1):
                print("Открыть уровни")

                X = 0
                Y = 0

                state = "levels"
                #time.sleep(1)
                draw_levels()


                print("Состояное Уровни")
                name=""
                pygame.display.set_caption("main/levels")


                # пока находимся в меню можем клацнуть на кнопку изменить   (добавить уровень или удаить его)
            elif state == "main" and (X > (width - w1) // 2) and (X < (width - w1) // 2 + w1) and (
                    Y > ots_up * 2 + h1) and (
                    Y < ots_up * 2 + h1 + h1):
                # print("btn2")
                state = "change"
                print("Состояное Изменить")
                pygame.display.set_caption("main/changing")


            elif state == "change" and (X > (width - w1) // 2) and (X < (width - w1) // 2 + w1) and \
                    (Y > ots_up) and (
                    Y < ots_up + h1):
                # print("btn1")
                X=0
                Y=0
                state = "creating"
                print("Состояное Создание нового уровня")

                pygame.display.set_caption("main/changing/creating")


                # пока находимся в меню можем клацнуть на кнопку изменить   (добавить уровень или удаить его)

            elif state == "change" and (X > (width - w1) // 2) and (X < (width - w1) // 2 + w1) and (
                    Y > ots_up * 2 + h1) and (
                    Y < ots_up * 2 + h1 + h1):
                # print("btn2")
                draw_levels()
                state = "editing"
                print("Состояное Изменение уровня")
                pygame.display.set_caption("main/changing/editing")



            elif state == "change" and (X > (width - w1) // 2) and (X < (width - w1) // 2 + w1) and (
                    Y > ots_up * 3 + 2*h1) and (
                    Y < ots_up * 3 + 2*h1 + h1):
                # print("btn2")
                draw_levels()
                state = "deleting"

                print("Состояное Удаление уровня")
                pygame.display.set_caption("main/changing/deleting")

            elif state == "change" and (X > (width - w1) // 2+250) and (X <  (width - w1) // 2+250+ btn_back_w-70) and (
                    Y > ots_up) and (
                    Y <  ots_up+btn_back_h):
                # print("btn2")
                draw_main()
                state = "main"
                print("Состояное Меню")

                pygame.display.set_caption("main")


            if state == "creating":

                marginUp = 30
                marginLeft = 30
                margin = 3

                size_num = 60
                bloc_size = 40
                btn_create_h = 50
                btn_create_w = 150
                margin_r_l = 30
                www=bloc_size*8+9*margin+btn_create_w+2*margin_r_l
                hhh=bloc_size*8+9*margin
                size_window = (www, hhh)
                screen = pygame.display.set_mode(size_window)
                screen.fill(black)

                pygame.draw.rect(screen, white,
                                  (www-btn_create_w-margin_r_l, hhh/2-(btn_create_h)/2, btn_create_w, btn_create_h))

                font = pygame.font.SysFont('stxingkai', 25)
                text1 = font.render("Сгенерировать", True, black)
                text_rect = text1.get_rect()
                text_x = www-(btn_create_w+2*margin_r_l)/2 - text_rect.width / 2
                text_y = hhh /2 - text_rect.height / 2
                screen.blit(text1, [text_x, text_y])

                for row in range(8):
                    for col in range(8):

                        x = col * bloc_size + (col + 1) * margin
                        y = row * bloc_size + (row + 1) * margin
                        pygame.draw.rect(screen, red, (x, y, bloc_size, bloc_size))
                for row in range(8):  # не трогай тройку!!!!!!!!!!!!! Это меню с уровнями
                    for col in range(8):  # не трогай тройку!!!!!!!!! Это меню с уровнями
                        x = col * bloc_size + (col + 1) * margin
                        y = row * bloc_size + (row + 1) * margin
                        if (X > x) and (X < x + bloc_size) and (Y > y) and (Y < y + bloc_size):

                            n=row+1
                            m=col+1
                            print(str(n)+" "+str(m))
                            for row1 in range(n):
                                for col1 in range(m):
                                    x = col1 * bloc_size + (col1 + 1) * margin
                                    y = row1 * bloc_size + (row1 + 1) * margin
                                    pygame.draw.rect(screen, white, (x, y, bloc_size, bloc_size))


                if (X > www-btn_create_w-margin_r_l) and (X < www-margin_r_l) and (
                        Y > hhh/2-(btn_create_h)/2) and (
                        Y < hhh/2+(btn_create_h)/2):

                    print(str(n) + " " + str(m))
                    print("###############################################")
                    mas = [["0"] * n for i in range(m)]
                    print("mas")
                    print(mas)
                    state="create_lvl"

                if state=="create_lvl":

                    def create_lvl(n, m):

                        print("n*m " + str(n) + "   " + str(m))

                        marginUp = 20
                        marginLeft = 20
                        margin = 5

                        bloc_size = 60
                        ww = 2 * marginUp + m * bloc_size + (m + 1) * margin
                        hh = 2 * marginLeft + n * bloc_size + (n + 1) * margin
                        btn_back_w = 100
                        btn_back_h = 40
                        mar = 8
                        screen = pygame.display.set_mode((ww + btn_back_w + (2 * mar), hh))
                        screen.fill(white)

                        pygame.draw.rect(screen, light_black, (ww + mar-margin,
                                                               hh / 2 - (btn_back_h) / 2, btn_back_w, btn_back_h))


                        font = pygame.font.SysFont('stxingkai', 30)

                        text1 = font.render("Создать", True, red)
                        text_rect = text1.get_rect()
                        text_x = ww + mar-margin + (btn_back_w) / 2 - text_rect.width / 2
                        text_y = hh / 2 - (btn_back_h) / 2 +(btn_back_h) / 2 - text_rect.height / 2
                        screen.blit(text1, [text_x, text_y])

                        for row in range(n):
                            for col in range(m):
                                x = col * bloc_size + (col + 1) * margin + marginUp
                                y = row * bloc_size + (row + 1) * margin + marginLeft

                                pygame.draw.rect(screen, black, (x, y, bloc_size, bloc_size))



                    create_lvl(n, m)


            elif state=="create_lvl":
                marginUp = 20
                marginLeft = 20
                margin = 5
                bloc_size = 60
                print("mas")
                print(mas)
                mar=8
                ww = 2 * marginUp + m * bloc_size + (m + 1) * margin
                hh = 2 * marginLeft + n * bloc_size + (n + 1) * margin
                if (X > ww + mar - margin) and (X < ww + mar - margin + btn_back_w) and (
                        Y > hh / 2 - (btn_back_h) / 2) and (Y < hh / 2 - (btn_back_h) / 2 + btn_back_h):
                    print("lllllllllllll")
                    SaveMas(mas,my_list)
                    state = "main"
                    # конвертация матрицы в строки ответа
                    # конвертация матрицы в значения up left



                for row in range(n):
                    for col in range(m):
                        x = col * bloc_size + (col + 1) * margin + marginUp
                        y = row * bloc_size + (row + 1) * margin + marginLeft
                        if (X > x) and (X < x + bloc_size) and (Y > y) and (Y < y + bloc_size):

                            print(mas)
                            if mas[col][row]=='0':
                                pygame.draw.rect(screen, red, (x, y, bloc_size, bloc_size))
                                mas[col][row] = '1'
                            else:
                                pygame.draw.rect(screen, black, (x, y, bloc_size, bloc_size))
                                mas[col][row] = '0'
                            print("mas")
                            print(mas)


            elif state == "editing":


                def edit_lvl(lvl_name):
                    state="edit"
                    name = "level " + str(lvl_name)

                    n = len(db.child("Levels").child(name).child().child("left").get().val()) - 1
                    m = len(db.child("Levels").child(name).child().child("up").get().val()) - 1
                    print("n*m " + str(n) + "   " + str(m))

                    up = db.child("Levels").child(name).child().child("left").get().val()
                    print("up")
                    up.pop(0)
                    print(up)

                    left = db.child("Levels").child(name).child().child("up").get().val()
                    print("left")
                    left.pop(0)
                    print(left)

                    spaces1 = 0

                    for row in range(len(up)):
                        print("str(up[row].count(" "))" + str(up[row].count(" ")))
                        if (str(up[row]).count(" ")) > spaces1:
                            spaces1 = up[row].count(" ")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!up " + str(up[row]) + "   " + str(up[row].count(" ")))

                    print("maxUp")
                    spaces1 += 1
                    print(spaces1)
                    maxUp = spaces1

                    spaces2 = 0
                    for row in range(len(left)):
                        print("str(up[row].count(" "))" + str(left[row].count(" ")))
                        if (str(left[row]).count(" ")) > spaces2:
                            spaces2 = left[row].count(" ")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!left " + str(left[row]) + "   " + str(
                                left[row].count(" ")))

                    print("maxLeft")
                    spaces2 += 1
                    print(spaces2)
                    maxLeft = spaces2

                    marginUp = 30
                    marginLeft = 30
                    margin = 5

                    size_num = 60
                    bloc_size = 100
                    ww = 2 * marginUp + maxUp * size_num + m * bloc_size
                    hh = 2 * marginLeft + maxLeft * size_num + n * bloc_size

                    screen = pygame.display.set_mode((ww + 40 + 5 * (m - 3) + btn_back_w, hh + 40 + 5 * (n - 3)))
                    screen.fill(white)

                    pygame.draw.rect(screen, light_black,
                                     (ww + 40 + 5 * (m - 3) - (0.5) * marginUp,
                                      hh + 40 + 5 * (n - 3) - btn_back_h - marginLeft, btn_back_w, btn_back_h))

                    font = pygame.font.SysFont('stxingkai', 40)

                    text1 = font.render("Вернуться", True, red)
                    text_rect = text1.get_rect()
                    text_x = ww + 40 + 5 * (m - 3) - (0.5) * marginUp + (btn_back_w) / 2 - text_rect.width / 2
                    text_y = hh + 40 + 5 * (n - 3) - marginLeft - (btn_back_h) / 2 - text_rect.height / 2
                    screen.blit(text1, [text_x, text_y])


                    pygame.draw.rect(screen, light_black,
                                     (ww + 40 + 5 * (m - 3) - (0.5) * marginUp,
                                      hh / 2 + btn_back_h, btn_back_w, btn_back_h))
                    text2 = font.render("Сохранить", True, red)
                    text_rect = text2.get_rect()
                    text2_x = ww + 40 + 5 * (m - 3) - (0.5) * marginUp + (btn_back_w) / 2 - text_rect.width / 2
                    text2_y = hh / 2 + btn_back_h + btn_back_h/2 - text_rect.height / 2
                    screen.blit(text2, [text2_x, text2_y])

                    pygame.draw.rect(screen, light_grey, (
                        marginLeft, marginUp, ww - 2 * marginLeft + 40 + 5 * (m - 3),
                        hh - 2 * marginUp + 40 + 5 * (n - 3)))
                    # level_1_1=up
                    # print("level_1_1")
                    # print(level_1_1)
                    # print("up")
                    # print(up)
                    res_level_1_1 = transform_to_mass(up, maxUp)

                    print("res_level_1_1")
                    print(res_level_1_1)
                    for row in range(maxUp):
                        for col in range(n):
                            x = row * size_num + (row + 1) * margin + marginUp + 5  # + maxUp * size_num
                            y = col * bloc_size + (col + 1) * margin + maxLeft * size_num + 40 + 5
                            pygame.draw.rect(screen, light_blue, (x, y, size_num, bloc_size))
                            ################
                            font = pygame.font.SysFont('stxingkai', 40)
                            text1 = font.render(res_level_1_1[col][row], True, white)
                            text_rect = text1.get_rect()
                            text_x = (2 * x + size_num) / 2 - text_rect.width / 2
                            text_y = (2 * y + bloc_size) / 2 - text_rect.height / 2
                            screen.blit(text1, [text_x, text_y])
                    # level_1_2 = left
                    print("level_1_2")
                    # print(level_1_2)
                    res_level_1_2 = transform_to_mass(left, maxLeft)
                    print("res_level_1_2")
                    print(res_level_1_2)
                    # print("left")
                    print("!!!!!!!!!!!!!!!!!!!!!!")

                    for row in range(maxLeft):
                        for col in range(m):
                            x = col * bloc_size + (col + 1) * margin + maxUp * size_num + 40 + 5
                            y = row * size_num + (row + 1) * margin + marginUp + 5  # + maxUp * size_num
                            pygame.draw.rect(screen, light_blue, (x, y, bloc_size, size_num))
                            font = pygame.font.SysFont('stxingkai', 40)
                            text1 = font.render(res_level_1_2[col][row], True, white)
                            text_rect = text1.get_rect()
                            text_x = (2 * x + bloc_size) / 2 - text_rect.width / 2
                            text_y = (2 * y + size_num) / 2 - text_rect.height / 2
                            screen.blit(text1, [text_x, text_y])



                    sol = db.child("Levels").child(name).child().child("sol").get().val()
                    sol.pop(0)
                    sol_mas = [['0'] * m for i in range(n)]
                    level_1 = [['0'] * m for i in range(n)]
                    level_1=sol_mas
                    print("sol_mas   " + str(sol_mas))
                    for row in range(n):

                        mystr = sol[row]
                        result = list(map(int, mystr))
                        #print("resuuuuuuult")
                        #print(str(result))
                        for col in range(m):
                            sol_mas[row][col] = str(result[col])
                    print("sol_mas   " + str(sol_mas))
                    print("level_1   " + str(level_1))
                    for row in range(n):
                        for col in range(m):
                            #print(str(row)+" "+str(col)+" = "+str(sol_mas[row][col]))
                            x = col * bloc_size + (col + 1) * margin + maxUp * size_num + 40 + 5
                            y = row * bloc_size + (row + 1) * margin + maxLeft * size_num + 40 + 5

                            if sol_mas[row][col] == "1":
                                pygame.draw.rect(screen, black, (x, y, bloc_size, bloc_size))

                            else:
                                pygame.draw.rect(screen, white, (x, y, bloc_size, bloc_size))


                    #UpdateMas(level_1,name)
                    #state = "main"
                            # else:
                            #     pygame.draw.rect(screen, red, (x, y, bloc_size, bloc_size))


                            #pygame.draw.rect(screen, red, (x, y, bloc_size, bloc_size))





                for row in range(3):#не трогай тройку!!!!!!!!!!!!! Это меню с уровнями
                    for col in range(3):#не трогай тройку!!!!!!!!! Это меню с уровнями
                        x = col * size_block + (col + 1) * margin
                        y = row * size_block + (row + 1) * margin
                        if (X > x) and (X < x + size_block) and (Y > y) and (Y < y + size_block):
                            if (row * 3 + col + 1 <= len(my_list)):
                                # print(my_list[row * 3 + col])
                                state = "edit"
                                edit_lvl(my_list[row * 3 + col])
                                level = my_list[row * 3 + col]
                                print("level : " + str(level))
                                state = "edit"  # + my_list[row * 3 + col]
                                name = "level " + str(level)

                                n = len(db.child("Levels").child(name).child().child("up").get().val()) - 1
                                m = len(db.child("Levels").child(name).child().child("left").get().val()) - 1
                                sol = db.child("Levels").child(name).child().child("sol").get().val()
                                sol.pop(0)
                                sol_mas = [['0'] * m for i in range(n)]
                                level_1 = [['0'] * m for i in range(n)]
                                for row in range(m):

                                    mystr = sol[row]
                                    result = list(map(int, mystr))
                                    print("resuuuuuuult")
                                    print(str(result))
                                    for col in range(n):
                                        sol_mas[row][col] = str(result[col])
                                print("sol_mas   " + str(sol_mas))



                                #### my_list[row * 3 + col]
                if (X > width - btn_margin) and (X < width - btn_margin + btn_back_w) and (
                                Y > height - btn_back_h - btn_margin) and (
                                Y < height - btn_margin):
                    db.child("Levels").child(name).update()
                    levels = db.child("Levels").child().get()
                    number_of_levels = len(levels.val())
                    print("number_of_levels")
                    print(number_of_levels)
                    my_list = []
                    for i in range(1, number_of_levels + 1):
                        my_list.append(i)
                    print("level was updated")
                    state = "main"
                    size_window = (width, height)
                    screen = pygame.display.set_mode(size_window)



                #   находимся в окне выбора уровня


            elif state == "deleting":

                for row in range(3):  # не трогай тройку!!!!!!!!!!!!! Это меню с уровнями
                    for col in range(3):  # не трогай тройку!!!!!!!!! Это меню с уровнями
                        x = col * size_block + (col + 1) * margin
                        y = row * size_block + (row + 1) * margin
                        if (X > x) and (X < x + size_block) and (Y > y) and (Y < y + size_block):
                            if (row * 3 + col + 1 <= len(my_list)):
                                # print(my_list[row * 3 + col])

                                level = my_list[row * 3 + col]
                                name = "level " + str(level)
                                db.child("Levels").child(name).remove()
                                print("level was deleted")
                                state="main"
                                chanching_levels_names()

                                levels = db.child("Levels").child().get()
                                number_of_levels = len(levels.val())
                                print("number_of_levels")
                                print(number_of_levels)
                                my_list = []
                                for i in range(1, number_of_levels + 1):
                                    my_list.append(i)



                                #### my_list[row * 3 + col]
                if (X > width - btn_margin) and (X < width - btn_margin + btn_back_w) and (
                        Y > height - btn_back_h - btn_margin) and (
                        Y < height - btn_margin):

                    state = "main"
                    size_window = (width, height)
                    screen = pygame.display.set_mode(size_window)

                #   находимся в окне выбора уровня


            elif state == "levels":

                name=""
                def draw_lvl(lvl_name):
                    state="level"
                    name = "level " + str(lvl_name)
                    print("tyt'")
                    n = len(db.child("Levels").child(name).child().child("left").get().val()) - 1
                    m = len(db.child("Levels").child(name).child().child("up").get().val()) - 1
                    print("n*m "+str(n)+"   "+str(m))

                    up = db.child("Levels").child(name).child().child("left").get().val()
                    print("up")
                    up.pop(0)
                    print(up)

                    left = db.child("Levels").child(name).child().child("up").get().val()
                    print("left")
                    left.pop(0)
                    print(left)

                    spaces1 = 0

                    for row in range(len(up)):
                        print("str(up[row].count(" "))" + str(up[row].count(" ")))
                        if (str(up[row]).count(" ")) > spaces1:
                            spaces1 = up[row].count(" ")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!up "+str(up[row])+"   "+str(up[row].count(" ")))

                    print("maxUp")
                    spaces1 += 1
                    print(spaces1)
                    maxUp = spaces1

                    spaces2 = 0
                    for row in range(len(left)):
                        print("str(up[row].count(" "))" + str(left[row].count(" ")))
                        if (str(left[row]).count(" ")) > spaces2:
                            spaces2 = left[row].count(" ")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!left " + str(left[row]) + "   " + str(left[row].count(" ")))

                    print("maxLeft")
                    spaces2 += 1
                    print(spaces2)
                    maxLeft = spaces2



                    marginUp = 30
                    marginLeft = 30
                    margin = 5

                    size_num = 60
                    bloc_size = 100
                    ww = 2 * marginUp + maxUp * size_num + m * bloc_size
                    hh = 2 * marginLeft + maxLeft * size_num + n * bloc_size

                    screen = pygame.display.set_mode((ww + 40 + 5 * (m - 3)+ btn_back_w, hh + 40 + 5 * (n - 3)))
                    screen.fill(white)

                    pygame.draw.rect(screen, light_blue,
                                     (ww + 40 + 5 * (m - 3)-(0.5)*marginUp, hh + 40 + 5 * (n - 3) - btn_back_h-marginLeft, btn_back_w, btn_back_h))

                    font = pygame.font.SysFont('stxingkai', 40)

                    text1 = font.render("Вернуться", True, black)
                    text_rect = text1.get_rect()
                    text_x = ww + 40 + 5 * (m - 3)-(0.5)*marginUp+ (btn_back_w) / 2 - text_rect.width / 2
                    text_y = hh + 40 + 5 * (n - 3)-marginLeft - (btn_back_h) / 2 - text_rect.height / 2
                    screen.blit(text1, [text_x, text_y])

                    if state=="level" and (X > width - btn_margin) and (X < width - btn_margin + btn_back_w) and (
                            Y > height - btn_back_h - btn_margin) and (
                            Y < height - btn_margin):
                        state = "main"
                        print("Состояное Меню")

                        size_window = (width, height)
                        screen = pygame.display.set_mode(size_window)

                    pygame.draw.rect(screen, light_grey, (
                        marginLeft, marginUp, ww - 2 * marginLeft + 40 + 5 * (m - 3),
                        hh - 2 * marginUp + 40 + 5 * (n - 3)))
                    # level_1_1=up
                    #print("level_1_1")
                    # print(level_1_1)
                    #print("up")
                    #print(up)
                    res_level_1_1 = transform_to_mass(up, maxUp)

                    print("res_level_1_1")
                    print(res_level_1_1)
                    for row in range(maxUp):
                        for col in range(n):
                            x = row * size_num + (row + 1) * margin + marginUp + 5  # + maxUp * size_num
                            y = col * bloc_size + (col + 1) * margin + maxLeft * size_num + 40 + 5
                            pygame.draw.rect(screen, light_blue, (x, y, size_num, bloc_size))
                            ################
                            font = pygame.font.SysFont('stxingkai', 40)
                            text1 = font.render(res_level_1_1[col][row], True, white)
                            text_rect = text1.get_rect()
                            text_x = (2 * x + size_num) / 2 - text_rect.width / 2
                            text_y = (2 * y + bloc_size) / 2 - text_rect.height / 2
                            screen.blit(text1, [text_x, text_y])
                    # level_1_2 = left
                    print("level_1_2")
                    #print(level_1_2)
                    res_level_1_2 = transform_to_mass(left, maxLeft)
                    print("res_level_1_2")
                    print(res_level_1_2)
                    # print("left")
                    print("!!!!!!!!!!!!!!!!!!!!!!")

                    for row in range(maxLeft):
                        for col in range(m):
                            x = col * bloc_size + (col + 1) * margin + maxUp * size_num + 40 + 5
                            y = row * size_num + (row + 1) * margin + marginUp + 5  # + maxUp * size_num
                            pygame.draw.rect(screen, light_blue, (x, y, bloc_size, size_num))
                            font = pygame.font.SysFont('stxingkai', 40)
                            text1 = font.render(res_level_1_2[col][row], True, white)
                            text_rect = text1.get_rect()
                            text_x = (2 * x + bloc_size) / 2 - text_rect.width / 2
                            text_y = (2 * y + size_num) / 2 - text_rect.height / 2
                            screen.blit(text1, [text_x, text_y])

                    for row in range(n):
                        for col in range(m):
                            x = col * bloc_size + (col + 1) * margin + maxUp * size_num + 40 + 5
                            y = row * bloc_size + (row + 1) * margin + maxLeft * size_num + 40 + 5
                            pygame.draw.rect(screen, white, (x, y, bloc_size, bloc_size))
                            # pygame.draw.rect(screen, green, (marginLeft+maxLeft*size_num+(row)*bloc_size, marginUp+maxUp*size_num+(col)*bloc_size, bloc_size, bloc_size))






                for row in range(3):
                    for col in range(3):
                        x = col * size_block + (col + 1) * margin
                        y = row * size_block + (row + 1) * margin
                        if (X > x) and (X < x + size_block) and (Y > y) and (Y < y + size_block):
                            if (row * 3 + col + 1 <= len(my_list)):
                                print(len(my_list))
                                # print(my_list[row * 3 + col])
                                draw_lvl(my_list[row * 3 + col])
                                level = my_list[row * 3 + col]
                                print("level : "+str(level))
                                state = "level"  # + my_list[row * 3 + col]
                                print("Состояное Уровень")

                                name = "level " + str(level)

                                n = len(db.child("Levels").child(name).child().child("up").get().val()) - 1
                                m = len(db.child("Levels").child(name).child().child("left").get().val()) - 1
                                level_1 = [['0'] * n for i in range(m)]

                                #### my_list[row * 3 + col]
                if (X > width - btn_margin) and (X < width - btn_margin + btn_back_w) and (
                                Y > height - btn_back_h - btn_margin) and (
                                Y < height - btn_margin):
                    state = "main"
                    print("Состояное Меню")

                    size_window = (width, height)
                    screen = pygame.display.set_mode(size_window)


                        # находимя на конкретном уровне



            elif state == "level":
                print("click in level)")
                name = "level " + str(level)

                n = len(db.child("Levels").child(name).child().child("left").get().val()) - 1
                m = len(db.child("Levels").child(name).child().child("up").get().val()) - 1
                # print("n*m "+str(n)+"   "+str(m))
                up = db.child("Levels").child(name).child().child("left").get().val()
                # #print("up")
                up.pop(0)
                # print("!!! "+str(up))
                spaces1 = 0
                for row in range(len(up)):
                    print("string "+str(up[row]))
                    if (str(up[row]).count(" ")) > spaces1:
                        spaces1 = up[row].count(" ")

                # print("spaces1 up  !!!")
                spaces1 += 1
                # print(spaces1)
                maxUp = spaces1

                left = db.child("Levels").child(name).child().child("up").get().val()
                # #print("left")
                left.pop(0)
                # print("!!! " + str(left))
                spaces2 = 0
                for row in range(len(left)):
                    if (str(left[row]).count(" ")) > spaces2:
                        spaces2 = left[row].count(" ")

                # print("maxLeft left  !!!")
                spaces2 += 1
                # print(spaces2)
                maxLeft = spaces2
                #

                #
                #
                #
                marginUp = 30
                marginLeft = 30
                margin = 5
                #maxUp = 2  ###########################################################################################
                #maxLeft = 2  ###########################################################################################
                size_num = 60
                #n = 3  ###########################################################################################
                #m = 3  ###########################################################################################
                bloc_size = 100
                #

                for row in range(n):
                    for col in range(m):
                        x = col * bloc_size + (col + 1) * margin + maxUp * size_num + 40 + 5
                        y = row * bloc_size + (row + 1) * margin + maxLeft * size_num + 40 + 5

                        if (X > x) and (X < x + bloc_size) and (Y > y) and (Y < y + bloc_size):

                            if level_1[row][col] == "1":
                                pygame.draw.rect(screen, white, (x, y, bloc_size, bloc_size))
                                level_1[row][col] = "0"
                                #print(level_1)

                            else:
                                pygame.draw.rect(screen, black, (x, y, bloc_size, bloc_size))
                                level_1[row][col] = "1"
                                #print(level_1)
                # print(level_1)
                sol = db.child("Levels").child(name).child().child("sol").get().val()
                sol.pop(0)
                sol_mas = [['0'] * m for i in range(n)]
                for row in range(n):

                    mystr = sol[row]
                    result = list(map(int, mystr))
                    print("resuuuuuuult")
                    print(str(result))
                    for col in range(m):
                        sol_mas[row][col] = str(result[col])
                print("sol_mas   " + str(sol_mas))
                #check(level_1, up, left)
                if (level_1==sol_mas):
                    print("Побеееееедааааааа!!!!!!!")
                    #раскрасить в зеленый
                    for row in range(n):
                        for col in range(m):
                            x = col * bloc_size + (col + 1) * margin + maxUp * size_num + 40 + 5
                            y = row * bloc_size + (row + 1) * margin + maxLeft * size_num + 40 + 5

                            if level_1[row][col] == "1":
                                pygame.draw.rect(screen, green, (x, y, bloc_size, bloc_size))

                                    # print(level_1)
                            else:
                                pygame.draw.rect(screen, white, (x, y, bloc_size, bloc_size))

                else:
                    for row in range(n):
                        for col in range(m):
                            x = col * bloc_size + (col + 1) * margin + maxUp * size_num + 40 + 5
                            y = row * bloc_size + (row + 1) * margin + maxLeft * size_num + 40 + 5

                            if level_1[row][col] == "1":
                                pygame.draw.rect(screen, black, (x, y, bloc_size, bloc_size))

                                    # print(level_1)
                            else:
                                pygame.draw.rect(screen, white, (x, y, bloc_size, bloc_size))
                marginUp = 30
                marginLeft = 30
                margin = 5

                size_num = 60
                bloc_size = 100
                ww = 2 * marginUp + maxUp * size_num + m * bloc_size
                hh = 2 * marginLeft + maxLeft * size_num + n * bloc_size

                # print("33333333333333333333333333333 " + str(X))
                # print("33333333333333333333333333333 " + str(Y))
                # print("33333333333333333333333333333 " + str(ww + 40 + 5 * (m - 3) - (0.5) * marginUp))
                # print("33333333333333333333333333333 " + str(hh + 40 + 5 * (n - 3) - btn_back_h - marginLeft))
                if (X > ww + 40 + 5 * (m - 3) - (0.5) * marginUp) and (
                        X < ww + 40 + 5 * (m - 3) - (0.5) * marginUp + btn_back_w) and (
                        Y > hh + 40 + 5 * (n - 3) - btn_back_h - marginLeft) and (
                        Y < hh + 40 + 5 * (n - 3) - marginLeft):
                    state = "main"
                    print("Состояное Меню")
                    size_window = (width, height)
                    screen = pygame.display.set_mode(size_window)
            elif state == "edit":

                print("click in edit level)")
                name = "level " + str(level)

                n = len(db.child("Levels").child(name).child().child("left").get().val()) - 1
                m = len(db.child("Levels").child(name).child().child("up").get().val()) - 1
                # print("n*m "+str(n)+"   "+str(m))
                up = db.child("Levels").child(name).child().child("left").get().val()
                # #print("up")
                up.pop(0)
                # print("!!! "+str(up))
                spaces1 = 0
                for row in range(len(up)):
                    print("string "+str(up[row]))
                    if (str(up[row]).count(" ")) > spaces1:
                        spaces1 = up[row].count(" ")

                # print("spaces1 up  !!!")
                spaces1 += 1
                # print(spaces1)
                maxUp = spaces1

                left = db.child("Levels").child(name).child().child("up").get().val()
                # #print("left")
                left.pop(0)
                # print("!!! " + str(left))
                spaces2 = 0
                for row in range(len(left)):
                    if (str(left[row]).count(" ")) > spaces2:
                        spaces2 = left[row].count(" ")

                # print("maxLeft left  !!!")
                spaces2 += 1
                # print(spaces2)
                maxLeft = spaces2
                #

                #
                #
                #
                marginUp = 30
                marginLeft = 30
                margin = 5
                #maxUp = 2  ###########################################################################################
                #maxLeft = 2  ###########################################################################################
                size_num = 60
                #n = 3  ###########################################################################################
                #m = 3  ###########################################################################################
                bloc_size = 100
                #


                # check(level_1, up, left)
                # if (level_1 == sol_mas):
                #     print("Побеееееедааааааа!!!!!!!")


                print("sol_mas!!!!!!!!!!")
                print(sol_mas)
                for row in range(n):
                    for col in range(m):
                        x = col * bloc_size + (col + 1) * margin + maxUp * size_num + 40 + 5
                        y = row * bloc_size + (row + 1) * margin + maxLeft * size_num + 40 + 5

                        if (X > x) and (X < x + bloc_size) and (Y > y) and (Y < y + bloc_size):

                            if sol_mas[row][col] == "1":
                                pygame.draw.rect(screen, white, (x, y, bloc_size, bloc_size))
                                sol_mas[row][col] = "0"
                                # print(level_1)

                            else:
                                pygame.draw.rect(screen, black, (x, y, bloc_size, bloc_size))
                                sol_mas[row][col] = "1"
                                # print(level_1)
                # print(level_1)

                marginUp = 30
                marginLeft = 30
                margin = 5

                size_num = 60
                bloc_size = 100
                ww = 2 * marginUp + maxUp * size_num + m * bloc_size
                hh = 2 * marginLeft + maxLeft * size_num + n * bloc_size

                # print("33333333333333333333333333333 " + str(X))
                # print("33333333333333333333333333333 " + str(Y))
                # print("33333333333333333333333333333 " + str(ww + 40 + 5 * (m - 3) - (0.5) * marginUp))
                # print("33333333333333333333333333333 " + str(hh + 40 + 5 * (n - 3) - btn_back_h - marginLeft))
                if (X > ww + 40 + 5 * (m - 3) - (0.5) * marginUp) and (
                        X < ww + 40 + 5 * (m - 3) - (0.5) * marginUp + btn_back_w) and (
                        Y > hh + 40 + 5 * (n - 3) - btn_back_h - marginLeft) and (
                        Y < hh + 40 + 5 * (n - 3) - marginLeft):
                    state = "main"
                    print("Состояное Меню")
                    size_window = (width, height)
                    screen = pygame.display.set_mode(size_window)
                if (X > ww + 40 + 5 * (m - 3) - (0.5) * marginUp) and (
                        X < ww + 40 + 5 * (m - 3) - (0.5) * marginUp + btn_back_w) and (
                        Y > hh / 2 + btn_back_h) and (
                        Y < hh / 2 + 2*btn_back_h):
                    print("WHICH LEVEL")
                    print(name)
                    UpdateMas(sol_mas, name)
                    state = "main"
                    print("Сохранено")

        # print("state = " + str(state))



    if state == "main":
        # print("Состояное МЕНЮ")
        draw_main()

    elif state == "change":
        draw_changing()


    pygame.display.update()
