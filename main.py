import turtle
from time import sleep


def exi_t():
    print("you pressed q -> quit")      #q for exit the program
    exit()


def match():
    # matching rows,column diagonal to determine winner and game-over
    if(l[0][0] == l[0][1] and l[0][1] == l[0][2] == 'X') or (l[1][0] == l[1][1] and l[1][0] == l[1][2] == 'X') or (l[2][0] == l[2][1] and l[2][1] == l[2][2] == 'X'):
        pen.goto(-150, 300)
        pen.write("GAME Over Player 1 Won!!!!", font="Courier 20 normal")
        sleep(2.5)
        exit()
    elif(l[0][0] == l[1][0] and l[1][0] == l[2][0] == 'X') or (l[0][1] == l[1][1] and l[1][1] == l[2][1] == 'X') or (l[0][2] == l[1][2] and l[1][2] == l[2][2] == 'X'):
        pen.goto(0, 300)
        pen.write("GAME Over Player 1 Won!!!!", font="Courier 20 normal")
        sleep(2.5)
        exit()
    elif(l[0][0] == l[1][1] and l[1][1] == l[2][2] == 'X') or (l[0][2] == l[1][1] and l[1][1] == l[2][0] == 'X'):
        pen.goto(0, 300)
        pen.write("GAME Over Player 1 Won!!!!", font="Courier 20 normal")
        sleep(2.5)
        exit()
    elif(l[0][0] == l[0][1] and l[0][1] == l[0][2] == 'O') or (l[1][0] == l[1][1] and l[1][0] == l[1][2] == 'O') or (l[2][0] == l[2][1] and l[2][1] == l[2][2] == 'O'):
        pen.goto(-150, 300)
        pen.write("GAME Over Player 2 Won!!!", font="Courier 20 normal")
        sleep(2.5)
        exit()
    elif(l[0][0] == l[1][0] and l[1][0] == l[2][0] == 'O') or (l[0][1] == l[1][1] and l[1][1] == l[2][1] == 'O') or (l[0][2] == l[1][2] and l[1][2] == l[2][2] == 'O'):
        pen.goto(0, 300)
        pen.write("GAME Over Player 2 Won!!!", font="Courier 20 normal")
        sleep(2.5)
        exit()
    elif(l[0][0] == l[1][1] and l[1][1] == l[2][2] == 'O') or (l[0][2] == l[1][1] and l[1][1] == l[2][0] == 'O'):
        pen.goto(0, 300)
        pen.write("GAME Over Player 2 Won!!!", font="Courier 20 normal")
        sleep(2.5)
        exit()
        
    elif(count == 9):
        pen.goto(0, 300)#if count is 9 and none of above is true then it's a draw
        pen.write("It's A Draw", font="Courier 20 normal")
        sleep(2.5)
        exit()


def click(x, y):
    move = False    #to determine a valid move
    global count, string, l
    if(x >= -245 and x <= -105) and (y >= 85 and y <= 215):
        i = 0
        j = 0   #respective position according to mouse click x-> xcor y-> ycor of curser
        pen.goto(-205, 90)
        if(l[i][j] == ''):
            move = True
            l[i][j] = string
            count += 1
            pen.write(string, font="courier 80 normal")
    elif(x >= -71 and x <= 70) and (y >= 85 and y <= 215):
        i = 0
        j = 1
        pen.goto(-30, 90)
        if(l[i][j] == ''):
            move = True
            l[i][j] = string
            count += 1
            pen.write(string, font="courier 80 normal")
    elif(x >= 100 and x <= 239) and (y >= 85 and y <= 215):
        i = 0
        j = 2
        pen.goto(140, 90)
        if(l[i][j] == ''):
            move = True
            l[i][j] = string
            count += 1
            pen.write(string, font="courier 80 normal")
    elif(x >= -245 and x <= -105) and (y >= -69 and y <= 61):
        i = 1
        j = 0
        pen.goto(-205, -60)
        if(l[i][j] == ''):
            move = True
            l[i][j] = string
            count += 1
            pen.write(string, font="courier 80 normal")
    elif(x >= -71 and x <= 70) and (y >= -69 and y <= 61):
        i = 1
        j = 1
        pen.goto(-30, -60)
        if(l[i][j] == ''):
            move = True
            l[i][j] = string
            count += 1
            pen.write(string, font="courier 80 normal")
    elif(x >= 100 and x <= 239) and (y >= -69 and y <= 61):
        i = 1
        j = 2
        pen.goto(140, -60)
        if(l[i][j] == ''):
            move = True
            l[i][j] = string
            count += 1
            pen.write(string, font="courier 80 normal")
    elif(x >= -245 and x <= -105) and (y >= -225 and y <= 89):
        i = 2
        j = 0
        pen.goto(-205, -210)
        if(l[i][j] == ''):
            move = True
            l[i][j] = string
            count += 1
            pen.write(string, font="courier 80 normal")
    elif(x >= -71 and x <= 70) and (y >= -225 and y <= 89):
        i = 2
        j = 1
        pen.goto(-30, -210)
        if(l[i][j] == ''):
            move = True
            l[i][j] = string
            count += 1
            pen.write(string, font="courier 80 normal")
    elif(x >= 100 and x <= 239) and (y >= -225 and y <= 89):
        i = 2
        j = 2
        pen.goto(140, -210)
        if(l[i][j] == ''):
            move = True
            l[i][j] = string
            count += 1
            pen.write(string, font="courier 80 normal")
    if(string == "X" and move):
        string = "O"
    elif(string == 'O' and move):
        string = "X"
    match()


if __name__ == "__main__":
    count = 0
    string = "X"
    color = input("Enter Color of pen should be valid like red,blue:-> ")
    l = [['', '', ''], ['', '', ''], ['', '', '']]
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    try:
        pen.color(color)
    except:
        print("Invalid Color!!!!!!")
        pen.color("black")  #default is black color
    pen.up()
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.bgpic("board.gif")
    wn.setup(850, 750)
    wn.listen()
    wn.onclick(click, 1)
    wn.onkeypress(exi_t, 'q')

    turtle.mainloop()
