def parser(filename):
    data = []
    try:
        with open(filename, "r") as f:
            for line in f.readlines():
                data.append([int(e) for e in line.split(" ")])
    except:
        pass
    return data

def SUM(data, indices):
    z = []
    for i in indices:
        z.append(sum(data[i]))
    return z


filename = input()
data = parser('C:/progi/PY/kontra/dima.txt' + filename)
print (data)



if(len(data) != 0):
    l = [len(e) for e in data]
    indices = [i for i, x in enumerate(l) if x == max(l)]
    print(max(SUM(data, indices)))
else:
    print(0)
print(indices)