#WAP to get a cube of number
def getCube(no):
    return no*no*no;

no=int(input("Enter Number\n"));
result = getCube(no);
print("Cube is ",result);