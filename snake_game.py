from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()
#detect wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() < -295 or snake.head.ycor() > 295:
        scoreboard.reset_high_score()
        snake.reset()

#detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass

        elif snake.head.distance(segment) < 10:
            scoreboard.reset_high_score()
            snake.reset()





screen.exitonclick()