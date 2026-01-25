#{Where:p = Principal
#R = Rate of Interest (%)
# = Time (years)
#n = Number of times interest applied per year
#A = Final Amount
#CI = A − P}
print("which kind of interest you want to find \n if you want to find CI then write CI \n or if you want SI then write"
      "SI ")
INTEREST =input("Enter the name of your interest ").upper()
if INTEREST=="CI" :
    print("R = Rate of Interst(%) \n T = Time(years) \n n = Number of times interest applied per year \n A = Final Amount ")
    R=int(input("enter R : "))
    while R <0:
         print("You did not enter the rate of interest")
         R = int(input("enter R : "))
    T=int(input("enter T : "))
    while T=="":
         print("You did not enter the time")
         T = int(input("enter T : "))
    n=int(input("enter n : "))
    while n=="":
          print("you did not enter the number of interest per year ")
          n = int(input("enter n : "))
    P=int(input("Enter p : "))
    while P<0:
          print("You did not enter the principal")
          P = int(input("Enter p : "))
    S=R/(100*n)
    U=1+S
    W=n*T
    V = pow(U,W)

    A=P*V
    CI=A-P
    print(f"Total money you need to pay/recover = {A}")
    print(f"Your total compound interest = {CI} \n Thank you😊😊😊")


elif INTEREST=="SI" :
    #P = Principal (the original amount)
     #R = Rate of Interest (%)
     #T = Time (in years)
    print("P = principal \n R = Rate of Interest \n T = Time(years)")
    P=int(input("Enter P : "))
    while P<0:
        print("you did not enter the right value of principal")
        P = int(input("Enter P : "))
    R=int(input("Enter R : "))
    while R=="":
        print("you did not enter the value of rate of interest ")
        R = int(input("Enter R : "))
    T=int(input("Enter T : "))
    while T=="":
        print("you did not enter the time(years)")
        T = int(input("Enter T : "))

    SI=(P*R*T)/100
    A=P+SI
    print(f"total amount you need to pay/recover = {A} ")
    print(f"Total interest you need to recover or pay={SI}")
    print("Thank you ❤️😍👌🙏 ")

else :
    print("invalid input ")
    print("Thank you ❤️😍👌🙏 ")

