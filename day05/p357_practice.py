# p357_practice.py
# 가장 효율적인 해저케이블망 설치
from operator import itemgetter


## 전역변수
G1 = None
cityAry = ['서울', '뉴욕', '런던', '북경', '방콕', '파리']
서울, 뉴욕, 런던, 북경, 방콕, 파리 = 0, 1, 2, 3, 4, 5

## 클래스 및 함수 선언
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g):
    print(' ', end = '     ')
    for v in range(g.SIZE):
        print(cityAry[v], end = '    ')
    print()
    for row in range(g.SIZE):
        print(cityAry[row], end = '   ')
        for col in range(g.SIZE):
            print('%2d'%g.graph[row][col], end = '\t')
        print()
    print()

def findVertex(g, findVtx):
    stack = []
    visitedAry = []

    current = 0 # 시작정점
    stack.append(current)
    visitedAry.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(gSize):
            if g.graph[current][vertex] != 0:
                if vertex in visitedAry: # 도착점이 이미 방문했으면
                    continue
                else :
                    next = vertex   # 다음 번 방문할 정점
                    break

        if next != None:    # 다음 방문할 정점이 있으면
            current = next
            stack.append(current)
            visitedAry.append(current)
        else : 
            current = stack.pop()

    if findVtx in visitedAry:
        return True
    else:
        return False

## 메인 코드 부분##
gSize = 6
G1 = Graph(gSize)
G1.graph[서울][뉴욕] = 80; G1.graph[서울][북경] = 10
G1.graph[뉴욕][서울] = 80; G1.graph[뉴욕][북경] = 40; G1.graph[뉴욕][방콕] = 70
G1.graph[런던][방콕] = 30; G1.graph[런던][파리] = 60
G1.graph[북경][서울] = 10; G1.graph[북경][뉴욕] = 40; G1.graph[북경][방콕] = 50
G1.graph[방콕][뉴욕] = 70; G1.graph[방콕][런던] = 30; G1.graph[방콕][북경] = 50; G1.graph[방콕][파리] = 20
G1.graph[파리][런던] = 60; G1.graph[파리][방콕] = 20

print('## 해저 케이블 전체 연결도 ##')
printGraph(G1)

# 가중치 간선 목록
edgeAry = []
for i in range(gSize):
    for k in range(gSize):
        if G1.graph[i][k] != 0:
            edgeAry.append([G1.graph[i][k], i, k])
edgeAry = sorted(edgeAry, key=itemgetter(0), reverse=False)

newAry = []
for i in range(0, len(edgeAry), 2):
    newAry.append(edgeAry[i])

print('## 중복간선 제거 목록 =>', end = ' ')
print(newAry)

# 가중치 높은 간선부터 제거
index = 0
# 0:춘천, 1:서울, 2:속초, 3:대전, 4:광주, 5:부산
while len(newAry) > (gSize -1): # 간선의 수가 (정점수  -1) 될때까지 반복
    start = newAry[index][1] # 서울부터 시작
    end = newAry[index][2]  # 광주부터 시작
    saveCost = newAry[index][0] # 현재 가중치 저장(복원을 위해서)

    G1.graph[start][end] = 0     # 무조건 지움
    G1.graph[end][start] = 0     # 무방향이라 양쪽으로 값이 다 있음

    startYN = findVertex(G1, start)  # 서울에 연결된 선이 있는지 확인
    endYN = findVertex(G1, end)      # 광주에 연결된 선이 있는지 확인

    if startYN and endYN:   # 둘다 다른 간선있으니까 지금 간선을 지워도 됨
        del(newAry[index])
    else:   # 연결된 간선이 없으니까 지웠던 인접행렬 값을 원상복귀
        G1.graph[start][end] = saveCost
        G1.graph[end][start] = saveCost
        index += 1

# 결과 출력
print('## 가장 효율적인 해저 케이블 연결도 ##')
printGraph(G1)

