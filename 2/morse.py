def Morse(a):
    # This is the basis for all the morse code conversion
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
    
    # words containsthe list of words as words are split with '   '
    words = a.split('   ')
    decoded = ""

    # for each word, we convert each letter back into normal text
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            decoded += sample[letter]
        decoded += " "

    # removing the extra space added to the end
    return decoded.strip()

x = input("Enter the Morse Code to be decoded: ")
print(Morse(x))
