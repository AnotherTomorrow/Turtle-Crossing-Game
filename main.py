import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.move_speed)
    screen.update()
    car_manager.new_car()
    car_manager.car_move()

    # Checks to see if a car hits the player
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Increases the level if player passes it
    if player.ycor() > 280:
        player.player_reset()
        scoreboard.track_score()

screen.exitonclick()
