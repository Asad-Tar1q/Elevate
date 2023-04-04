def ProbableNumberOfStops(N, ui, U, P):
    
    for i in range(len(ui)-1):
        S = N - (N*(1-(ui[i]/U))**P)
    return S


def EffectivePopulation(population):
    u = sum(population)
    return u



def main():
    N = int(input("Number of floors above main terminal: "))
    population = list(map(int, input("\nEnter the population : ").strip().split()))[:N]
    U = EffectivePopulation(population)
    P = 9.14

     

    S = ProbableNumberOfStops(N, population, U, P)
   
    print(S)


main()