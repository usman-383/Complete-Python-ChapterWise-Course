# Day_1 — Python basics (Chapter index)

This folder contains the Day 1 chapter files for a beginner-friendly Python course. The files are small, self-contained examples and practice problems that demonstrate basic Python syntax, data types, operators, input, and simple programs.

Layout (files and purpose)

- `1First_program.py` — First Python program examples and simple prints. Shows how to print strings and numbers, variable assignment, and using `type()`.
- `2Data_type.py` — Explanations and examples of Python data types: `str`, `int`, `float`, `bool`, and `NoneType`. Includes small practice examples for arithmetic operations.
- `3Type_of_operator.py` — Demonstrates operator categories: arithmetic, relational (comparison), assignment (including compound assignments), and logical operators. Contains short examples and printed outputs.
- `4Input_in_python.py` — How to use `input()` and how to cast inputs to `int` and `float`. Shows reading multiple values and printing types.
- `5Practice.py` — Practice questions/programs: sum of two numbers, square area, average of two floats, and a comparison exercise.

Runner script

- `run_all_day1.py` — A small runner that executes the files in order. It will skip interactive examples by default and ask before running them so you can provide input when needed.

How this README helps

- Quick index: find any example by filename and know what it demonstrates.
- Run instructions for Windows PowerShell so beginners can execute examples easily.
- Small tips about input casting and integer vs float behavior.

How to run these files (Windows PowerShell)

Open PowerShell and change directory to this folder, for example:

```powershell
cd "b:\Programming\1Python\Python_Chapterswise_Code\Day_1"
```

Run a single example with the Python interpreter (replace `N` with the file number):

```powershell
python .\1First_program.py
python .\2Data_type.py
python .\3Type_of_operator.py
python .\4Input_in_python.py
python .\5Practice.py
```

Notes and tips

- `input()` always returns a string. Convert with `int()` or `float()` when you need numeric types.
- Using `/` produces a float result; use `//` for integer (floor) division.
- Compound assignment operators (like `+=`, `-=`) update a variable in-place and are a concise way to write `x = x + y`.
- Many example files print results and `type()` to make outputs explicit — this is intentional for learners.

Suggested next steps for the learner

- Edit `5Practice.py` and try new inputs to see different outputs.
- Add small comments or additional print statements to observe intermediate values.
- When comfortable, move to `Day_2` to explore strings and slicing.

If you want, I can also:

- Add short header comments to each Python file explaining purpose (I can update the files in-place).
- Create a single runner script `run_all_day1.py` that executes each example and prints separators between outputs.

How to use the runner

```powershell
cd "b:\Programming\1Python\Python_Chapterswise_Code\Day_1"
python .\run_all_day1.py
```

When asked about interactive files, type `y` to run them (you'll be prompted for input) or `n` to skip.

---
Last updated: 2025-10-12
