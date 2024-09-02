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

if len(nums) < 5:
    print("Anna vähintään viisi lukua! ")
    exit(1)

nums.sort(reverse=True)
print("Viisi suurinta lukua: ")
for i in range(5):
    print(nums[i])