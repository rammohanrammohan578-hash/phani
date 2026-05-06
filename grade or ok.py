eng=float(input("enter eng marks:"))
math=float(input("enter eng marks:"))
sci=float(input("enter eng marks:"))
phy=float(input("enter eng marks:"))
che=float(input("enter eng marks:"))
computers=float(input("enter eng marks:"))
total=eng+math+sci+phy+che+computers
percentage=(total/500)*100
print("total marks = %.2f" %total)
print("marks percentage= %.2f" %percentage)
if(percentage >=98):
   print("A grade")
elif(percentage >=80):
   print("B grade")
elif (percentage >=70):
   print("A grade")
elif(percentage >=60):
   print("C grade")
elif(percentage >=50):
   print("A grade")
elif (percentage >=40):
   print("D grade")
else:
   print("ok")
           
