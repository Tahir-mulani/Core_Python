base=int(input("Enter base"));
index=int(input("Enter index"));

p=1;
while index!=0:
		p=p*base;
		index-=1;
		
print("power is ",p);