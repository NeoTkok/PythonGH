st = sorted(sorted(list(set([i for i in input().split()]))), key= lambda x: len(x), reverse=True)
for i in st:
    print(i)