def inspired_binary_search(A, elem):
    answer = 0
    for i in range(30):
        if S(30 - i, elem) == True:
            answer += 2**(30 - i)
        print(answer)
    if A[answer] == elem:
        print(answer + 1)
    else: print(-1)

def S(x, elem):
    if(x > len(A) - 1):
        return False

    if A[x] <= elem:
        return True

    else:
        return False

# Input
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
requests = list(map(int, input().split()))

for request in requests:
    inspired_binary_search(A, request)
