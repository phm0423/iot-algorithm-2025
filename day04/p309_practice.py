# p309_practice.py
# 편의점 판매물건목록 출력

import random
## 함수 선언 부분 ##
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def preorder(node):
        if node == None:
            return
        print(node.data, end = ' ')
        preorder(node.left)
        preorder(node.right)

## 전역변수선언 ##
memory = []
root = None
dataAry = ['바나나맛우유', '레쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sellAry = [random.choice(dataAry) for _ in range(20)]

print(f'오늘  판매된 물건(중복O) --> {sellAry}')

## 메인코드 ##
if __name__ =='__main__':
    node = TreeNode()
    node.data = sellAry[0]
    root = node
    memory.append(node)
    for name in sellAry[1:]:
        node = TreeNode()
        node.data = name

        curr = root
        while True:
            if name == curr.data:
                break
            if name < curr.data:
                if curr.left == None:
                    curr.left = node
                    memory.append(node)
                    break
                curr = curr.left
            else:
                if curr.right == None:
                    curr.right = node
                    memory.append(node)
                    break
                curr = curr.right

    print('이진 탐색 트리 구성 완료')
    
    print('오늘 판매된종류(중복X)-->', end = ' ')
    preorder(root)