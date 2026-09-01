# Number Guessing Game 🔢

Day 3. The computer picks a random number and you have to guess it, with
hints along the way telling you if you're too high or too low.

## What it does

Picks a random number between 1 and 100, then keeps asking you to guess
until you get it right. Tells you how many guesses it took at the end.

## How to run it

```
python number_guesser.py
```

Just type a number when it asks and keep going until you land on the
right one.

## Notes to self

- Used a while loop that keeps running until guess equals secret_number,
  simple but works well here
- The if, elif, else combo for high, low, correct felt way more natural
  this time than it did a couple days ago
- Want to come back and add a guess limit so it doesn't just run forever
  if someone keeps getting it wrong

## Why this exists

Same deal as the last two, rebuilding fundamentals on purpose. This one
was good practice for combining loops and conditionals instead of using
them separately.
