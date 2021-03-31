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

n = 3
m = 3
level_1 = [['0'] * n for i in range(m)]
#level_1_1 = ["1 1", "1","1 1"]  ###########################################################################################
#level_1_2 = ["1 1", "1",
#             "1 1"]  ###########################################################################################

pygame.init()

width = height = 350

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Game1")

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

h1 = 70
w1 = 200
ots_up = 70
margin = 25
size_block = (width - 4 * margin) / 3
state = "main"

levels = db.child("Levels").child().get()
number_of_levels = len(levels.val())
my_list = []
for i in range(1, number_of_levels + 1):
    my_list.append(i)


def transform_to_mass(mas, maxUp):
    qwe = [[0] * maxUp for i in range(len(mas))]
    for col in range(len(mas)):
        string = mas[col]
        while 2 * maxUp - 1 != len(string):
            if 2 * maxUp - 1 > len(string):
                string = "0 " + string
        result = string.split(" ")
        qwe[col] = result

    return qwe


def check(mas, numbers_up, numbers_left):
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
        # print(string.strip())
        if string.strip() != numbers_up[row]:
            check1 = False

    # print('      1 ' + str(check1))

    check2 = True

    for row in range(len(mas)):
        s = 0
        string = ''
        pause = False
        for col in range(len(mas[0])):
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
        # print(string.strip())
        if string.strip() != numbers_left[row]:
            check2 = False

    # print('      2 ' + str(check2))

    if check1 and check2:
        print("Е бои!!! Мои поздравения!!!")


def draw_main():
    screen.fill(black)
    pygame.draw.rect(screen, white, ((width - w1) // 2, ots_up, w1, h1))
    pygame.draw.rect(screen, white, ((width - w1) // 2, ots_up * 2 + h1, w1, h1))

    font = pygame.font.SysFont('stxingkai', 50)
    text1 = font.render("Играть", True, black)
    text_rect = text1.get_rect()
    text_x = width / 2 - text_rect.width / 2
    text_y = ots_up + h1 / 2 - text_rect.height / 2
    screen.blit(text1, [text_x, text_y])

    font = pygame.font.SysFont('stxingkai', 50)
    text2 = font.render("Изменить", True, black)
    text_rect = text2.get_rect()
    text_x = width / 2 - text_rect.width / 2
    text_y = ots_up + h1 / 2 + h1 + ots_up - text_rect.height / 2
    screen.blit(text2, [text_x, text_y])


def draw_levels():
    screen.fill(black)

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
                text1 = font.render("?", True, black)
            text_rect = text1.get_rect()
            text_x = x + size_block / 2 - text_rect.width / 2
            text_y = y + size_block / 2 - text_rect.height / 2
            screen.blit(text1, [text_x, text_y])


# level_1 = [['0'] * n for i in range(m)]
while True:
    for event in pygame.event.get():  # пока идет игра
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:  # если нажата кнопка мыши
            x_mouse, y_mouse = pygame.mouse.get_pos()
            X = x_mouse
            Y = y_mouse
            # print(str(X)+" "+str(Y))

            # пока находимся в меню можем клацнуть на кнопку играть
            if state == "main" and (X > (width - w1) // 2) and (X < (width - w1) // 2 + w1) and (Y > ots_up) and (
                    Y < ots_up + h1):
                # print("btn1")
                state = "levels"
                draw_levels()
                # пока находимся в меню можем клацнуть на кнопку изменить   (добавить уровень или удаить его)
            elif state == "main" and (X > (width - w1) // 2) and (X < (width - w1) // 2 + w1) and (
                    Y > ots_up * 2 + h1) and (
                    Y < ots_up * 2 + h1 + h1):
                # print("btn2")
                state = "st2"
                screen.fill(black)

                #   находимся в окне выбора уровня
            elif state == "levels":

                def draw_lvl(lvl_name):

                    name = "level " + str(lvl_name)

                    n = len(db.child("Levels").child(name).child().child("up").get().val()) - 1
                    m = len(db.child("Levels").child(name).child().child("left").get().val()) - 1

                    up = db.child("Levels").child(name).child().child("up").get().val()
                    print("up")
                    up.pop(0)
                    print(up)
                    spaces1 = 0
                    for row in range(len(up)):
                        if (str(up[row]).count(" ")) > spaces1:
                            spaces1 = up[row].count(" ")

                    print("spaces1")
                    spaces1 += 1
                    print(spaces1 + 1)
                    maxUp = spaces1

                    spaces2 = 0
                    for row in range(len(up)):
                        if (str(up[row]).count(" ")) > spaces2:
                            spaces2 = up[row].count(" ")

                    print("spaces1")
                    spaces2 += 1
                    print(spaces2 + 1)
                    maxLeft = spaces2

                    left = db.child("Levels").child(name).child().child("left").get().val()
                    print("left")
                    left.pop(0)
                    print(left)

                    marginUp = 30
                    marginLeft = 30
                    margin = 5

                    size_num = 60
                    bloc_size = 100
                    ww = 2 * marginUp + maxLeft * size_num + m * bloc_size
                    hh = 2 * marginLeft + maxUp * size_num + n * bloc_size
                    screen = pygame.display.set_mode((ww + 40 + 5 * (m - 3), hh + 40 + 5 * (n - 3)))
                    screen.fill(black)
                    pygame.draw.rect(screen, white, (
                        marginLeft, marginUp, ww - 2 * marginLeft + 40 + 5 * (m - 3),
                        hh - 2 * marginUp + 40 + 5 * (n - 3)))
                    #level_1_1=up
                    print("level_1_1")
                    #print(level_1_1)
                    print("up")
                    print(up)
                    res_level_1_1 = transform_to_mass(up, maxUp)

                    print("res_level_1_1")
                    # print(res_level_1_1)
                    for row in range(maxUp):
                        for col in range(n):
                            x = row * size_num + (row + 1) * margin + marginUp + 5  # + maxUp * size_num
                            y = col * bloc_size + (col + 1) * margin + maxLeft * size_num + 40 + 5
                            pygame.draw.rect(screen, green, (x, y, size_num, bloc_size))
                            ################
                            font = pygame.font.SysFont('stxingkai', 40)
                            text1 = font.render(res_level_1_1[col][row], True, white)
                            text_rect = text1.get_rect()
                            text_x = (2 * x + size_num) / 2 - text_rect.width / 2
                            text_y = (2 * y + bloc_size) / 2 - text_rect.height / 2
                            screen.blit(text1, [text_x, text_y])
                    #level_1_2 = left
                    print("level_1_2")
                    #print(level_1_2)
                    res_level_1_2 = transform_to_mass(left, 2)
                    #print("res_level_1_2")
                    #print(res_level_1_2)
                    #print("left")
                    #print(left)
                    for row in range(maxLeft):
                        for col in range(m):
                            x = col * bloc_size + (col + 1) * margin + maxLeft * size_num + 40 + 5
                            y = row * size_num + (row + 1) * margin + marginUp + 5  # + maxUp * size_num
                            pygame.draw.rect(screen, black, (x, y, bloc_size, size_num))
                            font = pygame.font.SysFont('stxingkai', 40)
                            text1 = font.render(res_level_1_2[col][row], True, white)
                            text_rect = text1.get_rect()
                            text_x = (2 * x + bloc_size) / 2 - text_rect.width / 2
                            text_y = (2 * y + size_num) / 2 - text_rect.height / 2
                            screen.blit(text1, [text_x, text_y])

                    for row in range(n):
                        for col in range(m):
                            x = col * bloc_size + (col + 1) * margin + maxLeft * size_num + 40 + 5
                            y = row * bloc_size + (row + 1) * margin + maxUp * size_num + 40 + 5
                            pygame.draw.rect(screen, red, (x, y, bloc_size, bloc_size))
                            # pygame.draw.rect(screen, green, (marginLeft+maxLeft*size_num+(row)*bloc_size, marginUp+maxUp*size_num+(col)*bloc_size, bloc_size, bloc_size))


                for row in range(3):
                    for col in range(3):
                        x = col * size_block + (col + 1) * margin
                        y = row * size_block + (row + 1) * margin
                        if (X > x) and (X < x + size_block) and (Y > y) and (Y < y + size_block):
                            if (row * 3 + col + 1 <= len(my_list)):
                                # print(my_list[row * 3 + col])
                                draw_lvl(my_list[row * 3 + col])
                                state = "level"  # + my_list[row * 3 + col]
                                level = my_list[row * 3 + col]
                                #### my_list[row * 3 + col]
                        # находимя на конкретном уровне
            elif state == "level":
                print("123123")
                # name = "level " + str(level)
                #
                # n = len(db.child("Levels").child(name).child().child("up").get().val()) - 1
                # m = len(db.child("Levels").child(name).child().child("left").get().val()) - 1
                #
                # up = db.child("Levels").child(name).child().child("up").get().val()
                # #print("up")
                # up.pop(0)
                # #print(up)
                # spaces1 = 0
                # for row in range(len(up)):
                #     if (str(up[row]).count(" ")) > spaces1:
                #         spaces1 = up[row].count(" ")
                #
                # #print("spaces1")
                # spaces1 += 1
                # #print(spaces1 + 1)
                # maxUp = spaces1
                #
                # spaces2 = 0
                # for row in range(len(up)):
                #     if (str(up[row]).count(" ")) > spaces2:
                #         spaces2 = up[row].count(" ")
                #
                # #print("spaces1")
                # spaces2 += 1
                # #print(spaces2 + 1)
                # maxLeft = spaces2
                #
                # left = db.child("Levels").child(name).child().child("left").get().val()
                # #print("left")
                # left.pop(0)
                # #print(left)
                #
                #
                #
                # marginUp = 30
                # marginLeft = 30
                # margin = 5
                # #maxUp = 2  ###########################################################################################
                # #maxLeft = 2  ###########################################################################################
                # size_num = 60
                # #n = 3  ###########################################################################################
                # #m = 3  ###########################################################################################
                # bloc_size = 100
                #
                # for row in range(n):
                #     for col in range(m):
                #         x = col * bloc_size + (col + 1) * margin + maxLeft * size_num + 40 + 5
                #         y = row * bloc_size + (row + 1) * margin + maxUp * size_num + 40 + 5
                #         if (X > x) and (X < x + bloc_size) and (Y > y) and (Y < y + bloc_size):
                #             if level_1[row][col] == "1":
                #                 pygame.draw.rect(screen, red, (x, y, bloc_size, bloc_size))
                #                 level_1[row][col] = "0"
                #                 #print(level_1)
                #
                #             else:
                #                 pygame.draw.rect(screen, black, (x, y, bloc_size, bloc_size))
                #                 level_1[row][col] = "1"
                #                 #print(level_1)
                # check(level_1, up, left)

    if state == "main":
        draw_main()

    pygame.display.update()
