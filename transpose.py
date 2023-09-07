
def transposeTable(step):
    
    musicalNotes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
    for i, note in enumerate(musicalNotes):
        print(f"{note.upper()} -> {musicalNotes[(i+step)%len(musicalNotes)]}")
        