def create_morse(message):
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-',
    'F': '..-.', 'G': '--.', 'H': '....'}
    string = [*message]
    print(string)
    morse_code=[]
    for char in string:
        for key in MORSE_CODE_DICT:
            if char == key:
                morse_code.append(MORSE_CODE_DICT[key])
    print(morse_code)





message = input("what's the message you want in morse code?").upper()




create_morse(message)
