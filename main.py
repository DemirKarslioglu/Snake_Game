import time
from turtle import Screen
from snake import Snake
from apple import Apple
from score import ScoreText

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("LightBlue2")
screen.title("Yılan Oyunu")
screen.tracer(0)

snake = Snake()
apple = Apple()
score_text = ScoreText()

game = True


def play_again():
    soru = screen.textinput(title="Do You Want To Restart?", prompt="Do You Want To Restart?(Yes - No)")
    if soru == "Yes":
        global oyun
        oyun = True
        for i in range(snake.counter):
            snake.parts[-1].hideturtle()
            snake.parts.pop(-1)
        snake.counter = 0
        snake.head.goto(0, 0)
        score_text.clear()
        score_text.goto(0, 260)
        score_text.score = 0
        score_text.update_score()
        apple.update()
        screen.update()
    else:
        oyun = False


while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()

    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")

    if snake.head.distance(apple) < 15:
        apple.update()
        snake.enlarge()
        score_text.increase_score()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        oyun = False
        score_text.game_over()
        play_again()

    for parca in snake.parts[1:]:
        if snake.head.distance(parca) < 10:
            oyun = False
            score_text.game_over()

screen.bye()
