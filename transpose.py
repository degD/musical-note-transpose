
import sys

def transposeTable(step):
    
    musicalNotes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
    for i, note in enumerate(musicalNotes):
        noteUpper = note.upper()
        transposeIndex = (i + int(step)) % len(musicalNotes)
        transposeNoteUpper = musicalNotes[transposeIndex].upper()
        print(f"{noteUpper.ljust(2)} -> {transposeNoteUpper}")
    

if __name__ == "__main__":
    
    transposeTable(sys.argv[1])