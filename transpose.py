
import sys

def transposeTable(step):
    
    musicalNotes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
    for i, note in enumerate(musicalNotes):
        print(f"{note.upper()} -> {musicalNotes[(i+int(step))%len(musicalNotes)]}")
    

if __name__ == "__main__":
    
    transposeTable(sys.argv[1])