#String as Lists
def main():
    weekdays=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    weekdaysSize = len(weekdays) #Size of the weekday list and will be used in for loop end
    for i in range(weekdaysSize):
        if(weekdays[i][0] == "S" or weekdays[i][0] == "I"):
            dayString = weekdays[i]
            print(dayString)