a = int(input("Enter a value:"))
b = int(input("Enter a value:"))
c = int(input("Enter a value:"))

avg = (a+b+c)/3
print("avg=", avg)

if avg> a and avg > b and avg > c:
    print("%d is higher than %d,%d,%d" %(avg, a, b, c))
