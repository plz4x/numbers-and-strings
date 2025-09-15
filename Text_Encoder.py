print("Welcome to Text Encoder!")
print("A program by plz4x, with assist from Copilot")
# Define dictionaries
encodekey = {
    " ": "000", 
    "A": "001", 
    "B": "002", 
    "C": "003", 
    "D": "004", 
    "E": "005", 
    "F": "006", 
    "G": "007", 
    "H": "008", 
    "I": "009", 
    "J": "010", 
    "K": "011", 
    "L": "012", 
    "M": "013", 
    "N": "014", 
    "O": "015", 
    "P": "016", 
    "Q": "017", 
    "R": "018", 
    "S": "019", 
    "T": "020", 
    "U": "021", 
    "V": "022", 
    "W": "023", 
    "X": "024", 
    "Y": "025", 
    "Z": "026",
    "a": "027", 
    "b": "028", 
    "c": "029", 
    "d": "030", 
    "e": "031", 
    "f": "032", 
    "g": "033", 
    "h": "034", 
    "i": "035", 
    "j": "036", 
    "k": "037", 
    "l": "038", 
    "m": "039", 
    "n": "040", 
    "o": "041", 
    "p": "042", 
    "q": "043", 
    "r": "044", 
    "s": "045", 
    "t": "046", 
    "u": "047", 
    "v": "048", 
    "w": "049", 
    "x": "050", 
    "y": "051", 
    "z": "052",
    "0": "053", 
    "1": "054", 
    "2": "055", 
    "3": "056", 
    "4": "057", 
    "5": "058", 
    "6": "059", 
    "7": "060", 
    "8": "061", 
    "9": "062",
    "!": "063", 
    "@": "064", 
    "#": "065", 
    "$": "066", 
    "%": "067", 
    "^": "068", 
    "&": "069", 
    "*": "070", 
    "(": "071", 
    ")": "072",
    "-": "073", 
    "_": "074", 
    "+": "075", 
    "=": "076", 
    "[": "077", 
    "]": "078", 
    "{": "079", 
    "}": "080", 
    ";": "081", 
    ":": "082", 
    "'": "083", 
    "\"": "084",
    ".": "085", 
    ",": "086", 
    "<": "087", 
    ">": "088", 
    "/": "089", 
    "?": "090", 
    "|": "091", 
    "\\": "092", 
    "`": "093", 
    "~": "094",
    "×": "095", 
    "÷": "096", 
}
# Reverses the above dictionary for decoding (credit to Copilot)
decodekey = {v: k for k, v in encodekey.items()}

while True:
    c = input("Do you want to encode or decode? (Enter E or D): ").upper()
    if c == "E":
        while True:
            mode = input("Enter your desired mode (Type 1 or 2):")
            if mode == 1 or mode == 2:
                break
            else:
                print("ERROR 01: Invalid input")
        iput = input("Enter encode text: ")
        encoded = ""
        try:
            print("Encoding in progress...")
            # Repeats the length of iput times
            for i in range(0, len(iput)):
                encoded += encodekey[iput[i]]
        except KeyError:
            print(f"ERROR 02: Unsupported character \"{iput[i]}\"")
        else:
            print(encoded)
    elif c == "D":
        iput = input("Enter decode text:")
        decoded = ""
        try:
            # Repeats the length of iput times, with i skipping by 3
            for i in range(0, len(iput), 3):
                # Slices a 3-digit chunk from the encoded string
                chunk = iput[i:i+3]
                decoded += decodekey[chunk]
        except KeyError:
            if len(iput) % 3 != 0:
                print("ERROR 04: Invalid input length")
                break
            else:
                print(f"ERROR 03: Unknown char code \"{chunk}\"")
        else:
            print(decoded)
    else:
        print("ERROR 01: Invalid input")

# Snippet of code that types a dictionary for me when I'm too lazy to type all the keys and values
##dictwrite = []
##j = 0
##for items in dictwrite:
##    snippet = f"    \"{items}\": \"0{j}\", "
##    j += 1
##    snippet(dicti)
