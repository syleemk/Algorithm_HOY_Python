arr_changeType = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
arr_changeCount = [0 for i in range(8)]

def inputMoney():
    price = int(input("물건 가격을 입력해주세요 : "))
    while True:
        money = int(input("받은 돈의 액수를 입력해주세요 : "))
        if price == money: print("거스름돈이 없습니다.")
        elif price > money: print("돈을 더 내야합니다.")
        else:
            changes = money - price
            print("거스름돈 액수 : %d" % changes)
            return changes

def CountChanges(changes):
    i = 0
    while i < 8:
        if changes >= arr_changeType[i]:
            changes -= arr_changeType[i]
            arr_changeCount[i] += 1
            if changes == 0: break
        else: i+=1

def printChanges():
    for i in range(8):
        print("%d원 : %d개" %(arr_changeType[i], arr_changeCount[i]))


changes = inputMoney()
CountChanges(changes)
printChanges()


