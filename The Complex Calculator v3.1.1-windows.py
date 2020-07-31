#The Complex Calculator v3.0.0 by CMPLX

#Modules

from math import *
from os import *
import time as t
from statistics import *
import random as r

#Global Variables
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
pi = 3.14159265359
PI = pi
Pi = pi
pI = pi
π = pi

#Functions >> Prime Numbers

def prm(x):
  if x <= 1:
    return (1 / 0)
  else:
    factorList = []
    factorCheck = 2
    while factorCheck < x:
      if x % factorCheck == 0 and factorCheck < x:
        factorList.append(int(x / factorCheck))
        factorCheck = factorCheck + 1
        continue
      elif x % factorCheck != 0 and factorCheck < x:
        factorCheck = factorCheck + 1
        continue
      else:
        break
    if len(factorList) == 0:
      return "That number was prime"
    else:
      z = ("That number was composite, here are its factors: " + str(factorList))
      return z
#Functions >> Factorial

def fact(x):
  while x == "a":
    x = a
    break
  while x == "b":
    x = b
    break
  while x == "c":
    x = c
    break
  while x == "d":
    x = d
    break
  while x == "e":
    x = e
    break
  while x == "f":
    x = f
    break
  return factorial(x)

#Functions >> Root

def rt(x, n):
  while x == "pi" or x == "Pi" or x == "PI" or x == "pI" or x == "π":
    x = pi
    break
  while n == "pi" or n == "Pi" or n == "PI" or n == "pI" or n == "π":
    n = pi
    break
  while x == "a":
    x = a
    break
  while x == "b":
    x = b
    break
  while x == "c":
    x = c
    break
  while x == "d":
    x = d
    break
  while x == "e":
    x = e
    break
  while x == "f":
    x = f
    break
  while n == "a":
    n = a
    break
  while n == "b":
    n = b
    break
  while n == "c":
    n = c
    break
  while n == "d":
    n = d
    break
  while n == "e":
    n = e
    break
  while n == "f":
    n = f
    break
  z = x ** (1 / n)
  return z

#Functions >> Random Number Generation

def rand(x, n):
  while x == "pi" or x == "Pi" or x == "PI" or x == "pI" or x == "π":
    x = pi
    break
  while n == "pi" or n == "Pi" or n == "PI" or n == "pI" or n == "π":
    n = pi
    break
  while x == "a":
    x = a
    break
  while x == "b":
    x = b
    break
  while x == "c":
    x = c
    break
  while x == "d":
    x = d
    break
  while x == "e":
    x = e
    break
  while x == "f":
    x = f
    break
  while n == "a":
    n = a
    break
  while n == "b":
    n = b
    break
  while n == "c":
    n = c
    break
  while n == "d":
    n = d
    break
  while n == "e":
    n = e
    break
  while n == "f":
    n = f
    break
  z = r.randint(int(x), int(n))
  return z

#Functions >> Interest

def intrst(x, y, t):
  while x == "pi" or x == "Pi" or x == "PI" or x == "pI" or x == "π":
    x = pi
    break
  while y == "pi" or y == "Pi" or y == "PI" or y == "pI" or y == "π":
    y = pi
    break
  while t == "pi" or t == "Pi" or t == "PI" or t == "pI" or t == "π":
    t = pi
    break
  while x == "a":
    x = a
    break
  while x == "b":
    x = b
    break
  while x == "c":
    x = c
    break
  while x == "d":
    x = d
    break
  while x == "e":
    x = e
    break
  while x == "f":
    x = f
    break
  while y == "a":
    y = a
    break
  while y == "b":
    y = b
    break
  while y == "c":
    y = c
    break
  while y == "d":
    y = d
    break
  while y == "e":
    y = e
    break
  while y == "f":
    y = f
    break
  while t == "a":
    t = a
    break
  while t == "b":
    t = b
    break
  while t == "c":
    t = c
    break
  while t == "d":
    t = d
    break
  while t == "e":
    t = e
    break
  while t == "f":
    t = f
    break
  z = (x * (1 + y) ** t)
  return z

#Functions >> Main Menu

def MainMenu():
  system('cls')
  print("+---------------------------------+".center(100)) #Shows a centered board with the title and author
  print("|  The Complex Calculator v3.0.0  |".center(100))
  print("|             by CMPLX            |".center(100))
  print("+---------------------------------+".center(100))
  print("\n" * 8) #Skips downward 8 spaces
  print("Press ENTER to go to the calculator page".center(100))
  input("".center(50))
  Equations()

#Functions >> Equation Menu

def Equations():
  system('cls')
  #Shows the equation board and trig board
  print("+-----------------------------------------------------------------+     +------------------------------------------------+".center(100))
  print("|  Getting the Absolute Value of a Number (X): 'abs(X)'           |     |o--------------o Trig Functions o--------------o|".center(100))
  print("|  Using Pi: 'pi' or 'π'                                          |     |  Sine: 'sin(X)'                                |".center(100))
  print("|  Getting the Factorial of a Number (X): 'fact(x)'               |     |  Cosine: 'cos(X)'                              |".center(100))
  print("|  Defining a Variable: 'dv'                                      |     |  Tangent: 'tan(X)'                             |".center(100))
  print("|  Taking a Number (X) to an Exponent (N): 'X ** N' (< 150)       |     |  Inverse Sine: 'asin(X)'                       |".center(100))
  print("|  Getting the Nth Root (N) of a Number(X): 'rt(X, N)'            |     |  Inverse Cosine: 'acos(X)'                     |".center(100))
  print("|  Using a Statistics Function (STAT) on a List (X): 'STAT([X])'  |     |  Inverse Tangent: 'atan(X)'                    |".center(100))
  print("|  Generating a Random Number: 'rand(LOWEST, HIGHEST)' (inclusive)|     |  Hyperbolic Sines: 'sinh(X) and asinh(X)'      |".center(100))
  print("|  Calculate an owed debt: 'intrst(STARTAMOUNT, RATE, PASSEDTIME)'|     |  Hyperbolic Cosines: 'cosh(X) and acosh(X)'    |".center(100))
  print("|  Logarithm (Default, Base 10): 'log10(X)'                       |     |  Hyperbolic Tangents: 'tanh(X) and atanh(X)'   |".center(100))
  print("|  Log-Base-N: 'log(X, BASE)                                     '|     +------------------------------------------------+".center(100))
  print("|  Prime Number Testing: 'prm(X)'                                 |                                                       ".center(100))
  print("|  Modulus: 'X % N'                                                                                                       ".center(100))
  print("+-----------------------------------------------------------------+                                                       ".center(100))
  print("--When referencing a variable, do not capitalize it.\n--Input the passed time in the same time units as the rate and input the rate as a decimal.\n--Type 'back' at any time to go back to the main menu, or 'rs' to reload this page.".center(100))
  print("\na = " + str(a) + "\nb = " + str(b) + "\nc = " + str(c) + "\nd = " + str(d) + "\ne = " + str(e) + "\nf = " + str(f))
  print("\n")
  print("Enter Your Equation:")
  EquInput = input("\n>> ")
  while EquInput == "back":
    MainMenu()
  while EquInput == "dv":
    DefVar()
  while EquInput == "rs":
    Equations()
  while EquInput == "":
    Equations()
  try:
    EquInput_eval = str(eval(EquInput))
  except:
    system('cls')
    print("+-----------------------------------------------------------------+     +------------------------------------------------+".center(100))
    print("|  Getting the Absolute Value of a Number (X): 'abs(X)'           |     |o--------------o Trig Functions o--------------o|".center(100))
    print("|  Using Pi: 'pi' or 'π'                                          |     |  Sine: 'sin(X)'                                |".center(100))
    print("|  Getting the Factorial of a Number (X): 'fact(x)'               |     |  Cosine: 'cos(X)'                              |".center(100))
    print("|  Defining a Variable: 'dv'                                      |     |  Tangent: 'tan(X)'                             |".center(100))
    print("|  Taking a Number (X) to an Exponent (N): 'X ** N' (< 150)       |     |  Inverse Sine: 'asin(X)'                       |".center(100))
    print("|  Getting the Nth Root (N) of a Number(X): 'rt(X, N)'            |     |  Inverse Cosine: 'acos(X)'                     |".center(100))
    print("|  Using a Statistics Function (STAT) on a List (X): 'STAT([X])'  |     |  Inverse Tangent: 'atan(X)'                    |".center(100))
    print("|  Generating a Random Number: 'rand(LOWEST, HIGHEST)' (inclusive)|     |  Hyperbolic Sines: 'sinh(X) and asinh(X)'      |".center(100))
    print("|  Calculate an owed debt: 'intrst(STARTAMOUNT, RATE, PASSEDTIME)'|     |  Hyperbolic Cosines: 'cosh(X) and acosh(X)'    |".center(100))
    print("|  Logarithm (Default, Base 10): 'log10(X)'                       |     |  Hyperbolic Tangents: 'tanh(X) and atanh(X)'   |".center(100))
    print("|  Log-Base-N: 'log(X, BASE)                                     '|     +------------------------------------------------+".center(100))
    print("|  Prime Number Testing: 'prm(X)'                                 |                                                       ".center(100))
    print("|  Modulus: 'X % N'                                                                                                       ".center(100))
    print("+-----------------------------------------------------------------+                                                       ".center(100))
    print("--When referencing a variable, do not capitalize it.\n--Input the passed time in the same time units as the rate and input the rate as a decimal.\n--Type 'back' at any time to go back to the main menu, or 'rs' to reload this page.".center(100))
    print("\na = " + str(a) + "\nb = " + str(b) + "\nc = " + str(c) + "\nd = " + str(d) + "\ne = " + str(e) + "\nf = " + str(f))
    print("\n" * 4)
    print("Sorry, you may have input something wrong, you will see this error if you use a function wrong, press ENTER without")
    print("inputting anything, mistype something, or fail to use brackets when inputting a list (like when using the stat functions).")
    print("If you're sure that you didn't, report this and all of the details to CMPLX.")
    input("\nPress ENTER to retry")
    Equations()
  system('cls')
  print("+-----------------------------------------------------------------+     +------------------------------------------------+".center(100))
  print("|  Getting the Absolute Value of a Number (X): 'abs(X)'           |     |o--------------o Trig Functions o--------------o|".center(100))
  print("|  Using Pi: 'pi' or 'π'                                          |     |  Sine: 'sin(X)'                                |".center(100))
  print("|  Getting the Factorial of a Number (X): 'fact(x)'               |     |  Cosine: 'cos(X)'                              |".center(100))
  print("|  Defining a Variable: 'dv'                                      |     |  Tangent: 'tan(X)'                             |".center(100))
  print("|  Taking a Number (X) to an Exponent (N): 'X ** N' (< 150)       |     |  Inverse Sine: 'asin(X)'                       |".center(100))
  print("|  Getting the Nth Root (N) of a Number(X): 'rt(X, N)'            |     |  Inverse Cosine: 'acos(X)'                     |".center(100))
  print("|  Using a Statistics Function (STAT) on a List (X): 'STAT([X])'  |     |  Inverse Tangent: 'atan(X)'                    |".center(100))
  print("|  Generating a Random Number: 'rand(LOWEST, HIGHEST)' (inclusive)|     |  Hyperbolic Sines: 'sinh(X) and asinh(X)'      |".center(100))
  print("|  Calculate an owed debt: 'intrst(STARTAMOUNT, RATE, PASSEDTIME)'|     |  Hyperbolic Cosines: 'cosh(X) and acosh(X)'    |".center(100))
  print("|  Logarithm (Default, Base 10): 'log10(X)'                       |     |  Hyperbolic Tangents: 'tanh(X) and atanh(X)'   |".center(100))
  print("|  Log-Base-N: 'log(X, BASE)                                     '|     +------------------------------------------------+".center(100))
  print("|  Prime Number Testing: 'prm(X)'                                 |                                                       ".center(100))
  print("|  Modulus: 'X % N'                                                                                                       ".center(100))
  print("+-----------------------------------------------------------------+                                                       ".center(100))
  print("--When referencing a variable, do not capitalize it.\n--Input the passed time in the same time units as the rate and input the rate as a decimal.\n--Type 'back' at any time to go back to the main menu, or 'rs' to reload this page.".center(100))
  print("\na = " + str(a) + "\nb = " + str(b) + "\nc = " + str(c) + "\nd = " + str(d) + "\ne = " + str(e) + "\nf = " + str(f))
  print("\n" * 4)
  print("Here's the result:\n" + str(EquInput_eval))
  input("\nPress ENTER to reset ")
  Equations()

#Functions >> Variable Programming Screen

def DefVar():
  system('cls')
  VarChoice_index = 0
  print("+-----------------------------------+".center(100))
  print("|            Programming            |".center(100))
  print("|            a Variable             |".center(100))
  print("+-----------------------------------+".center(100))
  print("--Type 'back' to go back to the equation screen, or 'rs' to reload this page.")
  print("\n" * 8)
  print("Enter the variable you want to program (Don't capitalize it):")
  VarChoice = input("\n>> ")
  while VarChoice == "back" or VarChoice == "bck" or VarChoice == "bk" or VarChoice == "bc":
    Equations()
  while VarChoice == "rs":
    DefVar()
  while VarChoice == "a":
    VarChoice_index = 1
    break
  while VarChoice == "b":
    VarChoice_index = 2
    break
  while VarChoice == "c":
    VarChoice_index = 3
    break
  while VarChoice == "d":
    VarChoice_index = 4
    break
  while VarChoice == "e":
    VarChoice_index = 5
    break
  while VarChoice == "f":
    VarChoice_index = 6
    break
  try:
    VarInputValidCheck = (1 / VarChoice_index)
  except:
    system('cls')
    VarChoice_index = 0
    print("+-----------------------------------+".center(100))
    print("|            Programming            |".center(100))
    print("|            a Variable             |".center(100))
    print("+-----------------------------------+".center(100))
    print("--Type 'back' to go back to the equation screen, or 'rs' to reload this page.")
    print("\n" * 8)
    print("Sorry, it looks like you didn't input a valid variable, if you're sure you did, \nreport this to CMPLX.")
    input("\nPress ENTER to retry")
    DefVar()
  system('cls')
  print("+-----------------------------------+".center(100))
  print("|            Programming            |".center(100))
  print("|            a Variable             |".center(100))
  print("+-----------------------------------+".center(100))
  print("--Type 'back' to go back to the equation screen, or 'rs' to reload this page.")
  print("\n" * 8)
  print("Enter the number or equation you want to program into this variable:")
  VarValueInput = input("\n>> ")
  while VarValueInput == "back":
    Equations()
  while VarValueInput == "rs":
    DefVar()
  try:
    VarValueInputValidCheck = float(eval(VarValueInput))
  except:
    system('cls')
    VarChoice_index = 0
    print("+-----------------------------------+".center(100))
    print("|            Programming            |".center(100))
    print("|            a Variable             |".center(100))
    print("+-----------------------------------+".center(100))
    print("--Type 'back' to go back to the equation screen, or 'rs' to reload this page.")
    print("\n" * 8)
    print("Sorry, it looks like you didn't input a valid value, if you're sure you did, \nreport this to CMPLX.")
    input("\nPress ENTER to retry")
    DefVar()
  while VarChoice_index == 1:
    if VarChoice_index == 1:
      a = eval(VarValueInput)
      break
    else:
      break
  while VarChoice_index == 2:
    if VarChoice_index == 2:
      b = eval(VarValueInput)
      break
    else:
      break
  while VarChoice_index == 6:
    if VarChoice_index == 6:
      f = eval(VarValueInput)
      break
    else:
      break
  while VarChoice_index == 6:
    if VarChoice_index == 6:
      f = eval(VarValueInput)
      break
    else:
      break
  while VarChoice_index == 6:
    if VarChoice_index == 6:
      f = eval(VarValueInput)
      break
    else:
      break
  while VarChoice_index == 6:
    if VarChoice_index == 6:
      f = eval(VarValueInput)
      break
    else:
      break
  system('cls')
  VarChoice_index = 0
  print("+-----------------------------------+".center(100))
  print("|            Programming            |".center(100))
  print("|            a Variable             |".center(100))
  print("+-----------------------------------+".center(100))
  print("--Type 'back' to go back to the equation screen, or 'rs' to reload this page.")
  print("\n" * 8)
  print("Variable Set... Press Enter to restart:")
  input()
  DefVar()
MainMenu()