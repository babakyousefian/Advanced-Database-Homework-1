#P1
def f1():
    # local variable
    s = "I live in khorramabad";
    print(s);
# Main
f1();

"""this above part is illustrating the local variable which means worked in their own block for instance 
s is a local variable in f1 function and  hasn't been detected in main method"""

#P2
def f2():
    # local variable
    s = "I live in khorramabad";
    print("Inside Function:",s);
#Main
f2();
print(s);

"""by moving subsequently forward to the next part can depict the local variable that can not work globally, means 
should you use the local variable , you couldn't use it in main method. this is why you declared in limit block like:
f2 function"""

#P3

def f3():
    global s;
    s = "I live in khorramabad";
    print(s);
# Main: Global Scope
s = "I live in Iran";
f3();
print(s);

"""on the other hand, the third part can deliniation the global variable which means : if you want to declared 
a global variable , you can use it in all of the body of your code, for instance : you can use global s in f3 
function or in main method and you can not change your amount"""

#P4

# This function uses global variables s
def f4():
    s = "I live in khorramabad";
    print(s);
#Main
s = "I live in Iran";
f4();
print(s);

"""to sum up, this part can demonstrate the global variable , which means : if you want to comment the 47th line
,you can see the amount of s in f4 function, if no, you can see the two dispersed amount of s"""