#nums = [4, 9 ,2, 6]
nums = []
how_many = int(input("How many numbers do you wish to enter: "))
for i in range(how_many):
    num = int(input("Enter a number: "))
    nums.append(num)
    
total = 0
for i in range(len(nums)):
    num = nums[i]
    total = num + total
avg = total/ len(nums)
#avg = (num[0] + num[1] + num[2])/len(nums)
print(avg)


the_max = 0
for num in nums:
    if num > the_max:
        the_max = num
    
print(the_max)

#Booooooooooo I forgot to save the rest of this before moving it

