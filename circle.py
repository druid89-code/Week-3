def main():
    shapeHeightInput = int(input("Please enter the height of your shapes "))
    shapeHeightInput += 1 #as the for loops are exclusive

    #advanced tasks
    #Shape 1: Right_aligned triangle

    for i in range(shapeHeightInput):
        for j in range(1, i+1):
            print("X", end="")
            print()
            print("\n")