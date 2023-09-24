# Trial and Error
*Author: Jeet Soni*

*Date: 09/24/2023*

---

### Description

Oh, do I love the clarity of reading an error. I absolutely enjoyed doing these exercises. I worked with handling the normal errors, file handling errors and also custom exceptions.

### Problems

**1. Write a Python program that takes two numbers as input from the user and calculates their division result. Use a try and except block to handle the case when the user enters 0 as the second number.**

I stored numerator and denominator input in two variables. Then, I used try and except block to try executing the divison `(numerator / denominator)`. If the user provides `0` for the denominator, the prgram will catch the `ZeroDivisionError` error in the except block and will let the user know that it can't divide by 0. 

**2. Write a Python program that attempts to read a file specified by the user. Handle the case where the file does not exist by displaying an error message.**

I created a text file with some data in it. In my python file, I asked user to provide us with the file name. After, I used try and except block to try to open the file and read the content. If the file doesn't exists then I catch the `FileNotFound` error in the except block and print a message saying "File was not found". 

**3. Write a Python program that asks the user for input and tries to convert it to an integer. Handle the case where the input is not a valid integer and display an error message.**

I created the variable `number` to store the user input. Then, I used try and except block to convert the number to `int` type. If user enters anything other than digits then the except block will catch `ValueError` and let the user know that their input is invalid and what is expected from them to enter. 

**4. Create a custom exception class called NegativeValueError. Write a function that takes a number as input and raises this custom exception if the number is negative. Then, write a program that calls this function and handles the custom exception.**

I created an empty `NegativeValueError` class and passed in `ValueError`. In my main python file, I created a function that will check if user enters negative number with `if statement`. If user does, then I used `raise` keyword to raise and called `NegativeValueError` class. In my main function, inside my `try and except` block, I took user input and stored it in a variable. I called my function and passed in the variable to check if the number is negative or not. If the number is negative, I catched the raised `NegativeValueError` in `except` block and let user know that the number they have entered is negative.  

---

Oh, this was fun really! I learned so much about the importance and usefulness of `try and except` in the real world. Now, When I get `"pretty"` errors and not `"nasty"` long code errors while filling out a form, I know how that's possible. 

Enjoy :)

Jeet



