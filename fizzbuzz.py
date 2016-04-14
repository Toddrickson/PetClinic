import sys

try: 
    user_input = raw_input("Enter the upper limit for fuzzbuzz: ")
    input = int(user_input)

    for i in range(0, input):
        if i % 3 == 0:
            print str(i) + " fizz"
        elif i % 5 == 0:
            print str(i) + " buzz"
        else:
            print str(i) + " woof"

except:
    print "You failed to enter an upper limit please run Fizz Buzz again."

