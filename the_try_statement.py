import sys

phone_phone_book = {"Sarah Hughes": "01234 567890",
                    "Tim Taylor"  : "02345 678901",
                    "Sam Smith"   : "03456 789694"}
                    
try:
    jamie = phone_phone_book["Jamie Theakston"]
except:
    print "Error:", sys.exc_info()[0] 
    print "Jamie Theakston is not listed"