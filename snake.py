from turtle import Turtle
import random
EDGE_WIDE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, shape, color, length):
        self.shape = shape
        self.color = color
        self.length = length
        self.snake_segments = []
        self.__create_snake()
        self.head = self.snake_segments[0]

    def __create_snake(self):
        for n in range(self.length):
            new_snake_segment = self.__add_segment(position=(n * -EDGE_WIDE, 0))
            self.snake_segments.append(new_snake_segment)
            print(self.snake_segments)

    def __add_segment(self, position):
        snake = Turtle()
        snake.reset()
        snake.penup()
        snake.color(self.color)
        snake.shape(name=self.shape)
        snake.goto(position)
        return snake

    def move_snake(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.head.forward(EDGE_WIDE)

    def extend_snake(self):
        new_snake_segment = self.__add_segment(self.snake_segments[-1].position())
        self.snake_segments.append(new_snake_segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)