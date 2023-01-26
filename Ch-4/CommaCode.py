L=[]
n=int(input("Enter the size of list: "))
for i in range (n):
    L.append(input("Enter the element: "))
for j in L:
    if j==L[-1]:
        print('and ' +j)
    else:
        print(j+', ',end='')
