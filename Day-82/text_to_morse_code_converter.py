morse_code_dict = {
    'A' : '.-',
    'B' : '-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..',
    
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    '0' : '-----',
    
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.",
    ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "_": "..--.-", '"': ".-..-.", "$": "...-..-", "@": ".--.-.", " ": "/"
}

def morse_code_converter(message):
    morse_code= ""
    for letter in message:
        if letter in morse_code_dict:
            morse_code += f" {morse_code_dict[letter]}"
        else:
            morse_code += f" {letter}"
    print(morse_code)
    
keep_running = True

while keep_running:
    
    user_input = input("Enter a string: ").upper()
    morse_code_converter(user_input)
    
    options = input("Do you want to convert other sentences? Y/N ").upper()
    if options == 'N':
        keep_running = False
        print('See you next time')