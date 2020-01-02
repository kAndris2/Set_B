i = 0
num = 0
div = 7

while i != 25:
    if num > 100 and num % div == 0:
        i += 1
        print(str(i) + ". - " + str(num))
    num += 1