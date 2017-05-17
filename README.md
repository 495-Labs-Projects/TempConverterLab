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