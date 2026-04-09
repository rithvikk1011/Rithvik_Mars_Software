The program decrypts by shifting each character backward in ASCII value by a given increasing offset value

For every character in the string:
1. Convert it to ASCII using ord()
2. Subtract the current count
3. Convert it back to a character using chr()
4. Append it to the result
5. Increment count

Formula: new_char = chr(ord(original_char) - count)
