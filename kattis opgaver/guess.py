l = 1
r = 1000
m = (1 + 1000) // 2

print(m)
while True:
    response = input()

    if(response == "lower"):
        r = m - 1

    elif(response == "higher"):
        l = m

    elif(response == "correct"):
        break
    
    m = (l + r + 1) // 2

    print(m)
