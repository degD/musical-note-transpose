
import sys

def transposeTable(step):
    
    musicalNotes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
    for i, note in enumerate(musicalNotes):
        noteUpper = note.upper()
        transposeIndex = (i + int(step)) % len(musicalNotes)
        transposeNote = musicalNotes[transposeIndex]
        print(f"{noteUpper} -> {transposeNote}")
    

if __name__ == "__main__":
    
    transposeTable(sys.argv[1])