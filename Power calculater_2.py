base = int(input("Enter the base number:"))
power = int(input("Enter the power number:"))
answer = 1
for i in range(1, power + 1):
    answer = base * answer
print(answer)