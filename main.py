import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.title("Turtle Crossing")
    return screen


def play_game():
    screen = setup_screen()
    player = Player()
    manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(fun=player.move, key="Up")

    game_is_on = True
    while game_is_on:
        manager.generate()

        time.sleep(0.1)
        manager.move()
        screen.update()
        for car in manager.car_list:
            if player.distance(car) < 20:
                game_is_on = False
                scoreboard.game_over()

        if player.reached_end():
            player.restart()
            manager.increase_speed()
            scoreboard.advance_level()
    screen.exitonclick()


play_game()
