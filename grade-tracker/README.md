# Grade Tracker

Day 6-7, the combine project for week 2. Bigger than the daily exercises,
pulls together dictionaries, list comprehensions, and a few built in
functions I hadn't really used yet like max, min, and sorted with a key.

## What it does

Lets you add students with a list of grades, view everyone's average,
check one student's average, see the highest and lowest average in the
class, and rank all students from best to worst average.

## How to run it

```
python grade_tracker.py
```

Type add, view, average, stats, rank, or quit and follow the prompts.

## Notes to self

- Storing grades as a list inside a dictionary, name as the key, felt
  like a natural next step after the contact book
- max and min with a key function took a couple tries to actually
  understand, but once it clicked it felt powerful
- sorted with a lambda for ranking was the trickiest part this week,
  had to look up the syntax a couple times before it stuck
- Would like to save this to a file next so the students don't disappear
  every time I close it

## Why this exists

Wrapping up week 2 on data structures. This was the first project that
felt like it actually needed everything from the week instead of just
practicing one thing at a time.
