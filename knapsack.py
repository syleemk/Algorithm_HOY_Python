itemNum = 4
Max = -1
maxW = 10


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


Items = [Item(7,42), Item(3,12), Item(4,40), Item(5,25)]

def knapsack(currentN, currentW, currentV):
    global Max
    if currentW <= maxW:
        Max = max(Max, currentV)

    for i in range(currentN+1, itemNum):
        if currentW + Items[i].weight <= maxW:
            knapsack(i ,currentW + Items[i].weight, currentV + Items[i].value)



for i in range(itemNum):
    knapsack(i, Items[i].weight, Items[i].value)

print("%d " % Max)



