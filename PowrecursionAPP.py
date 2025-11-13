#WAP to input two values first is base and second index calculate its power.
def power(base,index,p=1):
    if(index!=0):
        p=p*base;
        power(base,index-1,p);''
    else:
        print("power is ",p);

b=int(input("enter base value\n"));
ind=int(input("enter index value\n"));

power(b,ind)
    
    