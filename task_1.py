def nums_generator(max_num):
   for num in range(1, max_num + 1, 2):
       yield num


if __name__ == '__main__':
    nums = nums_generator(15)
    for i in nums:
        print(i)
