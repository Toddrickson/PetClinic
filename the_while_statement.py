miles_run = 0
total_miles = 108
running = True
first_speed = 1
second_speed = 2

while running:
    if miles_run <=  total_miles:
        print("You\'re going great! #1 You\'re on  On mile {}".format(miles_run*first_speed))
        print("You\'re going great! #2 You\'re on  On mile {}".format(miles_run*second_speed))
        miles_run +=1
    else:
        running = False
        

        
           