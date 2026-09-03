# Simple Calculator

Day 5. A basic calculator that does add, subtract, multiply, and divide,
built mainly to get comfortable writing functions that actually return
values instead of just printing stuff.

## What it does

Asks for two numbers and an operation, then gives you the result. Keeps
running until you tell it to stop.

## How to run it

```
python calculator.py
```

Enter a number, pick an operation, enter the second number, and it'll
print the result.

## Notes to self

- First time separating each operation into its own function instead of
  cramming everything into one block, feels a lot cleaner
- Added a check for dividing by zero so it doesn't blow up
- Should probably wrap the number inputs in a try/except at some point so
  it doesn't crash if someone types letters by accident

## Why this exists

Still working through fundamentals one exercise at a time. This one was
mainly about functions with parameters and return values, which felt more
"real" than the earlier ones.
