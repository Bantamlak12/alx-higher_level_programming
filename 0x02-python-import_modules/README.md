# **0x02. Python - import & modules**

## **Description**

In this project I've learned:

- how to import functions from another file
- how to create a module
- how to use the builtin-in function `dir()`
- how to prevent code in scipt from being executed when imported
- how to use command line arguments in a python programs

## **Requirements**

- Not allowed to use `*` for importing or `__import__`
- Not allowed to import any module
- Not allowed to use `try/except`
- The code should not be executed when imported - by using `__import__`

## **Test ✔️**

[Test: ](https://github.com/Bantamlak12/alx-higher_level_programming/tree/master/0x02-python-import_modules/test)
A test folder provided by alx_africa in partnership with Holberton school.

## **Tasks 📃**

- **0. Import a simple function from a simple file**

  - [0-add.py: ](https://github.com/Bantamlak12/alx-higher_level_programming/blob/master/0x02-python-import_modules/0-add.py)is a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`

  * The program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line.
  * Use the word `add_0` once

* **1. My first toolbox!**

  - [1-calculation.py: ](https://github.com/Bantamlak12/alx-higher_level_programming/blob/master/0x02-python-import_modules/1-calculation.py)is a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

  * `a` and `b` must be defined in 2 different lines: `a = 10` and another `b = 5`

* **2. How to make a script dynamic!**

  - [2-args.py: ](https://github.com/Bantamlak12/alx-higher_level_programming/blob/master/0x02-python-import_modules/2-args.py) is a program that prints the number of and the list of its arguments.

  - The output should be:
    - Number of argument(s) followed by `argument`(if number is one) or `arguments`(otherwise), followed by
    - `:` (or `.` if no arguments were passed) followed by
    * a new line, followed by (if at least one argument),
    * one line per argument:
      - the position of the argument (starting at 1) followed by :, followed by the argument value and a new line

* **3. Infinite addition**

  - [3-infinite_add.py: ](https://github.com/Bantamlak12/alx-higher_level_programming/blob/master/0x02-python-import_modules/3-infinite_add.py)is a program that prints the result of the addition of all arguments.

  * The output should be the result of the addition of all arguments, followed by a new line.

* **4. Who are you?**

  - [4-hidden_discovery.py: ](https://github.com/Bantamlak12/alx-higher_level_programming/blob/master/0x02-python-import_modules/4-hidden_discovery.py)is a program that prints all the names defined by the compiled module <a href="https://github.com/holbertonschool/0x02.py/" target="_blank">hidden_4.pyc</a>

  * You should print one name per line, in alpha order
  * You should print only names that do not start with `__`
  * Make sure you are running your code in Python3.8.x (`hidden_4.pyc` has been compiled with this version)

* **5. Everything can be imported**

  - [5-variable_load.py: ](https://github.com/Bantamlak12/alx-higher_level_programming/blob/master/0x02-python-import_modules/5-variable_load.py)is a program that imports the variable a from the file variable_load_5.py and prints its value.

* **6. Build my own calculator!**

  - [100-my_calculator.py](https://github.com/Bantamlak12/alx-higher_level_programming/blob/master/0x02-python-import_modules/100-my_calculator.py)is a program that imports all functions from the file calculator_1.py and handles basic operations.

  * Usage: `./100-my_calculator.py a operator b`
    - If the number of arguments is not 3, The program has to:
      - print `Usage: ./100-my_calculator.py <a> <operator> <b>` followed with a new line
      * exit with the value 1
    * `operator` can be:
      - `+` for addition
      * `-` for subtraction
      * `*` for multiplication
      * `/` for division
    * If the operator is not one of the above:
      - print `Unknown operator. Available operators: +, -, * and /` followed with a new line
      * exit with the value `1`
    * The result should be printed like this: `<a> <operator> <b> = <result>`, followed by a new line

* **7. Easy print**

  - [101-easy_print.py: ](https://github.com/Bantamlak12/alx-higher_level_programming/blob/master/0x02-python-import_modules/101-easy_print.py)is a program that prints `#pythoniscool`, followed by a new line, in the standard output.

* **9. Fast alphabet**
  - [103-fast_alphabet.py: ](https://github.com/Bantamlak12/alx-higher_level_programming/blob/master/0x02-python-import_modules/103-fast_alphabet.py)is a program that prints the alphabet in uppercase, followed by a new line.
