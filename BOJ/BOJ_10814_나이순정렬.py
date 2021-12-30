n = int(input())
arr = []
for _ in range(n):
    x,y = input().split()
    # int로 바꿔주는 로직이 중요함
    arr.append([int(x),y])

# 람다를 이용해서 정렬해주는 로직이 중요함
arr.sort(key=lambda x : x[0])
for i in range(len(arr)):
    print(arr[i][0],arr[i][1])