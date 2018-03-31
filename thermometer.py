# Thermometer by: Gracie Bracken
def main() :
    #instructions
    print("---------------------------------------------")
    print("Hey Dipper, remember your thermometer next time.")
    print("I'll help for now! Use your stopwatch, count how ")
    print("many times the cricket chirps in 13 seconds.")
    print("")

    # get the "chirps" from the user
    chps=input("How many times did the crickets chirp?  ")
    chps=int(chps)
    print("")

    # caculations and print
    ct=40
    temp=ct+chps
    if temp<50:
        print("It's way too cold for crickets.")
    else:
        print("By my AWESOME caculations, the temperature is",temp)
    
    print("---------------------------------------------")
    
main()

