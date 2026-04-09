def decrypt(a):
    # b contains our final output string
    b = ""
    length = len(a)

    # have a running counter variable to subtract from our letter's ascii
    count = 1

    # for each letter in the given string, we subtract
    for i in range(length):
        # converts the char to acii
        x = ord(a[i])
        # reduces the ascii by the running counter variable
        b+= chr(x-count)
        count+=1
    # convert it to upper case
    return b.upper()

x = input("Enter the string to be decrypted: ")
print("Decrypted String: " + decrypt(x))
