
def F1(number):
    max_digit = max(str(number));
    return int(max_digit);


def F2(number, max_digit):
    number_str = str(number);
    number_str = number_str.replace(str(max_digit), '', 1);
    return int(number_str) if number_str else 0;

def main():
    while True:
        number = input("Enter a 5 digits number: ");

        if number.isdigit() and len(number) == 5:
            number = int(number);
            break;
        else:
            print("It is not a 5 digits number, Please enter a valid number....!!!");

    max_digit = F1(number);
    print(f"The maximum digit is: {max_digit}");

    final_number = F2(number, max_digit);
    print(f"The final digit is: {final_number}");


if __name__ == "__main__":
    main();
