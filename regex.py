import re

text = "Hello 123"
result = re.search(r"\d+", text)
day = 2

match day:
   case 1:
       print("Monday")
   case 2:
       print("Tuesday")
   case 3:
       print("Wednesday")
   case _:
       print("Invalid day")
num = 8

match num:
   case 1 | 2 | 3:
       print("Between 1 and 3")
   case _:
       print("Other number")
x = 10

match x:
   case x if x > 5:
       print("Greater than 5")
   case _:
       print("Less or equal to 5")

if result:
   print("Found:", result.group())
   result2 = re.search("cat", "The cat is here ")
   if result2:
       print("Found:", result2.group())
       result3 = re.match("Hello", "world")
       if result3:
           print("Found:", result3.group())


text = "cat bat rat"
print(re.findall("at", text))
for match in re.finditer("at", text):
   print(match.start())

import re

def double(match):
   return str(int(match.group()) * 2)

text = "Values: 10 20 30"

result = re.sub(r"\d+", double, text)

print(result)
greedy=re.search(r"<.*>", "<h1>Title</h1>")
non_greedy=re.search(r"<.*?>", "<h1>Title</h1>")
print(greedy.group())
print(non_greedy.group())
#Literal dot
literal_dot = re.search(r"\.", "file.txt")
print(literal_dot.group())
dot_match = re.search(r"a.*b", "a\nb")  # No match
dot_match_all = re.search(r"a.*b", "a\nb", re.DOTALL)  # Match
print(dot_match)
print(dot_match_all.group())    