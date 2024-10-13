# Advanced-Database-Homework-1
Advanced Database Homework 1 - Python Basic Programming - Deadline: 1403/07/23


# Project Title

[![GitHub stars](https://img.shields.io/github/stars/your-username/your-repository.svg?style=social)](https://github.com/your-username/your-repository) 
[![GitHub forks](https://img.shields.io/github/forks/your-username/your-repository.svg?style=social)](https://github.com/your-username/your-repository/network)
[![GitHub license](https://img.shields.io/github/license/your-username/your-repository.svg)](https://github.com/your-username/your-repository/blob/main/LICENSE)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Visualizations](#visualizations)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction
A brief introduction of the project. the first homework python language project for Advanced Database lesson within Proffessor.Rashno

## Features
- Feature 1: immediately level of python programming.
- Feature 2: immediately level of data structure of python programming.
- Feature 3: imeddiately level of explain of python programming.

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/babakyousefian/Advanced-Database-Homework-1.git

---

cd your-repository

---

pip install -r requirements.txt


---

python script_name.py


---


### Tips for using this Markdown:

Feel free to adjust it based on my own project details. This will help create a visually appealing and informative GitHub README file.
created by babak yousefian.


---

# i would rather describe all of this project at this place:
---
## first project:


# Python Program to Print Even Numbers Separated by Asterisk (`*`)

## Overview
This Python script takes a string of digits as input from the user and prints only the even digits from that input, separated by an asterisk (`*`). The code is structured to handle invalid input types and uses basic control flow to achieve the desired output.

## Code Explanation

### 1. **Imports**
```python
import time;
```
- The `time` module is imported to simulate a small delay before the function call using `time.sleep()`. This doesn't impact the logic of the program, but adds a brief pause to the output.

### 2. **Function Definition**

```python
def print_even_separated(number:(str)="0"):
```
- The function `print_even_separated` is defined to take a single argument, `number`. The type hint `(str)` is specified for this parameter, indicating that it expects a string input. The default value is set to `"0"`.
  
#### Input Validation
```python
if not isinstance(number,str):
    raise TypeError("\n\n invalid inputs...!!!");
```
- The first condition checks whether the `number` parameter is of type `str`. If not, a `TypeError` is raised with the message `"invalid inputs...!!!"`.

#### Main Logic
```python
else:
    result = list();
```
- An empty list named `result` is initialized. This list will store the even digits from the input.

#### Iteration Through Input
```python
for i in number:
    if int(i) % 2 == 0:
        result.append(i);
    else:
        continue;
```
- The program loops through each character (`i`) in the input string `number`.
- Each character is converted into an integer using `int(i)`.
- The modulo operator (`%`) is used to check if the number is even. If `int(i) % 2 == 0`, the digit is added to the `result` list.
- If the number is odd, the `continue` statement is used to skip to the next iteration.

#### Printing the Result
```python
print("\n\n your output is : ",'*'.join(result));
```
- After the loop completes, the `join()` function is used to concatenate the even digits stored in `result` with an asterisk (`*`) as the separator.
- The formatted string `"\n\n your output is : "` is printed, followed by the joined result of even numbers.

### 3. **User Input and Function Call**
```python
number = input("\n\n please enter your number: ");
time.sleep(1);
print_even_separated(number);
```
- The program prompts the user to input a number using `input()`. The input is read as a string.
- `time.sleep(1)` adds a 1-second delay for effect before calling the `print_even_separated` function.
- The function is called with the user's input (`number`).

## Example
### Input:
```
please enter your number: 123456789
```

### Output:
```
your output is : 2*4*6*8
```

## Error Handling
If the input provided to the function is not a string, the program raises a `TypeError` with a custom error message, ensuring the program handles invalid types gracefully.

## How to Run
1. Copy the code into a Python file (e.g., `even_numbers.py`).
2. Run the script using Python:
   ```
   python even_numbers.py
   ```
3. Enter a sequence of numbers when prompted, and the program will display the even numbers separated by an asterisk (`*`).

## Requirements
- Python 3.x
- No additional libraries are required except for the built-in `time` module.

## License
This project is licensed under the MIT License.


---
---
---
# second project


# Python Program for Computing a Mathematical Expression with Factorials and Decimal Arithmetic

## Overview
This Python script computes a mathematical expression involving factorials and decimal arithmetic with high precision. The precision of decimal calculations is set to 1000 decimal places using the `decimal` module. The user is prompted to enter a number `n`, and the program computes a mathematical expression based on `n` terms.

## Code Explanation

### 1. **Imports**
```python
import time
from decimal import Decimal, getcontext
```
- The `time` module is imported to introduce a delay before printing the result.
- The `decimal` module is imported to handle high-precision decimal arithmetic.
- `getcontext().prec = 1000` sets the precision of decimal calculations to 1000 decimal places.

### 2. **Factorial Function**

```python
def Factorial(n: int) -> int:
```
- The `Factorial` function takes an integer `n` and returns the factorial of `n`.
- The function raises a `TypeError` if the input is not an integer.
- The factorial is calculated iteratively using a loop, multiplying values from 2 to `n`.

#### Input Validation
```python
if not isinstance(n, int):
    raise TypeError("\n\n An ERROR occurred...!!!")
```
- This ensures that the input is of type `int`. If not, a `TypeError` is raised with a custom message.

#### Main Logic
```python
fact = 1
if n == 0 or n == 1:
    return 1
else:
    for i in range(2, n+1, 1):
        fact *= i
```
- If `n` is 0 or 1, the function returns 1 (since 0! = 1! = 1).
- Otherwise, the function calculates the factorial using a loop.

### 3. **Computing the Expression**

```python
def compute_expression(n):
```
- The `compute_expression` function computes a sum based on a mathematical series involving factorials.
- It initializes the result as `Decimal(0)` to ensure that all calculations are done with high precision.

#### Variables
```python
result = Decimal(0)
sign = 1
```
- `result`: Holds the cumulative result of the series.
- `sign`: Alternates between `1` and `-1` to account for alternating terms in the series.

#### Iterating Through the Series
```python
for i in range(0, n+1, 1):
```
- The loop runs from 0 to `n`, calculating each term in the series.

#### Factorial Part and Divisor Calculation
```python
factorial_part = ((2 * i) + 3)
divisor = Decimal(i + 2)
constant = Decimal(9 - (2 * i))
```
- `factorial_part`: The value for which the factorial is computed in the current term.
- `divisor`: One part of the denominator.
- `constant`: Another part of the denominator.

#### Handling Division by Zero
```python
if divisor + constant == 0:
    print(f"Skipping division by zero at term {i}")
    continue
```
- If `divisor + constant` equals 0, the program skips that term to avoid division by zero.

#### Term Calculation and Alternating Signs
```python
term = (Decimal(Factorial(factorial_part))) / (divisor + constant)
result += sign * term
sign *= -1
```
- The current term is calculated as the factorial of `factorial_part` divided by the sum of `divisor` and `constant`.
- The term is added to `result`, with the sign alternating between positive and negative.

### 4. **Main Program Flow**

```python
n = input("\n\nPlease enter your number to calculate it: ")
n = int(float(n))
```
- The program prompts the user to input a number, which is converted to an integer.

```python
result = compute_expression(n)
time.sleep(1)
print(f"Result for the first {n} terms: {result}")
```
- The `compute_expression` function is called to compute the result for `n` terms.
- The result is printed after a 1-second delay.

## Example
### Input:
```
Please enter your number to calculate it: 5
```

### Output:
```
Result for the first 5 terms: <computed_result>
```

## Error Handling
- If the input is not an integer, the program raises a `TypeError`.
- If a term would involve division by zero, the program prints a warning and skips that term.

## How to Run
1. Copy the code into a Python file (e.g., `factorial_expression.py`).
2. Run the script using Python:
   ```
   python factorial_expression.py
   ```
3. Enter a number when prompted, and the program will compute the result for that number of terms.

## Requirements
- Python 3.x
- No additional libraries are required except for the built-in `decimal` and `time` modules.

## License
This project is licensed under the MIT License.



---
---
---

# third project



# Python Program to Print All 4-Digit Numbers Matching a Condition

## Overview
This Python script prints all 4-digit numbers between 1000 and 9999 where the sum of the last two digits equals the product of the first two digits. The program iterates through each number in the specified range and checks this condition.

## Code Explanation

### 1. **Function Definition**

```python
def print_All_4_Digits():
```
- The function `print_All_4_Digits` is defined to find and print all 4-digit numbers that meet the specified condition.

### 2. **Variable Initialization**
```python
l = list();
p1 = 0;
p2 = 0;
```
- An empty list `l` is initialized to store the digits of the current number being evaluated.
- `p1` and `p2` are initialized to 0. These variables will store:
  - `p1`: The sum of the last two digits.
  - `p2`: The product of the first two digits.

### 3. **Main Loop**
```python
for i in range(1000, 9999+1, 1):
```
- The loop iterates through all numbers between 1000 and 9999 inclusive. For each number, it:
  - Converts the number to a string.
  - Extracts each digit of the number to perform the necessary calculations.

#### Extracting Digits
```python
l = list(str(i));
```
- The current number `i` is converted to a string, and each digit is stored in the list `l`.

#### Calculating the Conditions
```python
p1 = int(int(l[len(str(i))-1]) + int(l[len(str(i))-2]));
p2 = int(int(l[0]) * int(l[1]));
```
- `p1`: The sum of the last two digits of the number. The last digit is `l[len(str(i))-1]` and the second-to-last digit is `l[len(str(i))-2]`.
- `p2`: The product of the first two digits. The first digit is `l[0]` and the second digit is `l[1]`.

### 4. **Condition Check and Output**
```python
if p1 == p2:
    print(str(i), sep=" ", end=" ");
else:
    continue;
```
- If the sum of the last two digits (`p1`) is equal to the product of the first two digits (`p2`), the number is printed.
- Otherwise, the loop continues to the next number.

### 5. **Calling the Function**
```python
print_All_4_Digits();
```
- The `print_All_4_Digits` function is called to execute the program and print the matching numbers.

### Example

The output of the program will print 4-digit numbers where the sum of the last two digits equals the product of the first two digits.

#### Example Output:
```
1278 1368 1458 ...
```

## How to Run
1. Copy the code into a Python file (e.g., `four_digit_numbers.py`).
2. Run the script using Python:
   ```
   python four_digit_numbers.py
   ```

## Requirements
- Python 3.x
- No additional libraries are required.

## License
This project is licensed under the MIT License.



---
---
---

# fourth project

readme_content = """

# Even Digit Numbers Finder



This Python script identifies and prints all three-digit numbers (from 100 to 999) that consist exclusively of even digits. 



## Features



- The script iterates through all three-digit numbers.

- It checks if all digits in the number are even.

- It prints the valid even digit numbers in a comma-separated format.



## Code Explanation



### Importing Required Modules



```python

import time

The time module is imported to introduce a delay before executing the main function, enhancing user experience.
Defining the Function

python
Always show details

def print_even_digit_numbers():

This function, print_even_digit_numbers, is responsible for finding and printing the even-digit numbers.
Looping Through Numbers

python
Always show details

for i in range(100, 999 + 1, 1):

The loop iterates through the range of three-digit numbers, starting from 100 to 999.
Converting Numbers to Strings

python
Always show details

num_str = str(i)

Each number is converted to a string to facilitate digit-wise checking.
Checking for Even Digits

python
Always show details

if all(int(digit) % 2 == 0 for digit in num_str):

The all() function checks if every digit in the number is even. The condition int(digit) % 2 == 0 ensures that the digit is an even number.
Printing the Result

python
Always show details

print(i, sep=", ", end=", ")

If the number consists of all even digits, it is printed in a comma-separated format.
Delay Before Execution

python
Always show details

time.sleep(1)

A 1-second delay is introduced before executing the function to provide a pause for the user.
Executing the Function

python
Always show details

print_even_digit_numbers()

Finally, the function is called to execute the defined operations.
Usage

To run the script, simply execute the Python file in an environment that supports Python 3.x. The output will be displayed in the console.
Output Example

The output will list all three-digit numbers made up solely of even digits, like:

Always show details

200, 202, 204, 206, 208, 220, ...

Conclusion

This script is a simple yet effective way to explore numeric properties and can be further modified to include additional features such as counting the total even-digit numbers or saving the output to a file. """
Save the content to a README.md file

readme_path = '/mnt/data/README.md' with open(readme_path, 'w') as readme_file: readme_file.write(readme_content)

readme_path



#

```

---
---
---

# fivth project

readme_content = """

# Pattern Generator



This Python script generates and prints a numerical pattern based on the user's input. The pattern is formed by multiplying the row number by the column number, creating a visually appealing output.



## Features



- The user can input a positive integer, which defines the size of the pattern.

- The script generates a triangular pattern of numbers, where each row contains products of the row number and column numbers.



## Code Explanation



### Importing Required Modules



```python

import time

The time module is imported to introduce a delay before executing the main function, enhancing user experience.
Defining the Function

python
Always show details

def print_pattern(n):

This function, print_pattern, is responsible for generating and printing the number pattern based on the input integer n.
Looping Through Rows

python
Always show details

for i in range(1, n + 1, 1):

This loop iterates through the range from 1 to n, representing the current row number. For each row, the value of i represents the row number.
Looping Through Columns

python
Always show details

for j in range(1, i + 1, 1):

This nested loop iterates through the range from 1 to i, representing the current column number. The value of j determines how many numbers will be printed in each row.
Printing the Pattern

python
Always show details

print(i * j, end="   ")

For each combination of i (row number) and j (column number), the product i * j is calculated and printed with a space for formatting. The end=" " parameter ensures that the printed values remain on the same line, separated by spaces.
Adding a Newline After Each Row

python
Always show details

print("\n")

After printing all columns for a particular row, a newline character is printed to move to the next line.
User Input

python
Always show details

n = int(input("Input: "))

The script prompts the user to input a positive integer, which will be used to determine the size of the pattern.
Delay Before Execution

python
Always show details

time.sleep(1)

A 1-second delay is introduced before executing the function to provide a pause for the user.
Executing the Function

python
Always show details

print_pattern(int(n))

Finally, the function is called with the user's input, generating the desired pattern.
Usage

To run the script, simply execute the Python file in an environment that supports Python 3.x. The user will be prompted to enter a positive integer. The output pattern will be displayed in the console.
Output Example

If the user inputs 5, the output will look like:

Always show details

1   

2   4   

3   6   9   

4   8   12   16   

5   10   15   20   25   

Conclusion

This script is a simple yet effective way to visualize multiplication in a triangular format and can be further modified to include additional features such as changing the pattern style or adding more complex mathematical operations. """
Save the content to a README.md file

readme_path = '/mnt/data/README.md' with open(readme_path, 'w') as readme_file: readme_file.write(readme_content)
```


---
---
---

# sixth project

readme_content = """

# Statistical Calculator



This Python script calculates various statistical metrics such as maximum, minimum, average, variance, and standard deviation for a user-defined number of inputs. The user is prompted to enter a series of integers, which are then processed to produce the desired statistics.



## Features



- Accepts a user-defined number of integer inputs.

- Calculates and prints:

  - Maximum value

  - Minimum value

  - Average

  - Variance

  - Standard Deviation



## Code Explanation



### Importing Required Modules



```python

from math import sqrt

The sqrt function from the math module is imported to calculate the square root, which is used to compute the standard deviation.
Defining the Function

python
Always show details

def calculateN(n: (int) = 0):

This function, calculateN, accepts an integer n, representing the number of inputs the user will provide.
Input Validation

python
Always show details

if not isinstance(n, int):

    raise TypeError("\n\n invalid inputs...!!!")

The function checks if the input n is an integer. If it is not, a TypeError is raised.
Variable Initialization

python
Always show details

l = []

maximum = 0

average = 0.00

sum = 0.00

Several variables are initialized:

    l: a list to store the user inputs.
    maximum, average, sum: variables to hold computed statistics.

Collecting User Inputs

python
Always show details

for i in range(0, n, 1):

    l.append(int(input("\nEnter number " + str(i + 1) + ": ")))

The script prompts the user to input n numbers, which are appended to the list l.
Finding Minimum and Maximum Values

python
Always show details

minimum = l[0]

for i in l:

    if i > maximum:

        maximum = i

    elif i < minimum:

        minimum = i

The script initializes the minimum value to the first element of the list. It then iterates through the list to find the maximum and minimum values.
Calculating Sum and Average

python
Always show details

for i in l:

    sum += i

average = sum / len(l)

The script calculates the sum of all elements in the list and then computes the average by dividing the sum by the number of inputs.
Calculating Variance and Standard Deviation

python
Always show details

N = len(l)

mu = float(average)

variance_sum = 0

for i in l:

    variance_sum += ((i - mu) ** 2)

variance = variance_sum / N

standard_deviation = sqrt(variance)

The variance is calculated using the formula Variance=∑(xi−μ)2NVariance=N∑(xi​−μ)2​. The standard deviation is then obtained by taking the square root of the variance.
Printing the Results

python
Always show details

print("\n\n Maximum is: ", maximum)

print("\n\n Minimum is: ", minimum)

print("\n\n Average is: ", average)

print("\n\n Standard Deviation is: ", standard_deviation)

Finally, the computed statistics are printed to the console.
User Input for Number of Values

python
Always show details

n = int(input("\n\n Enter the n: "))

calculateN(n)

The script prompts the user to enter the number of values (n) to process and calls the calculateN function.
Usage

To run the script, simply execute the Python file in an environment that supports Python 3.x. The user will be prompted to enter how many numbers they wish to input, followed by the actual numbers. The output will display the maximum, minimum, average, variance, and standard deviation of the provided numbers.
Example

If the user inputs 5 for n and then enters the numbers 10, 20, 30, 40, and 50, the output will be:

csharp
Always show details

Maximum is:  50

Minimum is:  10

Average is:  30.0

Standard Deviation is:  14.142135623730951

Conclusion

This script provides a straightforward way to calculate basic statistical measures for a set of integers and can be modified to accommodate additional features or input types. """
Save the content to a README.md file

readme_path = '/mnt/data/README.md' with open(readme_path, 'w') as readme_file: readme_file.write(readme_content)

```


---
---
---

# seventh project

readme_content = """

# Statistical Analysis Tool



This Python script provides a set of functions to perform basic statistical analysis on a list of numbers inputted by the user. The tool calculates the maximum, minimum, average, and standard deviation of the provided numbers.



## Features



- Accepts a user-defined number of integer inputs.

- Calculates and displays:

  - Maximum value

  - Minimum value

  - Average

  - Standard Deviation



## Code Explanation



### Importing Required Modules



```python

import time

from math import pow, sqrt

The time module is imported to introduce delays between calculations for better readability of the output. The pow and sqrt functions from the math module are used for mathematical operations.
Function Definitions
Maximum Function

python
Always show details

def Max1(l: (list) = []) -> int:

This function accepts a list l and returns the maximum value in the list. It checks if the input is a list and iterates through the list to find the maximum value.
Minimum Function

python
Always show details

def Min1(l: (list) = []) -> int:

This function accepts a list l and returns the minimum value in the list. It also checks for list validity and iterates to find the minimum value.
Average Function

python
Always show details

def Ave1(l: (list) = []):

This function computes the average of the numbers in the list l. It calculates the sum of the elements and divides by the length of the list. The result is printed to the console.
Standard Deviation Function

python
Always show details

def STD1(l: (list) = []):

This function calculates the standard deviation of the list l. It computes the average first, then calculates the variance, and finally takes the square root of the variance to find the standard deviation. The result is printed to the console.
User Input

python
Always show details

n = int(input("\\n\\n Enter the n: "))

The script prompts the user to input the number of integers they wish to analyze.
Collecting User Inputs

python
Always show details

l = list()

for i in range(0, n, 1):

    l.append(int(input("\\n\\n Enter number" + str(i + 1) + ": ")))

The script collects n integers from the user and stores them in a list l.
Function Calls and Outputs

    The script calls the Max1, Min1, Ave1, and STD1 functions sequentially to compute and display the maximum, minimum, average, and standard deviation of the numbers inputted by the user.
    Delays of 1 second (time.sleep(1)) are introduced between outputs for clarity.

Usage

To run the script, execute the Python file in an environment that supports Python 3.x. The user will be prompted to enter the number of values they wish to input, followed by the actual numbers. The script will then display the maximum, minimum, average, and standard deviation of the provided numbers.
Example

If the user inputs 5 for n and then enters the numbers 10, 20, 30, 40, and 50, the output will be:

csharp
Always show details

Maximum is:  50



Minimum is:  10



Average is:  30.0



Standard Deviation is:  14.142135623730951

Conclusion

This script provides a simple yet effective way to calculate basic statistical measures for a set of integers. It can be easily modified or expanded to accommodate additional statistical functions or input types. """
Save the content to a README.md file

readme_path = '/mnt/data/README.md' with open(readme_path, 'w') as readme_file: readme_file.write(readme_content)
```


---
---
---

# 8th project

readme_content = """

# Digit Manipulation Tool



This Python script takes a five-digit number as input from the user and performs operations to find the maximum digit and create a new number by removing the first occurrence of that maximum digit from the original number.



## Features



- Accepts a five-digit number from the user.

- Finds and displays the maximum digit in the number.

- Generates and displays a new number by removing the first occurrence of the maximum digit.



## Code Explanation



### Function Definitions



#### Find Maximum Digit



```python

def F1(number):

    max_digit = max(str(number))

    return int(max_digit)

    Purpose: This function takes a number as input, converts it to a string, and finds the maximum digit in that number. The maximum digit is returned as an integer.
    Parameters:
        number: The integer input from which the maximum digit is to be found.
    Returns: The maximum digit as an integer.

Remove Maximum Digit

python
Always show details

def F2(number, max_digit):

    number_str = str(number)

    number_str = number_str.replace(str(max_digit), '', 1)

    return int(number_str) if number_str else 0

    Purpose: This function takes the original number and the maximum digit as input. It removes the first occurrence of the maximum digit from the number and returns the new number.
    Parameters:
        number: The original integer input.
        max_digit: The maximum digit to be removed from the original number.
    Returns: The new number after removing the maximum digit as an integer. If the result is an empty string, it returns 0.

Main Function

python
Always show details

def main():

    while True:

        number = input("Enter a 5 digits number: ")



        if number.isdigit() and len(number) == 5:

            number = int(number)

            break

        else:

            print("It is not a 5 digits number, Please enter a valid number....!!!")



    max_digit = F1(number)

    print(f"The maximum digit is: {max_digit}")



    final_number = F2(number, max_digit)

    print(f"The final digit is: {final_number}")

    Purpose: The main function manages user input and coordinates the overall flow of the program. It repeatedly prompts the user to enter a five-digit number until a valid input is received.
    Process:
        The user is asked to enter a five-digit number.
        The input is validated to ensure it is a digit and has a length of five.
        If valid, the maximum digit is found using F1, and the result is printed.
        The final number is generated using F2, and the result is printed.

Script Entry Point

python
Always show details

if __name__ == "__main__":

    main()

    This conditional checks if the script is being run as the main module and calls the main() function to start the program.

Usage

To run the script, execute the Python file in an environment that supports Python 3.x. The user will be prompted to enter a five-digit number, and the program will then display the maximum digit and the new number after removing that digit.
Example

If the user inputs 54321, the output will be:

kotlin
Always show details

The maximum digit is: 5

The final digit is: 4321

If the user inputs 12234, the output will be:

kotlin
Always show details

The maximum digit is: 4

The final digit is: 1232

Conclusion

This script provides a simple utility for manipulating five-digit numbers by finding and removing the maximum digit. It can be modified to handle different types of number manipulations or extended to accommodate additional functionalities. """
Save the content to a README.md file

readme_path = '/mnt/data/README.md' with open(readme_path, 'w') as readme_file: readme_file.write(readme_content)
```

---
---
---


# 9th project

readme_content = """

# Variable Scope Demonstration



This Python script illustrates the concept of variable scope in programming, specifically focusing on local and global variables. It demonstrates how local variables function within their defined scopes and how global variables can be accessed throughout the code.



## Code Explanation



The code is divided into four parts, each highlighting different aspects of variable scope.



### Part 1: Local Variable



```python

def f1():

    # local variable

    s = "I live in khorramabad"

    print(s)



# Main

f1()

    Description: This part defines a function f1() that contains a local variable s. The variable s is only accessible within the f1() function. When called, it prints the value of s.
    Output:

    css
    Always show details

    I live in khorramabad

    Explanation: The variable s in this function does not exist outside of it. Therefore, it cannot be accessed in the main block.

Part 2: Local Variable with Print Outside Function

python
Always show details

def f2():

    # local variable

    s = "I live in khorramabad"

    print("Inside Function:", s)



# Main

f2()

print(s)

    Description: This part defines a function f2() that also contains a local variable s. It prints the value of s from within the function.
    Output:

    mathematica
    Always show details

    Inside Function: I live in khorramabad

    Explanation: The code attempts to print s outside of the function, which will result in a NameError because s is not defined in the global scope.

Part 3: Global Variable

python
Always show details

def f3():

    global s

    s = "I live in khorramabad"

    print(s)



# Main: Global Scope

s = "I live in Iran"

f3()

print(s)

    Description: This part defines a function f3() that declares s as a global variable. The function assigns a new value to s and prints it.
    Output:

    css
    Always show details

    I live in khorramabad

    I live in khorramabad

    Explanation: The global keyword allows the function to modify the variable s that was defined in the global scope. The modified value of s persists outside of the function.

Part 4: Global Variable Demonstration

python
Always show details

def f4():

    s = "I live in khorramabad"

    print(s)



# Main

s = "I live in Iran"

f4()

print(s)

    Description: This part defines a function f4() that uses a local variable s. It prints the value of s defined within the function.
    Output:

    css
    Always show details

    I live in khorramabad

    I live in Iran

    Explanation: In this case, s inside f4() is a local variable and does not affect the global variable s. If the line that prints s within the function is commented out, the global variable s would still be printed with its value from the main scope.

Conclusion

This script effectively demonstrates the difference between local and global variable scopes in Python. Understanding these concepts is crucial for writing code that behaves as intended, particularly when managing variable accessibility across different functions and the main program. """
Save the content to a README.md file

readme_path = '/mnt/data/README.md' with open(readme_path, 'w') as readme_file: readme_file.write(readme_content)
```

---
---
---

# 10th project

readme_factorial_content = """

# Factorial Calculation Using Recursion



This Python script demonstrates the use of a recursive function to calculate the factorial of a given number. The factorial of a non-negative integer \( n \) is the product of all positive integers less than or equal to \( n \). The factorial is denoted by \( n! \).



## Code Explanation



The code defines a recursive function named `factorial` that calculates the factorial of a given number. 



### Function Definition



```python

def factorial(x):

    if x == 1:  # this is the base case

        return 1

    else:  # this is the recursive case

        return (x * factorial(x - 1))

    Parameters:
        x: A non-negative integer whose factorial is to be calculated.

    Base Case:
        The base case of the recursion occurs when xx equals 1. The function returns 1 because the factorial of 1 is defined as 1. This prevents the recursion from continuing indefinitely.

    Recursive Case:
        If xx is greater than 1, the function calls itself with the argument x−1x−1. This effectively breaks down the problem into smaller instances, multiplying xx by the factorial of x−1x−1.

Example Usage

python
Always show details

print(factorial(4))

    This line calls the factorial function with an argument of 4.
    Output:

    Always show details

    24

    Explanation: The calculation proceeds as follows:
        4!=4×3!4!=4×3!
        3!=3×2!3!=3×2!
        2!=2×1!2!=2×1!
        1!=11!=1

Combining these results, we have:

    4!=4×3×2×1=244!=4×3×2×1=24

Conclusion

This script effectively demonstrates the concept of recursion in programming, showing how a function can call itself to solve a problem. The use of a base case ensures that the recursion terminates correctly, making it a powerful technique for solving problems like factorial calculation. """
Save the content to a README.md file

readme_factorial_path = '/mnt/data/README_Factorial.md' with open(readme_factorial_path, 'w') as readme_file: readme_file.write(readme_factorial_content)
```

---
---
---

### Author babak yousefian
