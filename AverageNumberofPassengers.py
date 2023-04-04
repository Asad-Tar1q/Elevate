import math

def RatedCarCapacity(LC, m): #CC
    CC = math.floor(LC/m)
    return CC

def Passengers(cfM, cfA, CC, ac, ap): #average number of passenger in the car based on area and mass (persons)
    pm = (cfM/100)*CC #average persons in lift according to mass 
    pa = (cfA/100)*(ac/ap) #average persons in lift according to area of lift
    return min(pm,pa)

def main():
    ac = float(input("Car Area: ")) #car area
    ap = float(input("Area per person: ")) #area per person
    cfM = float(input("Enter capacity factor by mass (as a percentage): "))
    cfA = float(input("Enter capacity factor by area: (as a percentage): "))
    LC = float(input("Elevator Capacity (KG): "))
    m = float(input("Passenger Mass: "))
    CC = RatedCarCapacity(LC,m)
    average_passengers = Passengers(cfM, cfA, CC, ac, ap)
    print(average_passengers)
    print(CC)

main()