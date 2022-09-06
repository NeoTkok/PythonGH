y = input()
x = (y.split(" ")) # N, M, K, Ta, Tb, Tc
N, M, K, Ta, Tb, Tc = float(x[0]), float(x[1]), float(x[2]), float(x[3]), float(x[4]), float(x[5])

# время На лифте:

t = 2 * Tb + abs(N - M) * Ta + abs(N - K) * Ta 
print (t)
print(Tc*abs(N - M)) 
if (t <= Tc*abs(N - M)):
    print("elevator")
else:
    print("stairs")