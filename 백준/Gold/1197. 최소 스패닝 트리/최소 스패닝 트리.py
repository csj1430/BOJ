import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())

graph = [[] for _ in range(v + 1)]

for _ in range(e) :
  a, b, c = map(int, input().split())
  
  graph[a].append((c, b)) # (가중치, 정점) 튜플 저장
  graph[b].append((c, a)) # 방향이 없기 때문에 똑같이 저장
  
def prim(start) :
  visited = [False] * (v + 1) # 정점 방문 여부 체크
  min_heap = [(0, start)] # 힙에 시작 노드 넣어줌
  total_weight = 0
  edge_count = 0
  
  while min_heap : # 힙이 빌 때까지 반복
    weight, b = heapq.heappop(min_heap)
    
    if visited[b] : # 이미 방문했으면 패스
      continue
    
    visited[b] = True
    total_weight += weight
    edge_count += 1
    
    if edge_count == v : # 모든 정점을 방문했다면 반복문 빠져나가기
      break
    
    for next_weight, a in graph[b] : # b와 연결된 정점들에 대해서
      if not visited[a] : # 방문하지 않았다면
        heapq.heappush(min_heap, (next_weight, a)) # 힙에 넣어줌
          
  return total_weight # 최소 스패닝 트리의 가중치를 출력
  
print(prim(1)) # 1번에서 시작하도록 설정. 어디서 시작해도 상관은 없음