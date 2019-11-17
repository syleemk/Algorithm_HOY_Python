pNum = 4
jNum = 4

Min = 1000000000
assigned_all = (1 << jNum) - 1

cost = (
    (9, 2, 7, 8),
    (6, 4, 3, 7),
    (5, 8, 1, 8),
    (7, 6, 9, 4)
)

def find_cost(person, assigned, t_cost):
    global Min
    if assigned is assigned_all:
        Min = min(Min, t_cost)
        return

    for i in range(jNum):
        if assigned & (1 << i) == 0 and person < pNum:
            find_cost(person + 1, assigned | (1 << i), t_cost + cost[person + 1][i])


for i in range(jNum):
    find_cost(0, 1 << i, cost[0][i])


print("%d" % Min)

