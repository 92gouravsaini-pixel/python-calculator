

n=float(input("enter a number n : "))
given_unit=input("enter a given_unit (Km/m/cm/mm)").lower()
output_unit=input("enter a output_unit(Km/m/cm/mm)").lower()

if given_unit=="km" :
    if output_unit=="m" :
        result=n*1000
        print(f"{result}{output_unit}")
    elif output_unit=="cm":
        result=n*100000
        print(f"{result}{output_unit}")
    elif output_unit=="mm":
        result=n*1000000
        print(f"{result}{output_unit}")
    elif output_unit=="dm":
        result=n*10,000
        print(f"{result}{output_unit}")
    else:
        print("Invalid input")
        exit()

elif given_unit=="m":
    if output_unit=="km":
        result=n/1000
        print(f"{result}{output_unit}")
    elif output_unit=="dm":
        result=n*10
        print(f"{result}{output_unit}")

    elif output_unit=="cm":
        result=n*100
        print(f"{result}{output_unit}")
    elif output_unit=="mm":
        resul=n*1000
        print(f"{result}{output_unit}")
    else:
        print("Invalid input")
        exit()

elif given_unit=="cm":
    if output_unit=="km":
        result=n/10000
        print(f"{result}{output_unit}")
    elif output_unit=="dm":
        result=n/10
        print(f"{result}{output_unit}")
    elif output_unit=="m":
        result=n/100
        print(f"{result}{output_unit}")
    elif output_unit=="mm":
        result=n*10
        print(f"{result}{output_unit}")
    else:
        print("Invalid input")
        exit()
elif given_unit=="mm":
    if output_unit=="km":
        result=n/1000000
        print(f"{result}{output_unit}")
    elif output_unit=="dm":
        result=n/100
        print(f"{result}{output_unit}")
    elif output_unit=="m":
        result=n/1000
        print(f"{result}{output_unit}")
    elif output_unit=="cm":
        result=n/10
        print(f"{result}{output_unit}")

else :
    print("Invalid input")
    exit()
