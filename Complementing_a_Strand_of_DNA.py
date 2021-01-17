# Written by Shreyansh Priyadarshi.
# This code can reverse the DNA chain and then find its complementary strand.

# Enter DNA sequence below between ''.
DNA = ''
reverse_complement = ''

for i in DNA:
    if i == 'A':
        reverse_complement += 'T'
    elif i == 'T':
        reverse_complement += 'A'
    elif i == 'C':
        reverse_complement += 'G'
    else:
        reverse_complement += 'C'

reverse_complement_output = ''.join(reversed(reverse_complement))
print(reverse_complement_output)
