no = int(input("enter number"));
rev=0;
print("before reverse ",no);
while no!=0:
		rem = no%10;   
		no = no//10;  # "//" --> for distract point.
		rev = rev*10+rem;
print("after reverse ",rev);
	