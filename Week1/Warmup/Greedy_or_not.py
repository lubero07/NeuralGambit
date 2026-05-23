# Write your code here
n = int(input())
nums = []
for i in range(n):
    x = int(input())
    nums.append(x)

score1 = 0
score2 = 0
turn = 1  # Player 1 starts

while len(nums) > 0:
    if turn == 1:
        if nums[0] >= nums[-1]:
            score1 += nums[0]
            nums.pop(0)
        else:
            score1 += nums[-1]
            nums.pop()
        turn = 2
    else:
        if nums[0] >= nums[-1]:
            score2 += nums[0]
            nums.pop(0)
        else:
            score2 += nums[-1]
            nums.pop()
        turn = 1  

if score1 > score2:
    print("Player 1")
elif score2 > score1:
    print("Player 2")
else:
    print("tie")
