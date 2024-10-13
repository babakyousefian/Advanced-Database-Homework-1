import time;

def print_pattern(n):
    for i in range(1, n+1 , 1):    # i=1 , i=2 , i=2 , i=3 , i=3 , i=3 , ... , i=8
        for j in range(1, i+1 , 1):# j=1 , j=1 , j=2 , j=1 , j=2 , j=3 , ... , j=8
            print(i * j, end="   ");
        print("\n");


n = int(input("Input: "));
print("\n\n");

time.sleep(1);

print_pattern(int(n));
