# p311_practice.py
# 폴더 및 하위 폴더 중복이름찾기

import os
## 함수선언 ##
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역변수선언 ##
memory = []
root = None
fnameAry = []

## 메인 코드 ##

if __name__ == '__main__':
    folderName = 'C:/Program Files/Common Files/'
    for dirName, subDirList, fnames in os.walk(folderName):
        for fname in fnames:
            fnameAry.append(fname)

    node = TreeNode()
    node.data = fnameAry[0]
    root = node
    memory.append(node)

    dupNameAry = []

    for name in fnameAry[1:]:
        node = TreeNode()
        node.data = name
        
        curr = root
        while True:
            if name == curr.data:
                dupNameAry.append(name)
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

    dupNameAry = list(set(dupNameAry))

    print(f'{folderName}, 및 그 하위 디렉터리의 중복된 파일 목록 -->')
    print(dupNameAry)

                