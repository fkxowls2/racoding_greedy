# 탐욕 알고리즘
# 가장 적은 거스름돈 개수를 계산하는 알고리즘(큰 돈 먼저 거슬러주는 알고리즘)
def greedy():
    coin = [50000,10000,5000,1000,500,100,50,10]   #현재 존재하는 한국의 모든 거슴름돈 단위
    box =[]
    cash = int(input('거스름돈을 입력하세요~'))
    for i in coin:   #거스름돈 계산
        if cash//i == 0:   #거슬러줄 수 없는 거스름돈 단위는 넘어가라
            continue
        box.append([i,cash//i])   #해당 거스름돈 단위와 개수를 box변수에 담는다
        cash = cash%i   #해당 거스름돈으로 제외하고 나머지 돈을 cash변수에 담는다
    for i in box:   #거스름돈 출력
        print('{}원 {}개'.format(i[0],i[1]), end='  ')   #한 줄로 출력하라

greedy()   #greedy 함수 실행