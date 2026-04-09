Morse code uses:
. and - for letters, single space: separates letters, three spaces: separates words

1. Dictionary Mapping:
A dictionary is used to map Morse code to characters
Example: ".-": A
2. Split into Words:
words = a.split('   '), this splits input into words using 3 spaces
3. Split into Letters
letters = word.split(' '), each word is split into individual morse letters using 1 space
4. Decode Each Letter: If the morse code is in the dictionary, it is appended to the decoded string
5. Add Spaces Between Words: After decoding a word, a space is added
6. Remove Extra Space: return decoded.strip(), removes the extra space at the end
