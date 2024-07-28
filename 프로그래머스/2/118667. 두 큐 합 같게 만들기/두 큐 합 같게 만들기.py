from collections import deque

def solution(queue1, queue2):
    answer = 0
    half = (sum(queue1) + sum(queue2)) / 2
    sum1 = sum(queue1) # 합을 미리 구해둬서 시간 단축
    sum2 = sum(queue2)
    deque1 = deque(queue1) # deque로 바꿔줌
    deque2 = deque(queue2)
    limit = len(deque1) * 3 # 최대 횟수 설정
    
    while answer <= limit : # 각 큐의 값이 같아질 때까지 반복
        if sum1 == sum2 : # 각 큐의 합이 같다면 반복 멈추기
            return answer
        
        if sum1 < sum2 : # 큐1의 합보다 큐2의 합이 크다면
            if deque2 :
              popped = deque2.popleft()
              sum2 -= popped
              deque1.append(popped)
              sum1 += popped
              answer += 1
            else :
              break
            
        elif sum1 > sum2 : # 큐1의 합보다 큐2의 합이 작다면
            if deque1 :
              popped = deque1.popleft()
              sum1 -= popped
              deque2.append(popped)
              sum2 += popped
              answer += 1
            else :
              break
        
    return -1