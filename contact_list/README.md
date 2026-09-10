# Contact Book

Day 3 of week 2. A simple contact book that uses dictionaries instead of
lists, since each contact has more than one piece of info attached to it.

## What it does

Lets you add, remove, search for, and view contacts. Each contact stores
a name, phone number, and email.

## How to run it

```
python contact_book.py
```

Type add, remove, search, view, or quit and follow the prompts.

## Notes to self

- Used a dictionary inside a dictionary, name as the outer key and then
  phone and email nested inside, felt like the right structure for this
- Search was basically free once everything was keyed by name, just
  check if the name is in contacts
- Might add support for multiple phone numbers per contact later, would
  need a list nested in there too

## Why this exists

Still on data structures for week 2. This one was mainly about dictionaries
and getting comfortable with key value pairs instead of everything being
a flat list.
