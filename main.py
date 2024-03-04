from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import scoreboard



screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game ")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


starting_position=[(0,0),(-20,0),(-40,0)]

segments=[]



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    if snake.head.xcor()>280  or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.xcor() < -280:
        game_is_on=False
        scoreboard.game_over()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()







screen.exitonclick()
