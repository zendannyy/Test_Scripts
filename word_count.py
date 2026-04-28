#!/usr/bin/env python3 
# can also do this with a one-liner with awk
# awk 'BEGIN {IGNORECASE = 1} {for(w=1;w<=NF;w++) print $w}' side_hustles.txt | sort | uniq -c | sort -nr
# tr ' ' '\n' < filename.txt | sort | uniq -c | sort -nr

# used https://stackoverflow.com/questions/40389820/how-to-print-unique-words-from-an-inputted-string for reference 

from collections import Counter
import io
import os
import sys
import re


IGNORE_WORDS = {'a', 'an', 'and', 'are', 'at', 'as', 'be', 'but', 'in', 'is',
                 'of', 'on', 'or', 'the', 'this', 'to', 'you', 'your'}   # type: set

def file_check(filename):
        """Checks if file given as arg exists
        filename (str): Path to the file to process
        
        Returns:
            List[str]: Empty or not"""
        if not os.path.exists(filename):
            print(f"Error: file '{filename}' doesn\'t exist")
            return False

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                # if we can open file, pass
                pass
            return True
        except Exception as e:
            print(f"Error reading file '{filename}': {e}")
            return False

def is_valid_word(word):
    """Check if a word contains at least one alphanumeric character (valid word).
    Args:
        word (str): The word to validate
        
    Returns:
        bool: True if word contains at least one letter or number, False if only punctuation
        """
    return any(char.isalnum() for char in word)
        

def word_count(filename):
    """ 
    Args: 
        The file to be taken as input
    Returns:
        List of unique words from file
    """
    
    if not file_check(filename):
        return False
    
    counter = Counter()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            # Convert to lowercase and find all words by requiring word boundaries, regardless of case
            words = re.findall(r'\b\w+\b', line.lower())
            # Filter out ignored words and update counter
            filtered_words = [word for word in words if word not in IGNORE_WORDS and is_valid_word(word)]
            counter.update(filtered_words)
    
    print("\nWord frequency (excluding common words):")
    print("-" * 40)
    for word, count in counter.most_common():
        print(f"{word}: {count}")

    print(f"\n{len(counter)} Total Unique words: (excluding common words):")
    print("-" * 40)
    unique = [w for w in counter if counter[w] == 1]

    for word in sorted(set(unique)):
        print(word)
  
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <filename>")
        sys.exit(1)

    data = str(sys.argv[1])

    print(data.splitlines(), end="\n"*2) 
    word_count(data)
