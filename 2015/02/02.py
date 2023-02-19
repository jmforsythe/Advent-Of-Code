lines = open("input.txt").readlines()
paper = 0
ribbon = 0
for line in lines:
    nums = sorted([int(i) for i in line.split("x")])
    paper += 3*nums[0]*nums[1] + 2*nums[0]*nums[2] + 2*nums[1]*nums[2]
    ribbon += 2*(nums[0]+nums[1]) + nums[0]*nums[1]*nums[2]
print(paper)
print(ribbon)
