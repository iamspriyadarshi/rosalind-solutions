# Written by Shreyansh Priyadarshi
# This code can convert DNA chain into RNA chain.

# Enter DNA sequence below.
DNA = ''
RNA = ''
for i in DNA:
    if i == 'T':
        RNA += 'U'
    else:
        RNA += i

print(RNA)
