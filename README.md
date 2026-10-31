# 🧰 Multi-Utility Toolkit (Python)

A simple **menu-driven Python project** that brings several useful tools
together in one program.\
You can check dates and times, perform mathematical calculations,
generate random data, create unique IDs, and work with text files ---
all from one easy menu.

------------------------------------------------------------------------

## ✨ Features

### 🕒 1. Date & Time Operations

-   Display the current date and time.
-   Calculate the number of days between two dates.
-   Format the current date and time using a custom format.
-   Use a stopwatch to measure elapsed time.
-   Run a countdown timer.

### ➗ 2. Mathematical Operations

-   Calculate the factorial of a number.
-   Calculate compound interest.
-   Find sine, cosine, and tangent for an angle.
-   Calculate the area of a circle.

### 🎲 3. Random Data Generation

-   Generate a random number.
-   Generate a list of random numbers.
-   Create a random password using letters, digits, and punctuation.
-   Generate a six-digit OTP.

### 🆔 4. Unique Identifier

-   Generate a UUID (Universally Unique Identifier) using Python's
    `uuid` module.

### 📁 5. File Operations

Uses a custom module named `file_ops.py` to: - Create a new file. -
Write data into a file. - Read data from a file. - Append additional
data to a file.

### 🔍 6. Explore Module Attributes

-   Enter a Python module name.
-   Import the module dynamically using `importlib`.
-   Display its available attributes with `dir()`.

------------------------------------------------------------------------

## 🛠️ Technologies & Python Modules

This project uses Python's built-in modules:

  Module        Purpose
  ------------- --------------------------------------------
  `datetime`    Current date/time and date calculations
  `time`        Stopwatch and countdown delay
  `math`        Factorial, powers, trigonometry and pi
  `random`      Random numbers, passwords and OTP
  `uuid`        Unique identifier generation
  `importlib`   Import modules dynamically
  `string`      Letters, digits and punctuation characters

**Custom module:** `file_ops.py` --- provides the file creation,
writing, reading and appending functions.

------------------------------------------------------------------------

## 📂 Project Structure

``` text
Multi-Utility-Toolkit/
│
├── main.py          # Main program and menu-driven tools
├── file_ops.py      # Custom file handling functions
└── README.md        # Project documentation
```

> Keep `main.py` and `file_ops.py` in the same folder so the file
> operations menu can import the custom module.

------------------------------------------------------------------------

## ▶️ How to Run

1.  Install Python 3 on your computer.
2.  Download or clone this project.
3.  Open the project folder in VS Code or a terminal.
4.  Make sure `main.py` and `file_ops.py` are in the same folder.
5.  Run:

``` bash
python main.py
```

6.  Choose an option from the main menu by entering its number.
7.  Follow the instructions shown on the screen.

------------------------------------------------------------------------

## 🧭 Main Menu

When you run the program, you can choose:

  Option   Tool
  -------- -------------------------------------
  1        Date and Time Operations
  2        Mathematical Operations
  3        Random Data Generation
  4        Generate Unique Identifiers (UUID)
  5        File Operations (custom module)
  6        Explore Module Attributes (`dir()`)
  7        Exit

------------------------------------------------------------------------

## 💡 Python Concepts Practised

-   `import` --- using built-in and custom modules.
-   Functions --- organizing the program into reusable sections.
-   `while` loops --- keeping menus active until the user exits.
-   `if`, `elif`, and `else` --- handling menu choices.
-   `try` and `except` --- handling invalid input.
-   `for` loops and `range()` --- countdowns and list generation.
-   `input()` and `print()` --- interacting with the user.
-   f-strings --- displaying calculated results.
-   List comprehension --- generating a list of random numbers.
-   `break` --- leaving a menu loop.
-   `dir()` --- exploring module attributes.

------------------------------------------------------------------------

## ⚠️ Notes

-   Enter dates in the format `YYYY-MM-DD` when asked.
-   Enter numeric values where the program requests numbers.
-   The custom file operations depend on the functions implemented in
    `file_ops.py`.
-   The generated OTP is a simple random six-digit code for practice; it
    is not a secure authentication system.
-   The password generator is a learning/demo feature and should not be
    treated as a security-audited password manager.

------------------------------------------------------------------------

## 🎯 Project Goal

The goal of this project is to practise Python fundamentals and
understand how different built-in modules and a custom module can work
together in one menu-driven application.

------------------------------------------------------------------------

## 👨‍💻 Author

Created as a Python learning project.

⭐ If you find this project useful, consider giving the repository a
star!
