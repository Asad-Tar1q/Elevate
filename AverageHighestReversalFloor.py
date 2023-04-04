import math
N=14
outer_sum = 0
inner_sum = 0
P = 9.14

for j in range(1,N+1):
    
    inner_sum = 0
    for i in range(1, j):
        inner_sum += 48/672
    outer_sum +=(inner_sum)**P



        
H = N - outer_sum
hi = float(input("Enter height of each floor: "))
initial_floor_height = float(input("Ground Floor to First Floor Height: "))
dh = initial_floor_height + hi*math.floor(H-1) + (H-math.floor(H))*hi

print(H)
print(dh)