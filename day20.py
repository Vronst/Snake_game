import turtle
import time
from snakeclass import Snake
from food import Food
from scoreboard import Scoreboard

screen = turtle.Screen()
# harold = turtle.Turtle("square")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Hungry Snake")
screen.tracer(0)
# harold.color("green")
# snakes = []
# x = 0
# for _ in range(3):
#     s = turtle.Turtle("square")
#     s.penup()
#     s.color("green")
#     s.setpos(x, 0)
#     snakes.append(s)
#     x -= 20
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Snake eats and grows.
    if snake.head.distance(x=food.xcor(), y=food.ycor()) < 15:
        food.refresh()
        snake.grow()
        scoreboard.score_up()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # scoreboard.game_over()
        # game_is_on = False
        scoreboard.reset()
        snake.reset()
    # Detect collision with tail.
    for one in snake.snakes[1:]:
        # if one == snake.head:
        #     pass
        if snake.head.distance(one) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
