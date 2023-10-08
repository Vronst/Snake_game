import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for _ in STARTING_POSITIONS:
            self.growth(_)
            # s = turtle.Turtle("square")
            # s.speed(6)
            # s.penup()
            # s.color("green")
            # s.goto(_)
            # self.snakes.append(s)

    def move(self):
        for segment in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[segment - 1].xcor()
            new_y = self.snakes[segment - 1].ycor()
            self.snakes[segment].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snakes[0].setheading(RIGHT)

    def growth(self, pos):
        s = turtle.Turtle("square")
        s.speed(6)
        s.penup()
        s.color("green")
        s.goto(pos)
        self.snakes.append(s)

    def grow(self):
        self.growth(self.snakes[-1].pos())

    def reset(self):
        for _ in self.snakes:
            _.goto(800, 800)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]
        self.head.home()
