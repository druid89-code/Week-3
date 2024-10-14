def main():
    firstName ="Umar"
    print(firstName[0]) #Prints the first letter of my name

    print()

    listSize = len(firstName)
    for i in range(listSize): #I've only defined the for loop end here
        upperCaseNameCharacter =firstName[i].upper() #easier to work with
        print(upperCaseNameCharacter)