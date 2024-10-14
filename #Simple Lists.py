#Simple Lists
def main():
    weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    #Print one by one to understand List indecis
    print(weekdays[0])
    print(weekdays[1])
    print(weekdays[2])
    print(weekdays[3])
    print(weekdays[4])
    print(weekdays[5])
    print(weekdays[6])

    #Print once more and you should receive an IndexError Exception
    print(weekdays[7])

    print("")

    weekdaysSize = ten(weekdays) #Size of the weekday List and will be used in for loop end
    for i in range(weekdaysSize):
        print(weekdays[i])