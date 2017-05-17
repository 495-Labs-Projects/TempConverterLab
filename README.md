# 495_tempconverter
## Temperature Converter Lab for 67495 F17

Re-creation of 67-272 lab 2A: TempConverter using Python. Two versions have been created, **one using structural programming**, and **one using object-oriented programming**

The *exp* branch contains the complete structional programming solution, whereas the *master* branch contains the partial structural programming solution and the complete object-oriented solution (may restructure eventually)

# Lab Writeup

# Part 1: Python (3) Introduction

Most of you should have had experience working with Python 3 in 15-112, but many of you may have forgotten Python syntax or have never programmed in Python before. With this in mind, this first half of the lab should help to refresh your memory in using Python both just chaining Python functions (a programming style referred to as "Structural Programming"), as well as using Python classes (a programming style referred to as "Object-Oriented Programming"). There are some 'on-your-own' resources at the end, so please be sure to take advantage of them for some extra Python practice. Knowing Python syntax, and knowing it well, will be important to being able to navigate this course.

1. We are going to begin by writing a simple Structural Programming Python script which will be able to convert temperatures and then modify this script to better understand Python syntax. Start by creating a file called `temp_converter_structural.py` using your preferred editor/IDE (perhaps in a new folder for this lab).

2. In this file, create a method called `convert` as follows:
```
def convert(temp):
  return 5 * (temp - 32) / 9
```

We also want to add some kind of output, so for now let's use some simple print statements below the function to see our conversion:

```
print(convert(32))
print(convert(50))
print(convert(212))
```

Run this code from the command line using the command `python3 temp_converter_structural.py`. You should get the output:
```
0
10
100
```
as the result in the terminal. Once you have this working, be sure to set up a Git repository and commit the file to it (ask a TA for help if you don't remember how to use Git!).

3. Now go into the function and remove the parenthesis to the right of 32 and rerun this code. Oh no, an error occurred! Fear not. Fix the error and we can check the fix before re-running using the command `python3 -m py_compile temp_converter_structural.py`. If you fixed it, nothing should output, otherwise there will be some error. Simply compiling and not running the Python code can be useful because it helps to find errors before they may show later during runtime.

4. Add the following test line to the print statement outputs:
```
print(convert("zero"))
```
Now re-run the code. Why did you get an error? To correct this, we will limit all temperatures to integers by adding a conditional to the top of the `convert` function:

```
if type(temp) != int:
  return "Temperature must be an integer"
```

Now re-run the code and notice the error should be fixed and the print statements output expected output. If this is the case, be sure to add the changes to the Git repository.

5. Add the line `print(convert(-500))` to the script and re-run. Of course, remembering your basic physics leaves you distressed at this point because you know this answer is in error – Absolute Zero is at –474 degrees Fahrenheit or -270 degrees Celsius, making this result impossible. To make sure our program doesn't give silly answers, we will add another line after the last correction (and before the calculation):

```
if temp < -474:
    return "Temperature below Absolute Zero"
```