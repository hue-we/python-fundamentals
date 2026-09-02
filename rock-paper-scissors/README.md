# Rock, Paper, Scissors

Day 4. Classic rock paper scissors against the computer, first to 3 wins
takes the match.

## What it does

Asks you to pick rock, paper, or scissors, the computer picks randomly,
and it keeps score until someone hits 3 wins.

## How to run it

```
python rock_paper_scissors.py
```

Type your choice each round and it'll tell you who won that round and
keep tallying the score.

## Notes to self

- Used a while loop that checks both scores so the game stops as soon as
  someone hits 3
- The win condition check got messy with all those or statements, might
  clean that up later with a function or a dictionary lookup
- Added a basic check for invalid input so it doesn't just crash if you
  type something weird

## Why this exists

Same fundamentals grind. This one was good for practicing comparison
logic and combining conditionals with loops in a slightly more real way
than the last couple exercises.
