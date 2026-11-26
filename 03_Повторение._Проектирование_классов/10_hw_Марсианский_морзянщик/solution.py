class MarvinMorseCoder:
    MORSE_CODE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    @staticmethod
    def encode(text):
        d = MarvinMorseCoder.MORSE_CODE
        words = []
        for w in text.upper().split():
            words.append(' '.join(d[c] for c in w if c in d))
        return '   '.join(words)

    @staticmethod
    def decode(morse):
        d = {v: k for k, v in MarvinMorseCoder.MORSE_CODE.items()}
        words = []
        for w in morse.split('   '):
            words.append(''.join(d.get(c, '?') for c in w.split()))
        return ' '.join(words)
