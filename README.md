# IC-2k24-92-PythonLab-VaibhikaLot
# section D program documentation 

## 1. variable and identifier practise
* **Aim**: To declare variables of different data types (string, integer, float, boolean) and display their values along with their Python data types.
* **logic**: The program initializes four distinct variables with personal details and uses the built-in type function inside a print statement to identify and display each variable's data type.
* **sample input output**
```input: vaibhika 
          20
          5.2
          true
 output:vaibhika <class 'str'>
        20 <class 'int'>
        5.2 <class 'float'>
        True <class 'bool'>
        [Finished in 628ms] 
 ```
## 2. greeting program 
* **Aim**: To take multiple user inputs and print a single, formatted greeting sentence combining all the details.
* **logic**:  The program captures string inputs for personal details and uses an f-string to seamlessly inject these variables into a single sentence template.
* **sample input /output**
```input: vaibhika 
          20
          indore
output: my name is vaibhika, i am 20 year old, and i am from indore.
```
## 3. arithmetic operation
* **Aim**: To accept two numeric inputs from the user and perform basic mathematical calculations on them.
* **logic**: The program converts inputs to floats and applies standard arithmetic operators to calculate and display    the sum, difference, product, quotient, and remainder with clear labels.
* **sample input/output**
``` input:  enter first no.:23
            enter second no.:34
output: enter first no.:23
        enter second no.:34
        sum of A and B is 57
        differnce of A and B is -11
        product of A and B is 782 
        remainder of A and B is 23
        quotient of A and B is 0.6764705882352942
        [Finished in 5.5s]
```
## 4. celsius to fahrenheit
* **Aim**: To accept a temperature value in Celsius and convert it into its equivalent Fahrenheit value.
* **logic**:The program converts the user input into a floating-point number and applies the standard linear temperature conversion formula to calculate the final result.
* **sample input/output**
```input: temp: 55.7
output:  temprature in celcius is 55.7°C
         converted temprature is 132.26
```
## 5. string manipulation
* **Aim**: To take a user's full name as input and display it in uppercase, lowercase, reversed order, and show its total character length.
* **logic**: The program applies built-in string case methods, a slicing technique for reversal, and the character-counting function to manipulate the input text.
* **sample input/output**
```input: enter your full name: vaibhika
  output: name in upper case: VAIBHIKA
          name in lower case: vaibhika
          lenght of name: 8
          reversed name: akihbiav 
          [Finished in 6.0s]
```
## 6. escape sequence practise
* **Aim**: To format text dynamically into a clean, aligned transaction receipt or tabular structure without using external libraries.
* **logic**: The program utilizes specific text-formatting characters to insert vertical tab spaces and horizontal line breaks directly within standard print statements.
* **sample input/output**
```output: 
--------cash reciept--------

item name   		 price
---------   		------
dalmakhni   		350/-
paneer kofta		300/-
rumali roti 		15/-
jeera rice  		250/-
roasted papad 		30/-
green salad 		55/-
water bottle		30/-
---------------------

total:      		1030/-

Thankyou for visiting
[Finished in 711ms]
```
