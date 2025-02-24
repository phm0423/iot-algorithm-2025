import random

# 전역 변수 선언

SIZE = 20
dataAry = ['콘말차', '삿포로 맥주', '아카페라 벤티 헤이즐넛', '레어치즈푸딩', '척오리지널 메가 사워', '요아정 요거트컵', 
           '페퍼로니피자주먹밥', '널담 슈톨렌', '딸기마시멜로케이크', '버니공쥬 딸기뚱카롱', '고추잡채호빵', '체다 슈크림붕어스낵']
sellAry = [random.choice(dataAry) for _ in range(SIZE)]
changeSellAry = sellAry

# 함수 선언
def run():
    while True:
        sel_menu = set_menu()
        if sel_menu == 1:
            print(f'오늘 판매된 물건(중복O) --> {sellAry}')
            print('------------------------------------')

        elif sel_menu == 2:
            changeSellAry.sort()
            i = 0
            while True:         # 1.첫번째와 두번째 인덱스를 비교를 반복하여
                if i+1 >= len(changeSellAry): # 4. i가 리스트 길이를 넘어가면 break
                    break
                elif changeSellAry[i] != changeSellAry[i+1]:   # 2. 서로 다르면 i를 증가시켜 다음인덱스로 넘어가고,
                    i += 1
                elif changeSellAry[i] == changeSellAry[i+1]:    # 3. 서로 같으면 앞쪽 인덱스(i번)를 리스트에서 삭제한다.
                    del(changeSellAry[i])
            
            print(f'오늘 판매된 물건(중복X) --> {changeSellAry}')
            print('------------------------------------')

        elif sel_menu == 3:
            break
        else:
            print('1, 2, 3 중 입력해주세요')
            print('------------------------------------')

def set_menu():
    str_menu = (f'1. 전체 판매 목록 보기\n'
                '2. 중복된 물품 제외하여 목록 보기\n'
                '3. 프로그램 종료')
    print(str_menu)
    try:
        sel_menu = int(input('메뉴 번호 입력: '))
    except Exception as e:
        sel_menu = 0

    return sel_menu

## 메인코드 ##
if __name__ =='__main__':
    run()
    print('프로그램 종료')

