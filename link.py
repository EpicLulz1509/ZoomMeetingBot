from datetime import datetime as dt

day = dt.today().strftime("%A")
print("Today is: " + day)

now = dt.now().strftime("%H:%M")
print("Time is: " + now)

ID = ""
PASS = ""

def check():
    n = 10
    while(n!=0):

        hr = int(dt.now().strftime("%H"))
        min = int(dt.now().strftime("%M"))

        total = (hr*60) + min
        print(total)
        total_join = (hr_join*60) + min_join
        print(total_join)
        time_left = total_join - total

        if(time_left < 15):
            print("Class starting....")
            n = 0
            return True

        elif(time_left > 15 & time_left < 60):
            print("Waiting for class to start in: " + time_left + " mins" )
            time.wait(int(time_left))
            n = 1
            
        else:
            print("Still more than an hour left try again later")
            n = 1
            return False



def connect():              #copy paste this block for various subjects
    global ID, PASS
    ID = ""                 #enter id and pass here
    PASS = ""
    print(ID)
    print(PASS)



if(day == "Monday"):
    hr_join = 9             #copy-paste and rename hr_join and min_join to set the timings for various classes
    min_join = 0
    if(check()):
        connect()

elif(day == "Tuesday"):
    hr_join = 9
    min_join = 0
    if(check()):
        connect()

elif(day == "Wednesday"):
    hr_join = 9
    min_join = 0
    if(check()):
        connect()

elif(day == "Thursday"):
    hr_join = 9
    min_join = 0
    if(check()):
        connect()

elif(day == "Friday"):
    hr_join = 9
    min_join = 0
    if(check()):
        connect()

elif(day == "Saturday"):
    hr_join = 00
    min_join = 10
    if(check()):
        connect()

print(ID)
print(PASS)