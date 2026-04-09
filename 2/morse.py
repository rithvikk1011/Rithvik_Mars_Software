def Morse(a):
    sample = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
        ".": "E", "..-.": "F", "--.": "G", "....": "H",
        "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
        "--": "M", "-.": "N", "---": "O", ".--.": "P",
        "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
        "-.--": "Y", "--..": "Z",
        "-----": "0", ".----": "1", "..---": "2",
        "...--": "3", "....-": "4", ".....": "5",
        "-....": "6", "--...": "7", "---..": "8",
        "----.": "9"
    }

    words = a.split('   ')
    decoded = ""

    for word in words:
        letters = word.split(' ')
        for letter in letters:
            decoded += sample[letter]
        decoded += " "
    
    return decoded.strip()

x = input("Enter the Morse Code to be decoded: ")
print(Morse(x))
