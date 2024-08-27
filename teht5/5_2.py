from types import NoneType

nums = []

while True:
    number = input("Anna luku: ")
    if number != '':
        number = int(number)
        nums.insert(number, int)
    else:
        break

for i in range(5):
    print(nums)