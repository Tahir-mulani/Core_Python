#Write a java program to enter marks of five subjects and calculate total marks and percentage.

print("Enter 5 subjects Marks");

s1=int(input("subject 1\n"));
s2=int(input("subject 2\n"));
s3=int(input("subject 3\n"));
s4=int(input("subject 4\n"));
s5=int(input("subject 5\n"));

total=(s1+s2+s3+s4+s5);
percentage=total/5;

print("Total Marks: ",total,"\nTotal Percentage: ",percentage);