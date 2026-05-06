def add():
    print(a+b)
def sub():
    print(a-b)
def mult():
    print(a*b)
def div():
    print(a/b)
print("welcome")
flag="y"
while (flag=='y'):
  print("1-add")
  print("2-sub")
  print("3-multi")
  print("4-division")
  print("5-exit")
  choice=int(input("enter your choice:"))
  a=int(input("enter the value of a:"))
  b=int(input("enter the value of b:"))
  if choice==1:
   add()
  elif choice==2:
   sub()
  elif choice==3:
   mult()
  elif choice==4:
   div()
  else:
     print("goodbye")
  flag=input("do you want to coutinue(y/n)")
  print(flag)
  if (flag=="n"):
     print("thank you")

