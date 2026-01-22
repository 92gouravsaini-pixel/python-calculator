import math
from selectors import SelectSelector

operator = input(" enter an operator for doning operation (+,-,%,*,^,$) : " )
print("for power=^ \n for under root= $ \n for reminder=%")
print("for sqrt you can two numbers at a time for sqrt but \nif you want only one no. sqrt then you can put any one of"
"them one")
a=float(input("enter a number a : ") )
b=float(input("enter a number b : "))
if operator== "+":
    result=a+b
    print(result)
elif operator=="-":
    if  a>b :
      result=a-b
      print(result)
    else :
        result=a-b
        print(f"-{result}")

elif operator == "*":
    if  a<0 or b<0 :
        result=-a*b
        print(result)
    else :
        result=a*b
        print(f"{result}")

elif  operator == "%" :
     result = a%b
     print(result)
elif operator == "^":
    print("a is base\n b is power")
    result=pow(a,b)
    print(result)

elif operator == "$":
  Aresult=math.sqrt(a)
  Bresult=math.sqrt(b)
  print(f"sqrt(a)= {Aresult} \n sqrt(b)={Bresult}")

else :
   print("invalid input")

print("thanks")
