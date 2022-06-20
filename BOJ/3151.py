N = int(input())
nums = sorted(map(int, input().split()))
answer = 0

for i in range(N - 2):
    left, right = i + 1, N - 1
    while left < right:
        sum_val = nums[i] + nums[left] + nums[right]
        if sum_val < 0:
            left += 1
        elif sum_val > 0:
            right -= 1
        else:
            if nums[left] == nums[right]:
                answer += (right - left + 1) * (right - left) // 2
                break
            else:
                l, r = 1, 1
                while nums[left] == nums[left + 1]:
                    left += 1
                    l += 1
                while nums[right] == nums[right - 1]:
                    right -= 1
                    r += 1
                answer += l * r
            left += 1
            right -= 1

print(answer)

