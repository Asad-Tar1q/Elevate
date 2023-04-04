import math

def TimeStop(tf, dh, S, v, time_dwell, time_door_closing, t_ad, t0):
    ts = (tf - ((dh)/(S*v))) + time_dwell + time_door_closing + t0 - t_ad
    return ts

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


#AverageHighestReversalFloor
def AverageHighestReversalFloor(N,p):
    outer_sum = 0
    for j in range(1,N+1):
        
        inner_sum = 0
        for i in range(1, j):
            inner_sum += 48/672
        outer_sum +=(inner_sum)**p
    H = N - outer_sum
    return H

#COME BACK TO THIS
def TravelDistanceToHighestReversalFloor(H,hi, initial_floor_height):
    dh = initial_floor_height + hi*math.floor(H-1) + (H-math.floor(H))*hi
    return dh


def main():
    time_door_closing = float(input("Door closing time: "))
    t_ad = float(input("Advanced door closing time: "))
    time_dwell = float(input("Door dwell time: "))
    t0 = float(input("Door opening time: "))
    S = 6.9

    v = float(input("Velocity: "))
    a = float(input("Acceleration: "))
    j = float(input("Jerk: "))
    ts = float(input("Allowance for motor start delay: "))
    t_level = float(input("Levelling Delay: "))
    hi = float(input("Enter height of each floor: "))
    initial_floor_height = float(input("Ground Floor to First Floor Height: "))
    p = 9.14
    N = 14
    H = AverageHighestReversalFloor(N,p)
    dh = TravelDistanceToHighestReversalFloor(H,hi,initial_floor_height)
    d = dh/S
    tf = TimeTravelFunction(d,v,a,j,ts,t_level)
    travel_time = TimeStop(tf, dh, S, v, time_dwell, time_door_closing, t_ad, t0)
    
    print(f"H: {H}")
    print(f"dh: {dh}")
    print(f"tf {tf}")
    print(f"Travel Time {travel_time}")





main()

