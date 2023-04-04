p=int(input("Enter principle amount\n"))
n=int(input("Enter number of years\n"))
s=input("Is customer senior citizen(y/n)\n")
if s=='y':
    r=12
else:
    r=10
i=(p*n*r)/100
print("Interest:",i)
