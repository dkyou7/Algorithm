n = int(input())
arr = []
for _ in range(n):
    x,y = input().split()
    arr.append([int(x),int(y)])

arr.sort(key=lambda x : (x[1],x[0]))
for i in range(len(arr)):
    print(arr[i][0],arr[i][1])