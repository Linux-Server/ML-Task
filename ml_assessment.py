"""
Machine Learning Engineer - Coding Assessment
=============================================
This module contains solutions for three Python problems:
1. Find the Top 5 Most Frequent Words
2. Flexible Anagram Checker
3. Simple Text Similarity Score

"""

import re
from collections import Counter


# ==============================================================================
# Question 1: Find the Top 5 Most Frequent Words
# ==============================================================================

def top_5_words(text: str) -> list:
    """
    Find and return the top 5 most frequently occurring words in the text.
    
    Args:
        text (str): A string containing multiple words separated by spaces 
                    and punctuation marks.
    
    Returns:
        list: A list of tuples containing (word, frequency) for top 5 words.
    
    Notes:
        - Ignores letter casing (case-insensitive)
        - Ignores punctuation marks
        - Returns words sorted by frequency (descending), then alphabetically
    """
    # Remove punctuation and convert to lowercase
    # Using regex to extract only alphanumeric words
    words = re.findall(r'[a-zA-Z]+', text.lower())
    
    # Count word frequencies
    word_counts = Counter(words)
    
    # Get the top 5 most common words
    top_5 = word_counts.most_common(5)
    
    return top_5


def print_top_5_words(text: str) -> None:
    """Print the top 5 most frequent words with their counts."""
    print("Top 5 Most Frequent Words:")
    print("-" * 30)
    top_5 = top_5_words(text)
    for word, count in top_5:
        print(f"{word} {count}")
    print()


# ==============================================================================
# Question 2: Flexible Anagram Checker
# ==============================================================================

def flexible_anagram(str1: str, str2: str) -> str:
    """
    Check if two strings are flexible anagrams.
    
    Flexible anagrams are defined as:
    - Same length: can differ by at most one character
    - Length differs by 1: shorter string's characters must all be in longer string
    - Length differs by more than 1: not flexible anagrams
    
    Args:
        str1 (str): First string
        str2 (str): Second string
    
    Returns:
        str: 'YES' if they are flexible anagrams, 'NO' otherwise
    """
    # Convert to lowercase for case-insensitive comparison
    s1 = str1.lower()
    s2 = str2.lower()
    
    len_diff = abs(len(s1) - len(s2))
    
    # If lengths differ by more than 1, they cannot be flexible anagrams
    if len_diff > 1:
        return 'NO'
    
    # Count characters in both strings
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    if len_diff == 0:
        # Same length: can differ by at most one character
        # Calculate total character differences
        diff = 0
        all_chars = set(count1.keys()) | set(count2.keys())
        for char in all_chars:
            diff += abs(count1.get(char, 0) - count2.get(char, 0))
        
        # If they differ by at most 2 (one char removed, one char added = 2 differences)
        # This accounts for one mismatch (e.g., 'abcd' vs 'abce')
        if diff <= 2:
            return 'YES'
        else:
            return 'NO'
    
    else:
        # Length differs by 1
        # The shorter string's characters must all match with longer string
        # (with at most the extra character as difference)
        if len(s1) > len(s2):
            longer, shorter = count1, count2
        else:
            longer, shorter = count2, count1
        
        # Check if shorter is subset of longer (character-wise)
        diff = 0
        for char, cnt in shorter.items():
            if longer.get(char, 0) < cnt:
                diff += cnt - longer.get(char, 0)
        
        # At most 0 missing characters from shorter in longer
        if diff == 0:
            return 'YES'
        else:
            return 'NO'


# ==============================================================================
# Question 3: Simple Text Similarity Score
# ==============================================================================

def text_similarity(sentence1: str, sentence2: str) -> float:
    """
    Calculate similarity score between two sentences based on unique word overlap.
    
    Formula: Similarity = (2 * |A ∩ B|) / (|A| + |B|)
    where A and B are sets of unique words in the two sentences.
    
    Args:
        sentence1 (str): First sentence
        sentence2 (str): Second sentence
    
    Returns:
        float: Similarity score rounded to 2 decimal places
    
    Notes:
        - Ignores punctuation
        - Case-insensitive comparison
    """
    # Extract words (ignoring punctuation) and convert to lowercase
    words1 = set(re.findall(r'[a-zA-Z]+', sentence1.lower()))
    words2 = set(re.findall(r'[a-zA-Z]+', sentence2.lower()))
    
    # Calculate intersection
    intersection = words1 & words2
    
    # Calculate similarity using the formula
    # Handle edge case where both sets are empty
    if len(words1) + len(words2) == 0:
        return 0.0
    
    similarity = (2 * len(intersection)) / (len(words1) + len(words2))
    
    return round(similarity, 2)


# ==============================================================================
# Sample Runs and Test Cases
# ==============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("MACHINE LEARNING ENGINEER - CODING ASSESSMENT")
    print("=" * 60)
    print()
    
    # -------------------------------------------------------------------------
    # Question 1: Top 5 Most Frequent Words - Sample Runs
    # -------------------------------------------------------------------------
    print("QUESTION 1: Top 5 Most Frequent Words")
    print("=" * 60)
    
    # Example from the problem statement
    text1 = "The quick brown fox jumps over the lazy dog. The fox was very quick and very smart."
    print(f"Input: {text1}")
    print("Output:")
    print_top_5_words(text1)
    
    # Additional test case
    text2 = "Python is great. Python is powerful. Python is easy to learn. Java is also popular."
    print(f"Input: {text2}")
    print("Output:")
    print_top_5_words(text2)
    
    # -------------------------------------------------------------------------
    # Question 2: Flexible Anagram Checker - Sample Runs
    # -------------------------------------------------------------------------
    print("QUESTION 2: Flexible Anagram Checker")
    print("=" * 60)
    
    test_cases_anagram = [
        ('abcd', 'abce'),   # Expected: YES (same length, one char different)
        ('abc', 'abcd'),    # Expected: YES (length differs by 1)
        ('abc', 'abxyz'),   # Expected: NO (length differs by more than 1)
        ('aabb', 'abbb'),   # Expected: YES (same length, one char different)
        ('abc', 'def'),     # Expected: NO (completely different)
        ('listen', 'silent'),  # Expected: YES (perfect anagram)
        ('hello', 'helo'),  # Expected: YES (one char missing)
    ]
    
    for str1, str2 in test_cases_anagram:
        result = flexible_anagram(str1, str2)
        print(f"Input: str1 = '{str1}', str2 = '{str2}'")
        print(f"Output: {result}")
        print()
    
    # -------------------------------------------------------------------------
    # Question 3: Text Similarity Score - Sample Runs
    # -------------------------------------------------------------------------
    print("QUESTION 3: Simple Text Similarity Score")
    print("=" * 60)
    
    test_cases_similarity = [
        (
            "Artificial intelligence is transforming the world.",
            "AI is changing the world."
        ),  # Expected: 0.55
        (
            "Generative AI creates new content.",
            "AI models can generate text, images, or music."
        ),  # Expected: 0.15
        (
            "Cats are lovely animals.",
            "Dogs are friendly pets."
        ),  # Expected: 0.25
        (
            "Machine learning is a subset of AI.",
            "Machine learning uses algorithms to learn patterns."
        ),  # Additional test
    ]
    
    for sent1, sent2 in test_cases_similarity:
        result = text_similarity(sent1, sent2)
        print(f"Input:")
        print(f"  sentence1 = '{sent1}'")
        print(f"  sentence2 = '{sent2}'")
        print(f"Output: {result}")
        print()
    
    print("=" * 60)
    print("ASSESSMENT COMPLETE")
    print("=" * 60)
