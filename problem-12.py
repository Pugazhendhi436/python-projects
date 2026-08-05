#regex expression 

import re

text = "The rain in Spain"
pattern = r"ain"
matches = re.findall(pattern, text)
print(matches)

if re.fullmatch(pattern, text):
    print("Full match found")

else:
    print("No full match found")

list_of_strings = ["The rain in Spain", "The sun in Spain", "The snow in Spain"]
for string in list_of_strings:
    if re.search(pattern, string):
        print(f"Match found in: {string}")
    else:
        print(f"No match found in: {string}")

for string in list_of_strings:
    if re.match(pattern, string):
        print(f"Match found at the beginning of: {string}")
    else:
        print(f"No match found at the beginning of: {string}")


text = "I love programming in Python"
pattern = re.escape("Python")
if re.search(pattern, text):
    print("Match found for 'Python' in the text")

text = "The pizza was amazing but the fizz and buzz were too loud"
pattern = r"\b\w+z\w+\b"

matches = re.findall(pattern, text)
print(matches)

#validate alphanumeric id

pattern = r"\w+"
test_strings = ["user_123", "User_Name", "invalid id", "bad-char!", "_leadingUnderscore", "ALL_CAPS_99"]

for s in test_strings:
    result = re.fullmatch(pattern, s)
    print(f"{s:<20} -> {'Valid' if result else 'Invalid'}")

#number_pattern_start = r"\d+"

target = "42"
pattern = rf"^{target}\b"
test_strings = ["42 is the answer", "42", "The answer is 42", "420 wide", "142 steps"]

for s in test_strings:
    result = re.search(pattern, s)
    print(f"{s:<17} -> {'Match' if result else 'No match'}")

#number_pattern_end = r"\d+$"

pattern = r"\d+$"
test_strings = ["version 2", "file_backup_3", "hello", "order 99b", "track5", "2024"]

for s in test_strings:
    result = re.search(pattern, s)
    if result:
        print(f"{s:<14} -> Ends with a number")
    else:
        print(f"{s:<14} -> Does not end with a number")

#find all substrings

text = "cat and cattle and catfish and catch and tomcat"
target = "cat"
pattern = re.escape(target)

matches = re.findall(pattern, text)
print(f'Occurrences of "{target}": {matches}')
print(f"Total count: {len(matches)}")

#replace delimeter

test_strings = [
    "one two three",
    "one,two,three",
    "one.two.three",
    "one, two. three",
    "no.delimiters,here today"
]

pattern = r"[ ,.]"

for s in test_strings:
    result = re.sub(pattern, ":", s)
    print(f"{s:<26} -> {result}")

#iterate matches

text = "cat and cattle and catfish and catch and tomcat"
target = "cat"
pattern = re.escape(target)

for i, match in enumerate(re.finditer(pattern, text), start=1):
    print(f'Match {i}: "{match.group()}" found at position {match.start()}-{match.end()}')

