#!/usr/bin/env python3
"""
Fuzzy Matching & String Similarity Deduplication
Calculates Levenshtein similarity to merge disparate vendor records.
"""
from difflib import SequenceMatcher

def string_similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower().strip(), b.lower().strip()).ratio()

def demonstrate_fuzzy_dedup():
    vendor_names = [
        "Microsoft Corporation",
        "Microsoft Corp",
        "MSFT",
        "Amazon Web Services Inc",
        "Amazon AWS",
        "Google LLC",
        "Google Alphabet"
    ]

    print("Finding fuzzy vendor matches (Threshold >= 0.70):")
    matches = []
    for i in range(len(vendor_names)):
        for j in range(i + 1, len(vendor_names)):
            score = string_similarity(vendor_names[i], vendor_names[j])
            if score >= 0.60:
                print(f"  Match: '{vendor_names[i]}' <==> '{vendor_names[j]}' (Score: {score:.2%})")

if __name__ == "__main__":
    demonstrate_fuzzy_dedup()
