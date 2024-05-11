morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.', ' ': '/'
}

morse_code_chars = {'-', '.', '/', ' '}


welcome = """
 __  __                        ____          _
|  \/  | ___  _ __ ___  ___   / ___|___   __| | ___
| |\/| |/ _ \| '__/ __|/ _ \ | |   / _ \ / _` |/ _ \\
| |  | | (_) | |  \__ \  __/ | |__| (_) | (_| |  __/
|_|__|_|\___/|_|  |___/\___|  \____\___/ \__,_|\___|
 / ___|___  _ ____   _____ _ __| |_ ___ _ __
| |   / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| |__| (_) | | | \ V /  __/ |  | ||  __/ |
 \____\___/|_| |_|\_/ \___|_|   \__\___|_|
      
Welcome!"""

goodbye = """
  ____                 _ _                _ 
 / ___| ___   ___   __| | |__  _   _  ___| |
| |  _ / _ \ / _ \ / _` | '_ \| | | |/ _ \ |
| |_| | (_) | (_) | (_| | |_) | |_| |  __/_|
 \____|\___/ \___/ \__,_|_.__/ \__, |\___(_)
                               |___/        
                    """


def text_to_code(code_string: str) -> str:
    """
    Convert a string of letters, numbers, and punctuation into Morse code.

    Args:
        code_string (str): The input string to be converted to Morse code.

    Returns:
        str: A string representing the input string converted to Morse code, with each character separated by a space.

    Examples:
        >>> text_to_code("SOS")
        '... --- ...'

        >>> text_to_code("HELLO")
        '.... . .-.. .-.. ---'

        >>> text_to_code("123")
        '.---- ..--- ...--'
    """
    code = [morse_code.get(letter) for letter in code_string]
    return " ".join(code)


def code_to_text(code_string: str) -> str:
    """
    Convert Morse code to text.

    Args:
        code_string (str): A string containing Morse code, with each character separated by a space.

    Returns:
        str: A string representing the input Morse code converted to text.

    Examples:
        >>> code_to_text("... --- ...")
        'SOS'

        >>> code_to_text(".... . .-.. .-.. ---")
        'HELLO'

        >>> code_to_text(".---- ..--- ...--")
        '123'
    """
    codes = code_string.split(' ')
    result = []
    for code in codes:
        for key, value in morse_code.items():
            if code == value:
                result.append(key)
    return "".join(result)


def fancy_border(text: str) -> str:
    border = '+' + '-'*(len(text)+4) + '+'
    return f'\n{border}\n|  {text}  |\n{border}'


if __name__ == "__main__":

    choices = """
1. Convert text to Morse code
2. Convert Morse code to text
3. Exit

Select an option: """
    decoder = 0

    print(welcome)
    while decoder != 3:
        try:
            decoder = int(input(f'{choices}'))

            if decoder == 1:
                phrase_to_convert = input(
                    "\nWhat would you like to convert to morse code? ").upper()
                print(
                    f'\nThe morse code is: \n{fancy_border(text_to_code(phrase_to_convert))}')

            elif decoder == 2:
                phrase_to_convert = input(
                    "\nPlease enter some morse code to decode: ").upper()

                if set(phrase_to_convert) <= morse_code_chars:
                    print(
                        f'\nThe secret message is: \n{fancy_border(code_to_text(phrase_to_convert))}')
                else:
                    raise ValueError

            elif decoder == 3:
                print(goodbye)
                break

            else:
                raise ValueError

        except ValueError:
            print("\nInvalid input. Please try again.\n")
