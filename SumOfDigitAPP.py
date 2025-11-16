#Write a Java program and compute the sum of an integer's digits.

no=993;

first=no//100;
middle=no//10;
last=no%10;
sum=first+middle+last;
print("Sum of digits: ",sum);
