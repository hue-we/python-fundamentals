# Grade Tracker with JSON

Day 3 of week 3. Same grade tracker as the last one, but swapped out the
plain text file for JSON instead. Wanted to see the difference firsthand
after doing it the manual way first.

## What it does

Same as before, add students and view their averages, but now it saves
and loads using json.dump and json.load instead of splitting strings by
hand.

## How to run it

```
python grade_tracker_json.py
```

Type add, view, save, or quit. It auto saves on quit, same as the last
version.

## Notes to self

- The difference from the plain text version is honestly kind of wild,
  no more splitting on colons and commas, json.dump just handles the
  whole dictionary for me
- Opened the json file afterward and it is actually readable, nice bonus
  compared to the text file version
- Still wrapped load in a try except for FileNotFoundError, same idea as
  before, just less code needed overall
- Want to try nesting more info per student next, like email or grade
  level, to see how JSON handles that compared to the flat version I had

## Why this exists

Still on file handling for week 3. This one was mainly to compare doing
it manually versus letting a proper format like JSON do the heavy
lifting, and the difference made the point pretty clearly.
