#!/bin/python3

import sys

helpMessage = """
Run `python transpose.py NUMBER` to print a table of musical notes by transposing NUMBER steps.
Run with `-h`, `--help`, or without any argument to get this help message.
Have a nice day!
"""


def printMusicalNotes():
    """Print list of notes"""
    musicalNotes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
    for note in musicalNotes:
        print(note.upper(), end=" ")
    print()

def transposeTable(step):
    """Transpose notes by given number of half sounds."""
    musicalNotes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
    for i, note in enumerate(musicalNotes):
        noteUpper = note.upper()
        transposeIndex = (i + int(step)) % len(musicalNotes)
        transposeNoteUpper = musicalNotes[transposeIndex].upper()
        print(f"{noteUpper.ljust(2)} -> {transposeNoteUpper}")
    

if __name__ == "__main__":
    
    if len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv == "--help":
        print(helpMessage)
        exit(1)
        
    try: 
        int(sys.argv[1])
        printMusicalNotes()
        print(f"Transpose {sys.argv[1]} steps:")
        transposeTable(sys.argv[1])
        exit(0)
    except ValueError:
        print("Argument is not an integer. Skipping...")
        exit(1)
        