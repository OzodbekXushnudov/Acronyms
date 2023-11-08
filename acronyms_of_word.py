# Author: Ozod Xushnudov
# Date: 11/08/2023
# Theme: Acronyms using Python

"""
An acronym is a short form of a word created by long words or phrases
such as NPL for natural language processing.
"""

user_input = str(input("Enter a Phrase: "))
text = user_input.split()

a = " "
for i in text:
    a = a + str(i[0]).upper()
print(f"{a} - {user_input.title()} ")
