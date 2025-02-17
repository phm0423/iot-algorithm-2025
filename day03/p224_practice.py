# p224_practice.py
# 괄호 매칭검사

## 전역 변수 선언##
SIZE = 100
stack=[None for _ in range(SIZE)]
top = -1

## 함수 선언 부분 ##
def isStackFull():  # 스택이 꽉 찼는지 확인하는 함수
    global SIZE, stack, top
    if (top == SIZE -1):   # Full / 실무에서 쓰는 스택은 거의 무제한
        return True
    else: 
        return False
    
def isStackEmpty(): # 스택이 비었는지 확인
    global SIZE, stack, top
    if (top == -1): # Empty
        return True
    else:
        return False
    
def push(data):     # 스택에 데이터 추가
    global SIZE, stack, top
    if isStackFull():  # isStackFull() == True와 동일
        print('Stack is full!')
        # return 생략
    else:
        top += 1
        stack[top] = data

def pop():          # 스택에서 데이터 추출
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is empty.')
        return None
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
    
def peek():         # 스택의 top위치의 데이터 확인(살짝보기)
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is empty.')
        return None
    else:
        return stack[top]
    
def checkBracket(expr):
    for ch in expr:
        if ch in '([{<':
            push(ch)
        elif ch in ')]}>':
            out = pop()
            if ch == ')' and out =='(':
                pass
            elif ch == ']' and out =='[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else : 
                return False
        else :
            pass
    if isStackEmpty():
        return True
    else:
        return False
    
## 메인 코드 부분 ##
if __name__ == '__main__':

    exprAry = ['(A+B)', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C*D]>)']
    
    for expr in exprAry:
        top = -1
        print(expr, '==>', checkBracket(expr))