
import sys

helpMessage = """
Run `python transpose.py NUMBER` to print a table of musical notes by transposing NUMBER steps.
Run with `-h`, `--help`, or without any argument to get this help message.
Have a nice day!
"""


def transposeTable(step):
    
    musicalNotes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
    for i, note in enumerate(musicalNotes):
        noteUpper = note.upper()
        transposeIndex = (i + int(step)) % len(musicalNotes)
        transposeNoteUpper = musicalNotes[transposeIndex].upper()
        print(f"{noteUpper.ljust(2)} -> {transposeNoteUpper}")
    

if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print("")
    transposeTable(sys.argv[1])