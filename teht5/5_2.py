nums = list()

number = input("Anna luku: ")
while True:
    if number == '':
        break
    else:
        number = int(number)
        nums.insert(0, number)
        number = input("Anna luku: ")
        continue

print("Viisi suurinta lukua: ")
nums.sort(reverse=True)
for i in range(5):
    print(nums[i])