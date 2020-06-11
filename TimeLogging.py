import datetime 

timeLogging = open("Haha I Lost.txt", "a")

print("Time Logging System")

newDay = input("Is today a new day?\n")

if newDay == "yes" or "Yes":
    date = datetime.date.today()
    timeLogging.write(str(date) + "\n")
        
elif newDay == "no":
    print("Not the first session I see.")

elif newDay == "No":
    print("Not the first session I see.")
        

        


newSession = input("Would you like to start a new session?\n")
if newSession == "yes" or "Yes":
       
        
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
       
        timeLogging.write(str(current_time) + " To ")
        
        endOfSession = input("Type 'end' when you have finished your session\n")
        
        if endOfSession == "end":
           
            endingNow = datetime.datetime.now()  
            endingTime = endingNow.strftime("%H:%M:%S")  
            timeLogging.write(str(endingTime) + "\n")

            totalTimePlayed = (endingNow - now)
            timeInSeconds = (totalTimePlayed.total_seconds() // 1)
            timeInMinutes = (timeInSeconds / 60)
            timeInHours = (timeInSeconds / 3600)
            
            print(timeInHours, timeInMinutes, timeInSeconds)

            timeLogging.write(str(timeInHours) + " Hours played\n \n")


       
        else:
            print("Great, you ruined it noob")



if newSession == "No" or "no":
        print("Ok.")
else:
    print("Im guessing you meant no, so yeah.")

timeLogging.close()