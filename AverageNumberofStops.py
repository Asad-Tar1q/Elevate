def ProbableNumberOfStops(N, ui, U, P):
    S = N - (N*(1-(ui/U))**P)
    return S



def main():
    N = int(input("Number of floors above main terminal: "))
    ui = int(input("Population per floor: "))
    U = ui*N
    P = 9.14

    

    S = ProbableNumberOfStops(N, ui, U, P)
   
    print(S)


main()