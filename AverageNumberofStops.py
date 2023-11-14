def ProbableNumberOfStops(N, ui, U, P):

    for i in range(N-1):
        S = N - (N*(1-(ui[i]/U))**P)
    return S


def EffectivePopulation(population):
    u = sum(population)
    return u



def main():
    N = int(input("Number of floors above main terminal: "))
    population = []
    for i in range(N):
        population.append(int(input(f"Enter the population for floor {i+1}: ")))

    U = EffectivePopulation(population)
    P = 9.14



    S = ProbableNumberOfStops(N, population, U, P)

    print(S)
    

main()
