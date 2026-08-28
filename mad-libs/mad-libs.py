print("Welcome to Mad Libs!")
print("Answer the prompts and I'll build a silly story.\n")

# Collect words from the user
adjective1 = input("Give me an adjective: ")
noun1 = input("Give me a noun: ")
verb1 = input("Give me a verb (past tense): ")
animal = input("Give me an animal: ")
place = input("Give me a place: ")
adjective2 = input("Give me another adjective: ")
number = input("Give me a number: ")

# Build the story using an f-string
story = f"""
Once upon a time, there was a {adjective1} {noun1} who lived in {place}.
One day, it {verb1} all the way to see a {adjective2} {animal}.
They became friends and had {number} adventures together.
The end!
"""

print(story)