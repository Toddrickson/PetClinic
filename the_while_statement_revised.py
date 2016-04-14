miles_run = 0
miles_ran = 108
total_miles = 108
running = True
first_speed = 1
second_speed = 2

while running:
    if miles_run <=  total_miles:
        print("You\'re doing great! #1 You\'re on  On mile {}".format(miles_run))
        print("You\'re doing great! #2 You\'re on  On mile {}".format(miles_ran))
        miles_run +=1
        miles_ran -=2

    else:
        running = False