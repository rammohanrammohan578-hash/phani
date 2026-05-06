i=12
n=0
while (i<=10):
    print(i,end=" ")
    n=n+i
    i=i+1
print(n)

print()
a=int(input("enter the number"))     
for x in  range(1,a):
    print(x,end="")
print()

start=int(input("enter the number start"))
end=int(input("enter the number stop"))
if start>end:
    print("start value should be greater than end value")
else:
    for x in  range(start,end):
        print(x,end=" ")
