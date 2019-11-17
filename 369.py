import time
startTime = time.time()

player = [0]
pNum = input("플레이어 수를 입력하세요 : ")
endNum = input("끝나는 수를 입력하세요 : ")

for i in range(int(pNum)):
    name = input("플레이어 %d의 이름을 입력하세요 :" % (i+1))
    player.insert(i, name)


clapCount = 0

for i in range(1, int(endNum)+1):
    string = str(i)
    length = len(string)
    clapCount = 0
    for k in range(length):
        if string[k] == '3' or string[k] == '6' or string[k] == '9':
            clapCount = clapCount + 1
    if clapCount is 0:
        print("%s : %d" % (player[(i-1) % int(pNum)], i))
    else:
        print("%s : " % player[(i-1) % int(pNum)], end = ' ' )
        for i in range(clapCount):
            print("짝!", end = '')
        print(' ');
endTime = time.time() - startTime
print("\nTime : " , endTime)