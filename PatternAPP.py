# Write a pattern draw this pattern 
#  * * * * *
#    * * * *
#      * * *
#        * *
#          *

for i in range(1,6,1):  #for(i=1;i<=5;i++)
		for j in range(1,6,1):   #for(j=1;j<=5;j++)
			if i<=j:
				print("*",end="");
			else:
				print(end=" ");
		print();    #for outer loop new line