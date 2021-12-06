from pynput.keyboard import Key, Listener, Controller
import pyautogui as pya
import pyperclip

EnglishToHebrew = {
    "a": "ש",
    "b": "נ",
    "c": "ב",
    "d": "ג",
    "e": "ק",
    "f": "כ",
    "g": "ע",
    "h": "י",
    "i": "ן",
    "j": "ח",
    "k": "ל",
    "l": "ך",
    "m": "צ",
    "n": "מ",
    "o": "ם",
    "p": "פ",
    "q": "/",
    "r": "ר",
    "s": "ד",
    "t": "א",
    "u": "ו",
    "v": "ה",
    "w": "'",
    "x": "ס",
    "y": "ט",
    "z": "ז",
    "A": "ש",
    "B": "נ",
    "C": "ב",
    "D": "ג",
    "E": "ק",
    "F": "כ",
    "G": "ע",
    "H": "י",
    "I": "ן",
    "J": "ח",
    "K": "ל",
    "L": "ך",
    "M": "צ",
    "N": "מ",
    "O": "ם",
    "P": "פ",
    "Q": "/",
    "R": "ר",
    "S": "ד",
    "T": "א",
    "U": "ו",
    "V": "ה",
    "W": "'",
    "X": "ס",
    "Y": "ט",
    "Z": "ז",
    ",": "ת",
    ".": "ץ",
    "/": ".",
    ";": "ף",
}

HebrewToEnglish = {
    "ש": "a",
    "נ": "b",
    "ב": "c",
    "ג": "d",
    "ק": "e",
    "כ": "f",
    "ע": "g",
    "י": "h",
    "ן": "i",
    "ח": "j",
    "ל": "k",
    "ך": "l",
    "צ": "m",
    "מ": "n",
    "ם": "o",
    "פ": "p",
    "/": "q",
    "ר": "r",
    "ד": "s",
    "א": "t",
    "ו": "u",
    "ה": "v",
    "'": "w",
    "ס": "x",
    "ט": "y",
    "ז": "z",
    "ת": ",",
    "ץ": ".",
    ".": "/",
    "ף": ";",
}

English = [
	'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]

Hebrew = [
	'א',
	'ב',
	'ג',
	'ד',
	'ה',
	'ו',
	'ז',
	'ח',
	'ט',
	'י',
	'כ',
	'ל',
	'מ',
	'נ',
	'ס',
	'ע',
	'פ',
	'צ',
	'ק',
	'ר',
	'ש',
	'ת',
]

keyboard = Controller()

def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    return pyperclip.paste()

def changeLanguage(text):
    finelText = ""
    if text[0] in English:
        for char in text:
            if char in EnglishToHebrew:
                finelText += EnglishToHebrew[char]
            else:
                finelText += char
                
    elif text[0] in Hebrew:
        for char in text:
            if char in HebrewToEnglish:
                finelText += HebrewToEnglish[char]
            else:
                finelText += char

    return finelText

def on_press(key):
    if str(key) == 'Key.f9':
        var = copy_clipboard()
        print(changeLanguage(var))
        keyboard.type(changeLanguage(var))

with Listener(on_press=on_press) as listener:
    listener.join()
