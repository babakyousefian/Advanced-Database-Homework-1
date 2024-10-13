def factorial(x):
    if x == 1:# this is the base case
        return 1;
    else:# this is the recursive case
        return (x*factorial(x-1));

print(factorial(4));

"""the recursive function is call their major own method in their own block"""