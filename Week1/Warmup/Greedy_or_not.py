def best_score(nums, left, right):
    if left > right:
        return 0
    total = sum(nums[left:right+1])
    pick_left = nums[left] + total - nums[left] - best_score(nums, left+1, right)
    pick_right = nums[right] + total - nums[right] - best_score(nums, left, right-1)
    return max(pick_left, pick_right)

n = int(input())
nums = list(map(int, input().split()))

total = sum(nums)
score1 = best_score(nums, 0, n-1)
score2 = total - score1

if score1 > score2:
    print("Player 1 wins")
elif score2 > score1:
    print("Player 2 wins")
else:
    print("Its a draw")
