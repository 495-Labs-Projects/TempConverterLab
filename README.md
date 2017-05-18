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

Re-run the code. Assuming the output is as expected, save the revision to the Git repository.

6. Of course, we have only half the temperature conversion problem – converting Fahrenheit to Celsius – and have no capability to convert Celsius to Fahrenheit. Create a new branch in git called `exp` (Again, ask a TA if you don't remember this from previous labs). Now in your code, add another argument called `measure` and using an `if ... else` construct, correct the code so that either a Fahrenheit or Celsius temperature is converted. Set up the `measure` argument so its default value is "F". Add the statements below:

```
print(convert(0, "C"))
print(convert(10, "C"))
print(convert(100, "C"))
print(convert(-280, "C"))
```

Re-run the code. Assuming the output is as expected, save the revision to the Git repository.

7. Looking at the results, we see that code is still problematic: we get a result for –280 oC even though we know that value is below Absolute Zero. There are a number of ways to correct this, but for learning purposes here, we are going to create a new method called is_below_absolute_zero which has two arguments: temp and measure. This method will simply return a boolean of true if the temperature for the measurement system is below the critical value. Create the basic structure for this method now.

Add the following code so your complete method looks like this:

```
def is_below_absolute_zero(temp, measure):
  return (temp < -454 and measure == "F") or (temp < -270 and measure == "C")
```

Note the use of boolean logic to check if our temperature is below Absolute Zero based on the measure. This will return `True` if the value is below Absolute Zero, and `False` otherwise. Furthermore, it will crash with non-integer temperatures (which we checked for in the `convert` method so we are safe here).

Rerun the code and make sure that everything is working properly. If so, save this code to the git repository. Checkout the `master` branch, and then merge the `exp` branch onto the `master` branch. (Again, ask a TA is you don't remember how to do this!)

## :exclamation: STOP
Show a TA that you have completed the structural temp conversion program and have properly saved the code to git. Make sure the TA initials your sheet.

# Part 2: Object-Oriented Programming

Python is inherently what is called an **Object-Oriented language**, meaning everything is packaged into what is called an *Object*, which is essentially an outline of a general thing. Classes have *attributes* and *methods*. An *attribute* is something an object has. It is some variable the object contains. A *method* is something an object can do. Here is a visual example:

```
class pythonClassExample(object):
    def __init__(self):
        self.x = 10

    def increment(self):
        self.x += 10
```

In this example, the class named `pythonClassExample` has both an *attribute* of `x` and a *method* of `increment`. Note that the *attribute* `x` persists, so the *method* `increment` is destructive and modifies `x`. We can create an instance of the `pythonClassExample` class by using the following statement:

```
newClassInstance = pythonClassExample()
```

Now the variable newClassInstance refers to an instance of the `pythonClassExample` class. The following code snippet illustrates how to work with Python classes, syntactically:

```
newClassInstance = pythonClassExample()
print(newClassInstance.x) # prints 10
newClassInstance.increment()
print(newClassInstance.x) # prints 20
```

Note that we do not pass any variables in for *self* when initializing or calling the `increment` function. This value refers to the class instance, which is indirectly passed using the `newClassInstance.<something>` syntax. Similarly, imagine we added the following method to the class:

```
def incrementBy(self, incrementValue):
  self.x += incrementValue

newClassInstance = pythonClassExample()
newClassInstance.incrementBy(5)
print(newClassInstance.x) # prints 15
```

This shows the syntax for passing arguments to a Python class method. Now, with this knowledge, we will write the same Temp Converter using such Object-Oriented techniques.

1. Create a new branch called `object_oriented` in your git repository and switch to it.

2. Create a new file called `temp_converter_object_oriented.py` and open it with your favorite editor/IDE.

3. Start by creating the general outline for a Python class:

```
class TempConverter(object):
  def __init__(self, initialTemp, measure='F'):
    return
```

4. Now write the `convert` and `is_below_absolute_zero` functions from the structural programming temp converter as class methods. Your general Python class will look like such:

```
class TempConverter(object):
  def __init__(self, temp, measure="F"):
    self.temp = temp
    self.measure = measure

  def convert(self):
    # converts the temperature from measure to the opposite

  def is_below_absolute_zero(self):
    # checks if the temperature is below absolute zero
```

The bodies for these methods will be similar to the functions you wrote before, but should call the class's values for `temp` and `measure`. You can check the expected behavior by adding the following code:

```
tempConverterObject = TempConverter(32, "C")
print(tempConverterObject.convert())
tempConverterObject.temp = 50
print(tempConverterObject.convert())
tempConverterObject.temp = 212
print(tempConverterObject.convert())
tempConverterObject.temp = "zero"
print(tempConverterObject.convert())
tempConverterObject.temp = -500
print(tempConverterObject.convert())
```

running the code in terminal, and seeing:

```
89.6
122.0
413.6
Temperature must be an integer
Temperature below Absolute Zero
```

5. Once you have confirmed the output is as expected, be sure to commit the code to git and then merge the `object_oriented` branch onto `master`.

## :exclamation: STOP
Show a TA that you have completed the Object-Oriented temp conversion program and have properly saved the code to git. Make sure the TA initials your sheet.