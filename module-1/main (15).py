#Darreon Tolen
#CSD 325
#Module 1.3

def bottles_of_beer():
    # Start
    bottles = int(input("Enter the number of bottles: "))

    # Loop while there are bottles left
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print("Take one down and pass it around,")
            print(f"{bottles - 1} bottle{'s' if bottles - 1 != 1 else ''} of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around,")
            print("No more bottles of beer on the wall.\n")

        # Decrease bottle count
        bottles -= 1

    # No bottles left
    print("Time to buy more beer!")

# Run the program
bottles_of_beer()




