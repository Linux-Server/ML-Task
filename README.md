# Machine Learning Engineer - Coding Assessment

A Python-based coding assessment containing three programming challenges focused on text processing and string manipulation.

## 📋 Overview

This repository contains solutions for:

| Question | Task | Description |
|----------|------|-------------|
| 1 | Top 5 Most Frequent Words | Find the most common words in a text block |
| 2 | Flexible Anagram Checker | Check if two strings are "flexible anagrams" |
| 3 | Text Similarity Score | Calculate similarity between two sentences |

## 🚀 Quick Start

### Prerequisites
- Python 3.6+

### Run the Assessment
```bash
python3 ml_assessment.py
```

## 📝 Problem Descriptions

### Question 1: Find the Top 5 Most Frequent Words

**Problem:** Given a block of text, find and print the top 5 most frequently occurring words.

**Rules:**
- Ignore letter casing (case-insensitive)
- Ignore punctuation marks

**Example:**
```
Input: "The quick brown fox jumps over the lazy dog. The fox was very quick and very smart."

Output:
the 3
quick 2
fox 2
very 2
brown 1
```

---

### Question 2: Flexible Anagram Checker

**Problem:** Check if two strings are "flexible anagrams" - nearly anagrams with at most one mismatch.

**Rules:**
- Same length strings: can differ by at most one character
- Length differs by 1: shorter string's characters must all be in longer string
- Length differs by more than 1: NOT flexible anagrams

**Examples:**
| str1 | str2 | Output | Reason |
|------|------|--------|--------|
| `abcd` | `abce` | YES | Same length, one char different |
| `abc` | `abcd` | YES | Length differs by 1 |
| `abc` | `abxyz` | NO | Length differs by more than 1 |
| `listen` | `silent` | YES | Perfect anagram |

---

### Question 3: Simple Text Similarity Score

**Problem:** Calculate a similarity score between two sentences based on unique word overlap.

**Formula:**
$$\text{Similarity} = \frac{2 \times |A \cap B|}{|A| + |B|}$$

Where A and B are sets of unique words in the two sentences.

**Rules:**
- Ignore punctuation
- Case-insensitive comparison
- Output rounded to 2 decimal places

**Examples:**
| Sentence 1 | Sentence 2 | Output |
|------------|------------|--------|
| "Artificial intelligence is transforming the world." | "AI is changing the world." | 0.55 |
| "Cats are lovely animals." | "Dogs are friendly pets." | 0.25 |

---

## 📁 Project Structure

```
ML-Task/
├── ml_assessment.py          # Main solution file with all three functions
├── ML_Engineer_Coding_Assessment_3Q.pdf  # Original problem statement
└── README.md                 # This file
```

## 🔧 Functions

```python
# Question 1
top_5_words(text: str) -> list

# Question 2
flexible_anagram(str1: str, str2: str) -> str  # Returns 'YES' or 'NO'

# Question 3
text_similarity(sentence1: str, sentence2: str) -> float
```

## 📊 Sample Output

```
============================================================
MACHINE LEARNING ENGINEER - CODING ASSESSMENT
============================================================

QUESTION 1: Top 5 Most Frequent Words
============================================================
Input: The quick brown fox jumps over the lazy dog...
Output:
the 3
quick 2
fox 2
very 2
brown 1

QUESTION 2: Flexible Anagram Checker
============================================================
Input: str1 = 'abcd', str2 = 'abce'
Output: YES

QUESTION 3: Simple Text Similarity Score
============================================================
Input:
  sentence1 = 'Artificial intelligence is transforming the world.'
  sentence2 = 'AI is changing the world.'
Output: 0.55

============================================================
ASSESSMENT COMPLETE
============================================================
```

## ✅ Evaluation Criteria

- ✔️ Correctness and logic of the implementation
- ✔️ Code readability and modular design
- ✔️ Handling of edge cases
- ✔️ Proper formatting of output
- ✔️ Comments and documentation

## 📄 License

This project is for assessment purposes only.
