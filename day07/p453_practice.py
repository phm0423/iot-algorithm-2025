# p453_practice.py
# 선택정렬과 퀵정렬 성능비교

import random
import time

# 함수선언
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if ary[minIdx] > ary[k]:
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx], ary[i]

    return ary

def qSort(arr, start, end):
    if end <= start:
        return
    low = start
    high = end

    pivot = arr[(low+high)//2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low+1, high-1

    mid = low

    qSort(arr, start, mid-1)
    qSort(arr, mid, end)

def quickSort(ary):
    qSort(ary, 0, len(ary)-1)

# 메인코드
countAry = [1000, 10000, 12000, 15000]

for count in countAry:
    tempAry = [random.randint(10000, 99999) for _ in range(count)]
    selectAry = tempAry[:]
    quickAry = tempAry[:]

    print(f'## 데이터수 : {count}개')
    start = time.time()
    selectionSort(selectAry)
    end = time.time()
    print(f'선택정렬 -->{end-start:10.3f}초')
    start = time.time()
    quickSort(selectAry)
    end = time.time()
    print(f'퀵정렬 --> {end-start:10.3f}초')
    print()

    # count *=5 (의미 몰룸)