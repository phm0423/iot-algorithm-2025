# p421_practice.py
# 성적별 조편성하기

# 전역변수선언
scoreAry = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]


# 클래스 및 함수 선언
def scoreSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0 , -1):
            if ary[cur-1][1]> ary[cur][1]:
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
    return ary

# 메인코드
print(f'정렬 전 --> {scoreAry}')
scoreAry = scoreSort(scoreAry)
print(f'정렬 후 --> {scoreAry}')

print('## 성적별 조 편성표 ##')
for i in range(len(scoreAry)//2):
    print(f'{scoreAry[i][0]} : {scoreAry[len(scoreAry)-1-i][0]}')