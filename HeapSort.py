class Heap:
    def __init__(self):
        self.h = [0, ]
        self.size = 0

    def insert(self, element): # 가장 마지막에 넣고, 부모랑 비교해가면서 위로 올려보낸다
        self.size += 1
        i = self.size
        self.h.append(element)
        while i!=1 and element < self.h[i//2] :
            self.h[i] = self.h[i//2]
            i = i//2
        self.h[i] = element

    def delete(self):
        parent = 1
        child = 2
        pop = self.size

        out = self.h[parent] # 루트가 삭제되고 가장 마지막 노드가 루트자리에 온다
        last = self.h[self.size]
        self.size -= 1
        
        while child <= self.size:
            if (child <= self.size) and (self.h[child] > self.h[child+1]): #더 작은 자식을 고른다
                child += 1
            if last <= self.h[child]: break
            self.h[parent] = self.h[child]
            parent = child
            child *= 2
        self.h[parent] = last
        self.h.pop(pop)
        return out

    def Sort(self, arr, arrSize):
        for i in range(arrSize):
            self.insert(arr[i])

        for i in range(arrSize):
            arr[i] = self.delete()


def main():
    h = Heap()
    arr = []
    s = input("정렬할 배열의 원소를 한줄에 입력하세요 : ")
    arr = s.split()
    arr = list(map(int, arr))
    num = len(arr)

    Heap.Sort(h, arr, num)

    print("정렬 결과 : ", end='')
    for i in range(num):
        print('%d' % arr[i], end=' ')

main()