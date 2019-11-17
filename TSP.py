city = 4
dist = (
    (0,2,5,7),
    (2,0,8,3),
    (5,8,0,1),
    (7,3,1,0)
)
visited_all = (1 << city) - 1
inf = float('inf')
Min = 10000000000


def find_dist(start, last, visited, tmp_dist):
    global Min
    if visited == visited_all:
        if dist[last][start] != 0:
            tmp_dist += dist[last][start]
            Min = min(Min, tmp_dist)
            return

    for c in range(city):
        if (visited & (1 << c)) == 0 and dist[last][c] != 0:
            find_dist(start, c, visited | (1 << c), tmp_dist + dist[last][c])


for i in range(city):
    find_dist(i, i, 1 << i, 0)


print("%d " % Min)



