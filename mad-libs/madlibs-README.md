# Mad Libs Generator 🎭

Day 2 of getting back into Python. This one asks you for a bunch of random 
words and stuffs them into a story, mad-libs style. Basically an excuse to 
practice taking input and formatting strings.

## What it does

Asks for a few words (adjective, noun, verb, animal, place, etc), then 
plugs them all into a little story and prints it out. Simple but kind of 
fun to see how ridiculous the story turns out.

## How to run it

```
python mad_libs.py
```

Just answer the prompts as they come and it'll spit out your story at the end.

## Notes to self

- Used an f-string to build the story, way cleaner than trying to concatenate 
  everything with +
- Could probably clean this up later by storing the answers in a list and 
  looping through the prompts instead of writing out each input() separately
- Thinking about adding a second story template so it's not the same one 
  every time

## Why this exists

Still on the "rebuild the fundamentals" grind. This one was a good one for 
getting comfortable with string formatting and just handling a bunch of 
user input without it turning into a mess.
