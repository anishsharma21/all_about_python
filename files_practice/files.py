# with open('pi_digits.txt') as file:
#     print(file.readlines())
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line
print(pi_string)