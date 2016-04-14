#!/usr/bin/python

def main():
    running = True
    year = 2001
    counter = 0
    
    while running == True:
        try:
            if year >= 2001 and year < 2007:
                print "The were signed to Lookout Records"
            elif year >= 2007 and year < 2010:
                print "The were signed to Touch and Go Records"
            elif year >= 2010 < 2016:
                print "They were signed to Matador Records"
            else:
                print "They were unsigned"
        except:
            print "Something went wrong"
            
        counter = counter + 1
        
        if counter > 0:
            running = False

if __name__ == "__main__":
    main()