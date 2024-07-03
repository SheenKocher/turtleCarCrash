import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
car_manager = CarManager()
screen.onkey(player.go_up,"Up")
scoreboard = Scoreboard()
scoreboard.update_scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    #detecting collision with cars

    for car in car_manager.all_cars:
        if car.distance(player)<20:
            player.color("red")
            screen.update()
            scoreboard.game_over()
            game_is_on = False

    #detect sucessfull crossing
    if player.is_at_finishline():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()




screen.exitonclick()

