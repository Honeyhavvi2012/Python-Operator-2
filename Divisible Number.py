print("Enter a Number (Numerater)")
numn = int(input())
print("Enter a Number(denominater):")
numd = int(input())

if numn%numd==0:
    print("\n" +str(numn)+ "is divisible by" +str (numd))
else:
    print("\n" +str(numn)+ "is not divisible by" + str(numd))