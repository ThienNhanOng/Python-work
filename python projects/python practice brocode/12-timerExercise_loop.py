#this exercise will practice loops and create a countdown 

import time #this will import the time function in python

#this example is that after 3 seconds the prompt will show up saying times up
time.sleep(2)
print("times up!")

#this loop exercise will allow users to interact and set a timer
mytime = int(input("enter the stopwatch time in seconds"))
for x in range(0, mytime):
    print(x)
    time.sleep(1)
print("timer is done!")

#this loop will allow the timer to count backwards
mytime2 = int(input("enter the stopwatch time in seconds and clock time "))
for x in range(mytime2, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"00:00:{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("times up")

