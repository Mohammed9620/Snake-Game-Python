from turtle import Screen
import time
from snake_1 import Snake
from food import Food
from score_record import Score

score=Score()
snake=Snake()
food=Food()

score.update_record()
screen=Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.control_right,"Right")
screen.onkey(snake.control_left,"Left")
screen.onkey(snake.control_up,"Up")
screen.onkey(snake.control_down,"Down")


game_is_on = True

while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)
    if snake.segments[0].distance(food) <15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    # Test if there is a collision with wall
    if snake.segments[0].xcor() > 285 or snake.segments[0].xcor() < -285 or snake.segments[0].ycor() > 285 or \
            snake.segments[0].ycor() < -285:
        game_is_on=False
        score.game_over()

    # Test if there is a collision with tail
    for segment in snake.segments:
        if segment== snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on = False
            score.game_over()

screen.exitonclick()