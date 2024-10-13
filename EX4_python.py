import time;

def print_even_digit_numbers():

    for i in range(100,999+1,1):

        num_str = str(i);

        if all(int(digit) % 2 == 0 for digit in num_str):
            print(i, sep=" " , end=", ");


time.sleep(1);

print_even_digit_numbers();
