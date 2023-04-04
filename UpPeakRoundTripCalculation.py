 
import math



def TimeTravelFunction(d,v,a,j,ts,t_level):
    #Choosing Equation

    lower = (2*(a)**(3))/((j)**(2))
    upper = (a**(2)*v + v**(2)*j)/(j*a)

    #Reaches Full Speed
    if d >= upper: 
        time = (d/v) + (a/j) + (v/a) + ts + t_level

    #Reaches Full acceleration but not full speed
    elif d >= lower:
        time = a/j + ((a**(3)+4*d*j**(2))**(1/2))/(j*(a)**(1/2)) + ts + t_level

    #Does not reach Full Acceleration or Full Speed
    else:
        time = ((32*d)/j)**(1/3)+ts+t_level

    #Output Time
    time = round(time,2)
    return time


def TimeStop(tf, dh, S, v, time_dwell, time_door_closing, t_ad, t0):
    ts = (tf*(dh/S) - ((dh)/(S*v))) + time_dwell + time_door_closing + t0 - t_ad
    return ts

def ProbableNumberOfStops(N, ui, U, P):
    S = N - (N*(1-(ui/U))**P)
    return S

def RatedCarCapacity(LC, m): #CC
    CC = math.floor(LC/m)
    return CC

def RoundTripTime(dh,dx,v,S,ts,P,tp,loss):
    RTT = ((2*dh+dx)/v+(S+1)*ts + 2*P*tp)(1+loss)
    return RTT

def Passengers(cfM, cfA, CC, ac, ap): #average number of passenger in the car based on area and mass (persons)
    pm = cfM*CC #average persons in lift according to mass 
    pa = cfA*(ac/ap) #average persons in lift according to area of lift
    return min(pm,pa)

def main():
    #Variables
    
    v = float(input("Velocity: "))
    a = float(input("Acceleration: "))
    j = float(input("Jerk: "))
    ts = float(input("Allowance for motor start delay: "))
    t_level = float(input("Levelling Delay: "))
    
    ac = float(input("Car Area: ")) #car area
    ap = float(input("Area per person: ")) #area per person
    cfM = float(input("Enter capacity factor by mass (as a percentage): "))
    cfA = float(input("Enter capacity factor by area: (as a percentage): "))
    L = int(input("Number of Elevators: "))
    LC = float(input("Elevator Capacity (KG): "))
    loss = float(input("Round trip time losses (percentage): "))
    m = float(input("Passenger Mass: "))
    N = int(input("Number of floors above main terminal "))
    time_door_closing = float(input("Door closing time: "))
    t_ad = float(input("Advanced door closing time: "))
    time_dwell = float(input("Door dwell time: "))
    t0 = float(input("Door opening time: ")) 
    
    ui = int(input("Population per floor: "))
    hi = float(input("Enter height of each floor: "))
    


    #average passenger transfer time
    passenger_loading_time = float(input("Enter passenger loading time: "))
    passenger_unloading_time = float(input("Enter passenger unloading time: "))
    tp = (passenger_loading_time + passenger_unloading_time) / 2 
    
    #Travel Distance to Heighest Floor
    dx = float(input("Total height of unserved floors (set to 0 if there are no express floors): "))
    dh = N*hi + 5 #Try after with height of individual floors

    #s
    CC = RatedCarCapacity(LC,m) #safe number of passengers that can be transported by the car
    P = Passengers(cfM, cfA, CC, ac, ap)

    

    #Probable Number of stops AKA S
    U = ui*N
    S = ProbableNumberOfStops(N, ui, U, P)

    d = dh/S
    tf = TimeTravelFunction(d,v,a,j,ts,t_level)
    time_stop = TimeStop(tf, dh, S, v, time_dwell, time_door_closing, t_ad, t0)


    RTT = RoundTripTime(dh,dx,v,S,time_stop,P,tp,loss)

    print(RTT)
    print(CC)
    print(dh)
    print(P)
    print(S)
    print(tp)
    print(ts)
    print(U)


main()