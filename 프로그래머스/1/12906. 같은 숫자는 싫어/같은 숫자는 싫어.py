def solution(arr):
    arr2 = []
    arr2.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i]!=arr[i-1]:
            arr2.append(arr[i])
    answer = arr2
    return answer