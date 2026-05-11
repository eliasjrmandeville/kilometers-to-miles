#Name: Elias Mandeville
#Date: Tuesday, 9.16.25
#Desc: Program to calculate the number of miles traveled
#based on user input of kilometers

def main():
    
    #Declare constant to store conversion of .6214
    CONVERSION = 0.6214

    #Declare string variable to store name
    userName = ""

    #Declare and initialize real variables to store kilometers and miles
    kiloMeters = 0.0
    miles = 0.0

    #Display line of 25 -'s
    print("-" * 79)
    #Display Introduction
    print("\t\tWELCOME TO MY MILES CONVERSION PROGRAM!")
    #Display line of 25 -'s
    print("-" * 79)
    
    #Display 2 blank lines
    print()
    print()
    
    #Prompt user for name
    userName = input("Please enter your name: ")

    #Greeting User
    print(f"\nHello, {userName}!")
    
    #Prompt user for kilometers traveled
    kiloMeters = float(input(f"How many kilometers did you travel, {userName}? "))

    #Calculate miles
    miles = kiloMeters * CONVERSION
    
    #Display results
    print()
    print(f"Name:\t{userName}")
    print(f"Miles:\t{miles:.2f}")
    
    #Display outro
    print(f"\nThank you, {userName}!")

#Call main function
main()

