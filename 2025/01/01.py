nums = [int(line.replace("L","-").replace("R","+")) for line in open("input.txt").read().splitlines()]
for i in range(len(nums) - 1):
    nums[i+1] += nums[i]
print(len([i for i in nums if i%100 == 50]))
print(sum(len([i for i in range((min(a,b)//100)*100-50, (max(a,b)//100)*100+150, 100) if i in range(a+1 if a<b else b, b+1 if a<b else a)]) for a,b in zip(nums, nums[1:])))
