# Write a java program to enter two angles of a triangle and find the third angle.

a1=int(input("Enter First Angle"));
a2=int(input("Enter Second Angle"));

#a1+a2+a3=180

a3=180-(a1+a2);
print("Third Angle is: ",a3);
