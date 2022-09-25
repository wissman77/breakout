import turtle
import random

# initial constants for cfreating breaks
X_INCREAMENT = 44
Y_INCREAMENT = 22
INITIAL_X = -310
INITIAL_Y = 230

x_move = 0
y_move = 0
score = 0
lives = 3


# creating all breaks instances and return a list
def create_breaks():
    colors = ('red', 'red', 'orange', 'orange', 'green', 'green', 'yellow', 'yellow')
    breaks = []
    x = 0
    y = 0
    for color in colors:
        for _ in range(15):
            t = turtle.Turtle('square')
            t.up()
            t.goto(INITIAL_X + x, INITIAL_Y + y)
            t.color(color)
            t.shapesize(stretch_wid=1, stretch_len=2.1)
            x += X_INCREAMENT
            breaks.append(t)
        x = 0
        y -= Y_INCREAMENT
    return breaks


# creating a player instance
def create_player():
    t = turtle.Turtle('square')
    t.up()
    t.speed(0)
    t.goto(0, -270)
    t.color('blue')
    t.shapesize(stretch_wid=1, stretch_len=5)
    return t


# creating a ball instance
def create_ball():
    global x_move, y_move
    t = turtle.Turtle('circle')
    t.up()
    t.goto(0, 0)
    t.color('white')
    t.shapesize(stretch_wid=0.7, stretch_len=0.7)
    x_move = random.choice((4, 5, 6, 7, 8))
    y_move = random.choice((4, 5, 6, 7, 8))
    return t


# creating a score label instance
def create_score():
    t = turtle.Turtle()
    t.hideturtle()
    t.up()
    t.goto(240, 270)
    t.color('white')
    return t


# creating a lives label instance
def create_lives():
    t = turtle.Turtle()
    t.hideturtle()
    t.up()
    t.goto(-330, 270)
    t.color('white')
    return t


# moving the player paddle left
def player_left():
    if player.xcor() > -270:
        player.setx(player.xcor() - 72)


# moving the player paddle left
def player_right():
    if player.xcor() < 270:
        player.setx(player.xcor() + 72)


# increase speed every 10 breaks 
def increase_speed():
    global x_move, y_move
    if score % 100 == 0 and score != 0:
        if x_move < 0:
            x_move -= 1
        else:
            x_move += 1

        if y_move < 0:
            y_move -= 1
        else:
            y_move += 1

# game logic
def play_game():
    global x_move, y_move, score, lives, ball
    score_t.clear()
    lives_t.clear()
    score_t.write(f'score: {score}', font=('Arial', 13, 'normal'))
    lives_t.write(f"Lives: {lives}", font=('Arial', 13, 'normal'))
    ball.goto(ball.xcor() - x_move, ball.ycor() - y_move)
    ball.clear()
    

    # collision with player paddle
    if ball.xcor() >= player.xcor() - 50 and ball.xcor() <= player.xcor() + 50 and ball.ycor() <= player.ycor():
        y_move *= -1
    
    # collision with walls
    if ball.xcor() <= -325 and ball.ycor() > -290 or ball.xcor() >= 320 and ball.ycor() > -290:
        x_move *= -1

    # collision with roof
    if ball.ycor() >= 270:
        y_move *= -1

    if ball.ycor() < -310:
        ball.reset()
        lives -= 1
        lives_t.clear()
        ball = create_ball()

    # collision with breaks
    for index, a_break in enumerate(breaks):
        if ball.ycor() >= a_break.ycor() - 20 and ball.xcor() >= a_break.xcor() -20 and ball.xcor() <= a_break.xcor() + 20:
            # add score
            score_t.clear()
            score += 10
            increase_speed()
            a_break.reset()
            del breaks[index]
            y_move *= -1

screen = turtle.Screen()
screen.tracer(False)
screen.bgcolor('black')
breaks = create_breaks()
player = create_player()
ball = create_ball()
score_t = create_score()
lives_t = create_lives()

screen.listen()
screen.onkey(player_right, 'Right')
screen.onkey(player_left, 'Left')


is_on = True
is_winner = False

while is_on:
    screen.update()
    play_game()
    if lives == 0:
        is_on = False
    # 3 breaks left is winning state 
    if len(breaks) == 3:
        is_winner = True
        is_on = False

finnish_t = turtle.Turtle()
if is_winner:
    finnish_t.color('green')
    finnish_t.write('YOU WON!', align='center', font=('Arial', 50, 'normal'))
else:
    finnish_t.color('red')
    finnish_t.write('GAME OVER!', align='center', font=('Arial', 50, 'normal'))
turtle.done()