def decrypt(a):
    b = ""
    length = len(a)
    count = 1
    for i in range(length):
        x = ord(a[i])
        b+= chr(x-count)
        count+=1
    return b.upper()

x = input("Enter the string to be decrypted: ")
print("Decrypted String: " + decrypt(x))
