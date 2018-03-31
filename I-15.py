# I-15 by Gracie Bracken 02/10/2018
def main() :
    #instructions
    print("...............................................................")
    print("Welcome to the highway travel advisor!")
    print("This application has been configured to work")
    print("with travel on I-15 within the state of Utah.")
    print("We'll ask for a few pieces of information, then")
    print("give you advice on your travel.")
    print("")
    
# enter mile marker
    ent_mile_marker=input("Enter I-15 at what mile marker? ")
    ent_mile_marker=int(ent_mile_marker)
# exit mile marker
    ex_mile_marker=input("Exit I-15 at what mile marker? ")
    ex_mile_marker=int(ex_mile_marker)
# how long you want to take
    hours=input("How many hours from now do you want to arrive? ")
    hours=float(hours)
# speed you will be driving
    speed=input("Expected average speed in MPH? ")
    speed=int(speed)
    print("")
# equations
    travel= ex_mile_marker - ent_mile_marker
    arrive= travel / speed

# if and elif statements       
    if speed > 80 :
        print("WARNING! You will be traveling dangerously fast")
        print("and that's breaking the law.")
    elif speed < 60:
        print("WARNING! Your speed is too slow. You'll be a")
        print("hindrance to other trafic")

    else: 
        print("You will travel:",travel,"miles.")
        if arrive == hours :
            print("Your would have to leave right now!")
        elif arrive < hours :
            print("Leave in the next", hours - arrive, "hours to be on time.")
        elif arrive > hours :
            print("You won't be able to get there on time.")
            print("You'll be", arrive - hours, "hours late.")

    print("Thanks for using the highway travel advisor.")
    
    print("...............................................................")
    

main()
