# p371_practice.py
# 팩토리얼 예제 풀어보기 (디버깅으로 과정알아보기)

def factorial(n):
    if n <= 1:
        print('1 반환')
        return 1
    print(f'{n} * {n-1}! 호출')
    retVal = factorial(n-1)

    print(f'{n} * {n-1} 반환 (={retVal})' )
    return n * retVal

print(f'\n5! = {factorial(5)}')