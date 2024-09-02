def listsum(nums) -> int:
    nums_sum = 0
    for num in nums:
        nums_sum += num
    return nums_sum

def main():

    nums = [1,2,3,4,5]
    nums_sum = listsum(nums)
    print(f"Summa: {nums_sum}")

if __name__ == '__main__':
    main()
