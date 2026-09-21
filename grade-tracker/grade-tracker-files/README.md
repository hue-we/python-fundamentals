# Grade Tracker with File Saving

Day 1-2 of week 3. Took the grade tracker from week 2 and gave it the
ability to actually remember students between runs instead of losing
everything the second you close the program.

## What it does

Same as the original grade tracker, add students and view their
averages, but now it saves to a text file and loads that file back in
when you start the program again.

## How to run it

```
python grade_tracker_files.py
```

Type add, view, save, or quit. It auto saves whenever you quit, or you
can save manually any time with the save command.

## Notes to self

- Used the with open() as f pattern for both reading and writing, cleaner
  than manually opening and closing files myself
- Had to think through the file format a bit, went with name colon grades
  separated by commas, simple enough to split back apart when loading
- Wrapped the load function in a try except for FileNotFoundError so it
  does not crash the first time there is no file yet
- Want to come back and handle a badly formatted line without the whole
  thing breaking

## Why this exists

First real exercise for week 3, focused on file handling. This was the
first time something I built actually persisted, felt like a proper
milestone compared to everything just resetting each run.
