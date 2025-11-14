#Write a program to print table between 2 to 10.
for i in range(1,11,1): #for(i=1,i<11;i++)
	for j in range(2,11,1):  #for(j=2,j<11;j++)
		print(i*j,end ="\t");  #it is part of inner loop.
		
	print();   #it is part of outer loop