nums = [2,7,11,15]
target = 9

found =  False

for i_index,i in enumerate(nums):
    if not found:
        for j_index,j in enumerate(nums[i_index+1:],i_index+1):
            if i + j == target:
                found = True
                print([i_index,j_index])

# Good Read: https://leetcode.com/problems/two-sum/solutions/737092/sum-megapost-python3-solution-with-a-detailed-explanation/

