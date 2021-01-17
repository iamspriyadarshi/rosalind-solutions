# Written by Shreyansh Priyadarshi
# This code can find mutation in DNA sequence.

# Enter both DNA sequence below.
first_DNA = ''
second_DNA = ''
difference = 0

for i in range(len(first_DNA)):
    if first_DNA[i] != second_DNA[i]:
        difference += 1

print(difference)
