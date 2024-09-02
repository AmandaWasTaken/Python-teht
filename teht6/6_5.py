def evens_list(nums):
    evens = []
    for i in nums:
        if i % 2 == 0:
            evens.insert(i ,i)
    return evens

def main():
    nums = [1,2,3,4,5]
    evens = evens_list(nums)
    print(f"Alkuperäinen lista: {nums} "
          f"Muokattu lista: {evens}")

if __name__ == '__main__':
    main()