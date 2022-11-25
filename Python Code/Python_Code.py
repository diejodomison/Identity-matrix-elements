dim=int(input())
for i in range(dim):
    for j in range(dim):
        if j!=i and j!=dim-1:
            print(0,end=",")
        elif j==i and j!=dim-1:
            print(1,end=",")
        elif j==i:
            print(1)
        else:
            print(0)
            



    


