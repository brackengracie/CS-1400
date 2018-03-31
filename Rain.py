def main():
    print("...............................................")
    print("Welcome to the rainwater tank calculator.")
    print("We'll ask you for a few parameters about your")
    print("rainfall and rain catchment area. Then, we'll")
    print("tell how big to make your tank. We assume")
    print("that your catchment area is rectangular.")
    print("")

    rain_fall=input("How many inches of rain fall in a large storm? ")
    rain_fall=float(rain_fall)

    width=input("How wide is your catchment area, in feet? ")
    width=int(width)

    length=input("How long is your catchment area, in feet? ")
    length=int(length)

    gallons=7.48

    area=width(12)*length(12)/gallons
    print(area)
    

    
    
                    
main()
