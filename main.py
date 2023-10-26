import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
from draw import Draw

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("grey")
screen.listen()

# Create the object of the player
me = Player()

# Call the car manager class
my_car_manager = CarManager()
my_car_manager.hideturtle()

# Create the initial wall of cars
# all_cars = []
# all_ys = [-240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140,
#           160, 180, 200, 220, 240, ]
# chosen_positions = []
# for car_index in range(15):
#     car = CarManager()
#     random_y = random.choice(all_ys)
#     while random_y in chosen_positions:
#         random_y = random.choice(all_ys)
#     chosen_positions.append(random_y)
#     random_x = random.uniform(150, 300)
#     car.setx(random_x)
#     car.sety(random_y)
#     all_cars.append(car)

# Create the second wall
# all_ys = [-240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140,
#           160, 180, 200, 220, 240, ]
# chosen_positions.clear()
# chosen_positions = []
# for car_index in range(15):
#     car = CarManager()
#     random_y = random.choice(all_ys)
#     while random_y in chosen_positions:
#         random_y = random.choice(all_ys)
#     chosen_positions.append(random_y)
#     random_x = random.randint(0, 150)
#     car.setx(random_x)
#     car.sety(random_y)
#     all_cars.append(car)

# Create the third wall
# all_ys = [-240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140,
#           160, 180, 200, 220, 240, ]
# chosen_positions.clear()
# chosen_positions = []
# for car_index in range(15):
#     car = CarManager()
#     random_y = random.choice(all_ys)
#     while random_y in chosen_positions:
#         random_y = random.choice(all_ys)
#     chosen_positions.append(random_y)
#     random_x = random.uniform(-300, -100)
#     car.setx(random_x)
#     car.sety(random_y)
#     all_cars.append(car)

# Create the lines with Drawey
drawey = Draw()
drawey.draw_lines()

# Create the scoreboard
scorey = Scoreboard()
scorey.setup()

# Run the game
screen.onkeypress(me.move_up, "Up")
screen.onkeypress(me.move_down, "Down")
screen.onkeypress(me.move_left, "Left")
screen.onkeypress(me.move_right, "Right")

game_is_on = True
frame = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    my_car_manager.create_cars()
    my_car_manager.move_cars()
    # When the turt crosses the road
    if me.ycor() >= 265:
        print("You made it!")
        me.next_level()
        scorey.player_1_score += 1
        scorey.setup()
        my_car_manager.level_up()

    # Move the cars
    for drivers in my_car_manager.all_cars:
        # rand_distance = random.randint(difficulty, 0)
        # drivers.forward(rand_distance)
        if drivers.distance(me) < 20:
            print("You got smooshed")
            scorey.game_over()
            game_is_on = False
        if drivers.xcor() <= -300:
            random_x = random.randint(300, 350)
            drivers.setx(random_x)

screen.exitonclick()
