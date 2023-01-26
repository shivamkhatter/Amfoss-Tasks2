tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]
def printTable():
    for i in range (len(tableData[0])):
        for j in range(len(tableData)):
            if printTable!='':
                print(tableData[j][i].rjust(8),end='')
        print('\n')
printTable()
    
