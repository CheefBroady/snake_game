from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


game_is_on = True
sleep_time = 0.5
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # 0 stands for 'off', the screen is not going to be refreshed; it needs 'screen.update()' \
# to refresh the screen manually


snake = Snake(shape="square", color="white", length=3)
food = Food()
food.refresh()
scoreboard = Scoreboard()

screen.listen()  # set focus on TurtleScreen in order to collect key-events
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


counter = 0
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    # if counter == 9:
    #     game_is_on = False
    #     counter += 1
    snake.move_snake()
    # print(f"Länge des Arrays: {len(snake.snake_segments)}")

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()
        sleep_time -= 0.02

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.snake_segments[1:]:
        # if head collides with any segment in the tail:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()