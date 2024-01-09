N = int(input()) # 숫자 개수
nums = input()
sum = 0; # 값의 합


for i in range(N):
    sum += int(nums[i])

print(sum)