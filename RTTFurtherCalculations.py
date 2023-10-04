import math
#average time betweem elevator departures
def UppeakInterval(RTT,L):
    uppint = RTT/L
    return uppint

#Number of people transported in 5 minutes
def UpPeakHandlingCapacity(P,uppint):
    upphc = (300*P)/uppint
    return upphc

#Percentage of effective building population managed
def HandlingCapacity(upphc,U):
    pop = (100*upphc) / U
    return pop

def main():
    RTT = 155.6
    L = 5
    P = 9.14
    U = 672
    uppint = UppeakInterval(RTT,L)
    upphc = UpPeakHandlingCapacity(P,uppint)
    pop = HandlingCapacity(upphc,U)

    print(f"Up Peak Interval: {math.round(uppint,2)}s")
    print(f"Up Peak Handling Capacity: {math.round(upphc,2)} people")
    print(f"Handling Capacity: {math.round(pop,2)}%")

    
main()
