# Tuples and Sets

Day 4 of week 2. Smaller exercise than the last two, mostly about getting
a feel for tuples and sets and when you'd actually reach for them instead
of a regular list.

## What it does

Shows a basic tuple example with a coordinate point, then lets you type
in a bunch of numbers and shows you which ones were duplicates by
converting the list into a set.

## How to run it

```
python tuples_and_sets.py
```

Enter numbers one at a time, type done when you're finished, and it'll
show you the original list next to the deduped version.

## Notes to self

- Tuples clicked pretty fast, basically a list you can't accidentally
  change, useful for stuff like coordinates where order matters
- Sets are the more useful one here, turning a list into a set to dedupe
  it in one line is way cleaner than writing a loop to check for
  duplicates manually
- Curious to try set operations next, like union and intersection with
  the & and | operators

## Why this exists

Still working through week 2 data structures. Shorter one today, mostly
building intuition for when tuples or sets are the better tool instead
of defaulting to a list every time.
