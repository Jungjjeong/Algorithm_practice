import pandas as pd

def solution(n, k, cmd):
    df = pd.DataFrame([
        ['무지'],
        ['콘'],
        ['어피치'],
        ['제이지'],
        ['프로도'],
        ['네오'],
        ['튜브'],
        ['라이언']
    ])
    for i in cmd:
        if D in i: # x칸 위 행 선택
            print("D", i)
        elif U in i: # X칸 아래 행 선택
            print("U", i)
        elif C in i: # 선택 행 삭제 후 바로 아래 행 선택
            print("C", i)
        elif Z in i: # 가장 최근에 삭제한 행 복구
            print("Z", i)
        
    print(df)
    
    answer = ''
    return answer