# Grade Tracker with Classes

Day 4-5 of week 3. Rebuilt the grade tracker again, this time using
actual classes instead of a plain dictionary. Coming from C# this part
felt more familiar than anything else so far, mostly just relearning the
syntax.

## What it does

Same core idea as before, add students, add grades, view everyone, but
now each student is a proper Student object that knows how to calculate
its own average, and a Classroom object manages the whole list of them.

## How to run it

```
python grade_tracker_oop.py
```

Type add, grade, view, top, or quit. Add a student first, then use grade
to add scores to them one at a time.

## Notes to self

- self instead of this took a second to get used to typing, but the
  concept is identical to C# classes
- Liked moving the average calculation into the Student class itself
  instead of computing it separately every time, feels like the data and
  the logic belong together now
- Classroom holding a list of Student objects instead of a dictionary of
  raw grades is a nicer structure, easier to add more student specific
  stuff later without breaking anything
- Want to combine this with the JSON saving from a couple days ago next,
  will need to figure out converting objects to dictionaries and back

## Why this exists

Second to last stretch of week 3, moving from plain data structures into
actual objects. This one felt the most natural so far since the concepts
carried straight over from C#, just new syntax to get comfortable with.
