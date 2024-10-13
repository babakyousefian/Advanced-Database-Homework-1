import time;
def print_even_separated(number:(str)="0"):
    if not isinstance(number,str):
        raise TypeError("\n\n invalid inputs...!!!");
    else:
        result = list();

        for i in number:
            if int(i) % 2 == 0:
                result.append(i);
            else:
                continue;

        print("\n\n your output is : ",'*'.join(result));


number = input("\n\n please enter your number: ");

time.sleep(1);
print_even_separated(number);
