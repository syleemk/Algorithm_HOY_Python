op = input("연산자를 입력하세요 (+, -, x, % ) : ")
res = int(input("결과 값을 입력하세요 : "))

if op is '+':
    for x in range(1, res):
        y = res - x
        print("( %d, %d ) " % (x, y))
elif op is '-':
    while True:
        ran = int(input("숫자의 범위를 입력해주세요 : "))
        if ran <= res:
            print("범위를 결과 값보다 큰 수로 입력해주세요!")
        else:
            break
    for x in range(ran, res, -1):
        y = x - res
        print("( %d, %d )" % (x, y))
elif op is 'x':
    for x in range(1, res + 1):
        y = res / x
        if res % x is 0:
            print("( %d, %d )" % (x, y))
elif op is '%':
    while True:
        ran = int(input("숫자의 범위를 입력해주세요 : "))
        if ran <= res:
            print("범위를 결과 값보다 큰 수로 입력해주세요!")
        else:
            break
    y = 1
    while True:
        x = res * y
        if x > ran: break
        print("( %d, %d )" % (x, y))
        y += 1


