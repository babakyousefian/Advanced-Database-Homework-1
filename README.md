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


