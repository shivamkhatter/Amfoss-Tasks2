tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]
def printTable(tableData):
    L=[]
    for x in tableData:
        m=0
        for y in x:
            if len(y) >m:
                m=len(y)
        L.append(m)       
    
    for i in range (len(tableData[0])):
        for j in range(len(tableData)):
            if printTable!='':
                print(tableData[j][i].rjust(L[j]),end=' ')
        print('\n')
printTable(tableData)
    

