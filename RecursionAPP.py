#WAP print statement with using recursive.
def show(no):
    if(no==0):  #base Case
        print("End");
    else:
        print("Good Morning");
        show(no-1);   #recursive call

show(5)    #initial call