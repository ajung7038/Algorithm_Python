N = int(input()) # 시험 본 과목의 개수
score = list(map(int, input().split())) # 성적
max = max(score) # 가장 큰 점수
sum = 0 # 성적 합계

# 성적 계산
for i in score:
    sum += i/max*100

print(sum/N)