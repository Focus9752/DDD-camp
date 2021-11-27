N, Q = map(int,input().split())

setArr = list(range(0,N))

firstRun = True
originalX = None

def find(x):
    global firstRun
    global originalX

    if(firstRun == True):
        originalX = x
        firstRun = False
        
    if(setArr[x] == x):
        setArr[originalX] = x

        originalX = None
        firstRun = True

        return x

    return find(setArr[x])

def main():
    
    inputs = input().split()

    operation = inputs[0]
    a = int(inputs[1])
    b = int(inputs[2])
    
    if(operation == "?"):
        if(find(a) == find(b)):
            print("yes")
        else:
            print("no")
            
    elif(operation == "="):
        setArr[a] = b

        for index, item in enumerate(setArr):
            if(find(item) == a):
                setArr[index] = b

for i in range(Q):
    main()

