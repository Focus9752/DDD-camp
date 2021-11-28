# ikke færdig

n,m = list(map(int, input().split()))

canSizes = []
colors = []
answers = []

for i in range(n):
    canSizes.append(int(input()))
canSizes.sort()

for i in range(m):
    colors.append(int(input()))

def main():
    answer = 0

    for color in colors:
        binResult = binarySearch(canSizes, color, 0, len(canSizes) - 1)
        if canSizes[binResult] == color:
            pass
        else:
            smallestVal = min(canSizes, key=lambda x : abs(x - color))
            answer += abs(smallestVal - color)

    print(answer)

def binarySearch(list, elem, l, r):
    if l <= r:
        m = (l + r + 1) // 2

        if l == r:
            return l
                
        elif list[m] > elem:
            return binarySearch(list, elem, l, m - 1)
        
        else:
            return binarySearch(list, elem, m, r)



main()
