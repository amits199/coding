n=int(input("ente the number"))


for i in range(1,n+1):
    if n%i==0:
        factors=factors+[i]
     

if len(factors==2):
    print("yes the number is prime")
    
else:
    print("wrong input")

else:
    print("No number is not prime prime")

