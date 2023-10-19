"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        count = 0
        for freq in items:
            if item == freq or str(item)==str(freq):
                count += 1
        frequencies[str(item)] = count
    return frequencies
 
